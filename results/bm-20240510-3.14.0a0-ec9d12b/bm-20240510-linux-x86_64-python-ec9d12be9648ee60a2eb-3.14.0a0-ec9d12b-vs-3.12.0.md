# Results vs. 3.12.0

- fork: python
- ref: ec9d12be9648ee60a2eb
- machine: linux-x86_64
- commit hash: ec9d12b
- commit date: 2024-05-10
- overall geometric mean: 1.00x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 269 ms: 1.02x faster                                                  |
| chameleon      | 7.41 ms                                                | 7.08 ms: 1.05x faster                                                 |
| docutils       | 2.77 sec                                               | 2.81 sec: 1.01x slower                                                |
| tornado_http   | 103 ms                                                 | 93.9 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 363 ms: 1.30x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 349 ms: 1.29x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 459 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 585 ms: 1.24x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 955 ms: 1.21x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 479 ms: 1.21x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 981 ms: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 617 ms: 1.18x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 88.0 ms: 1.10x faster                                                 |
| float          | 84.7 ms                                                | 78.6 ms: 1.08x faster                                                 |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                                  |
| regex_dna      | 212 ms                                                 | 215 ms: 1.01x slower                                                  |
| regex_effbot   | 3.61 ms                                                | 3.78 ms: 1.05x slower                                                 |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                |
| pickle_pure_python   | 324 us                                                 | 310 us: 1.05x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.04x faster                                                  |
| pickle_dict          | 35.5 us                                                | 35.1 us: 1.01x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 108 ms: 1.01x slower                                                  |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                 |
| unpickle_list        | 5.29 us                                                | 5.34 us: 1.01x slower                                                 |
| unpickle             | 15.9 us                                                | 16.1 us: 1.01x slower                                                 |
| json_loads           | 28.5 us                                                | 29.0 us: 1.02x slower                                                 |
| xml_etree_parse      | 159 ms                                                 | 163 ms: 1.02x slower                                                  |
| json_dumps           | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.29 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.3 ms: 1.08x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                 |
| django_template | 34.6 ms                                                | 35.1 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 363 ms: 1.30x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 349 ms: 1.29x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 459 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 585 ms: 1.24x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 955 ms: 1.21x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 479 ms: 1.21x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 981 ms: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 617 ms: 1.18x faster                                                  |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.13x faster                                                 |
| logging_format             | 7.23 us                                                | 6.42 us: 1.13x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.77 us: 1.12x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                |
| chaos                      | 67.0 ms                                                | 60.3 ms: 1.11x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 67.9 ms: 1.11x faster                                                 |
| nbody                      | 97.0 ms                                                | 88.0 ms: 1.10x faster                                                 |
| pathlib                    | 19.3 ms                                                | 17.6 ms: 1.10x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 74.5 ms: 1.10x faster                                                 |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                                  |
| tornado_http               | 103 ms                                                 | 93.9 ms: 1.09x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 157 ms: 1.08x faster                                                  |
| float                      | 84.7 ms                                                | 78.6 ms: 1.08x faster                                                 |
| sympy_str                  | 300 ms                                                 | 279 ms: 1.07x faster                                                  |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                 |
| generators                 | 31.2 ms                                                | 29.3 ms: 1.07x faster                                                 |
| chameleon                  | 7.41 ms                                                | 7.08 ms: 1.05x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 20.5 ms: 1.05x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 310 us: 1.05x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.04x faster                                                  |
| fannkuch                   | 417 ms                                                 | 400 ms: 1.04x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 65.8 ms: 1.04x faster                                                 |
| async_generators           | 463 ms                                                 | 446 ms: 1.04x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                 |
| nqueens                    | 83.3 ms                                                | 80.3 ms: 1.04x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 3.67 ms: 1.03x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 3.27 us: 1.02x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.28 ms: 1.02x faster                                                 |
| pyflate                    | 482 ms                                                 | 474 ms: 1.02x faster                                                  |
| sympy_expand               | 478 ms                                                 | 469 ms: 1.02x faster                                                  |
| 2to3                       | 274 ms                                                 | 269 ms: 1.02x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 764 ms: 1.02x faster                                                  |
| deepcopy                   | 371 us                                                 | 366 us: 1.02x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                                 |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.01x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                                |
| pickle_dict                | 35.5 us                                                | 35.1 us: 1.01x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 40.3 us: 1.01x faster                                                 |
| bench_thread_pool          | 842 us                                                 | 833 us: 1.01x faster                                                  |
| bench_mp_pool              | 24.0 ms                                                | 23.8 ms: 1.01x faster                                                 |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.56 sec: 1.01x faster                                                |
| logging_silent             | 104 ns                                                 | 104 ns: 1.00x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 55.2 ms: 1.01x slower                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 108 ms: 1.01x slower                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.10 ms: 1.01x slower                                                 |
| scimark_sor                | 129 ms                                                 | 130 ms: 1.01x slower                                                  |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                  |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                 |
| unpickle_list              | 5.29 us                                                | 5.34 us: 1.01x slower                                                 |
| unpickle                   | 15.9 us                                                | 16.1 us: 1.01x slower                                                 |
| docutils                   | 2.77 sec                                               | 2.81 sec: 1.01x slower                                                |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.01x slower                                                  |
| django_template            | 34.6 ms                                                | 35.1 ms: 1.01x slower                                                 |
| json_loads                 | 28.5 us                                                | 29.0 us: 1.02x slower                                                 |
| xml_etree_parse            | 159 ms                                                 | 163 ms: 1.02x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 563 ms: 1.02x slower                                                  |
| go                         | 139 ms                                                 | 144 ms: 1.03x slower                                                  |
| json                       | 5.26 ms                                                | 5.44 ms: 1.03x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                                |
| sqlite_synth               | 2.83 us                                                | 2.94 us: 1.04x slower                                                 |
| asyncio_tcp                | 491 ms                                                 | 510 ms: 1.04x slower                                                  |
| pickle_list                | 5.08 us                                                | 5.29 us: 1.04x slower                                                 |
| richards                   | 45.8 ms                                                | 48.0 ms: 1.05x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.78 ms: 1.05x slower                                                 |
| richards_super             | 51.5 ms                                                | 54.5 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                  |
| python_startup             | 9.55 ms                                                | 10.3 ms: 1.08x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.80 ms: 1.22x slower                                                 |
| coverage                   | 72.7 ms                                                | 93.8 ms: 1.29x slower                                                 |
| telco                      | 7.10 ms                                                | 173 ms: 24.41x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (5): xml_etree_process, xml_etree_generate, dask, scimark_fft, spectral_norm
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240510-3.14.0a0-ec9d12b/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x