# Results vs. 3.12.0

- fork: brandtbucher
- ref: decref_escapes
- machine: linux-x86_64
- commit hash: 4711506
- commit date: 2024-09-19
- overall geometric mean: 1.07x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 277 ms: 1.01x slower                                                  |
| docutils       | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                |
| tornado_http   | 103 ms                                                 | 95.1 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 319 ms: 1.48x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 403 ms: 1.43x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 876 ms: 1.35x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 858 ms: 1.35x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 555 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.2 ms: 1.21x faster                                                 |
| float          | 84.7 ms                                                | 70.7 ms: 1.20x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.05x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                 |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                                  |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 77.9 ms: 1.14x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 54.6 ms: 1.13x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 98.0 ms: 1.09x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.06x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                                  |
| json_loads           | 28.5 us                                                | 27.5 us: 1.03x faster                                                 |
| unpickle             | 15.9 us                                                | 15.3 us: 1.03x faster                                                 |
| unpickle_list        | 5.29 us                                                | 5.16 us: 1.02x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| pickle_dict          | 35.5 us                                                | 35.2 us: 1.01x faster                                                 |
| pickle_list          | 5.08 us                                                | 5.37 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.97 ms: 1.19x faster                                                 |
| django_template | 34.6 ms                                                | 35.4 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.9 us: 1.51x faster                                                 |
| async_tree_none            | 472 ms                                                 | 319 ms: 1.48x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 403 ms: 1.43x faster                                                  |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 876 ms: 1.35x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 858 ms: 1.35x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 555 ms: 1.31x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                 |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 67.2 ms: 1.22x faster                                                 |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.21x faster                                                 |
| nbody                      | 97.0 ms                                                | 80.2 ms: 1.21x faster                                                 |
| float                      | 84.7 ms                                                | 70.7 ms: 1.20x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 62.7 ms: 1.20x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                |
| mako                       | 11.9 ms                                                | 9.97 ms: 1.19x faster                                                 |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.29 ms: 1.18x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.21 ms: 1.16x faster                                                 |
| richards                   | 45.8 ms                                                | 39.9 ms: 1.15x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 77.9 ms: 1.14x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 54.6 ms: 1.13x faster                                                 |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                  |
| richards_super             | 51.5 ms                                                | 45.6 ms: 1.13x faster                                                 |
| raytrace                   | 312 ms                                                 | 280 ms: 1.12x faster                                                  |
| fannkuch                   | 417 ms                                                 | 375 ms: 1.11x faster                                                  |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.11x faster                                                  |
| chaos                      | 67.0 ms                                                | 60.8 ms: 1.10x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 98.0 ms: 1.09x faster                                                 |
| tornado_http               | 103 ms                                                 | 95.1 ms: 1.08x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.07x faster                                                  |
| pyflate                    | 482 ms                                                 | 451 ms: 1.07x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.06x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                                  |
| go                         | 139 ms                                                 | 132 ms: 1.06x faster                                                  |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                  |
| regex_compile              | 148 ms                                                 | 142 ms: 1.05x faster                                                  |
| json_loads                 | 28.5 us                                                | 27.5 us: 1.03x faster                                                 |
| unpickle                   | 15.9 us                                                | 15.3 us: 1.03x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                                 |
| async_generators           | 463 ms                                                 | 451 ms: 1.03x faster                                                  |
| unpickle_list              | 5.29 us                                                | 5.16 us: 1.02x faster                                                 |
| json                       | 5.26 ms                                                | 5.14 ms: 1.02x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 761 ms: 1.02x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.02x faster                                                 |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                  |
| pickle_dict                | 35.5 us                                                | 35.2 us: 1.01x faster                                                 |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                 |
| bench_thread_pool          | 842 us                                                 | 838 us: 1.00x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 68.3 ms: 1.00x faster                                                 |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                  |
| 2to3                       | 274 ms                                                 | 277 ms: 1.01x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 3.83 ms: 1.01x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                                  |
| asyncio_tcp                | 491 ms                                                 | 498 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.02x slower                                                |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                 |
| django_template            | 34.6 ms                                                | 35.4 ms: 1.02x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.02x slower                                                |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                  |
| mdp                        | 2.63 sec                                               | 2.70 sec: 1.03x slower                                                |
| sympy_expand               | 478 ms                                                 | 504 ms: 1.05x slower                                                  |
| nqueens                    | 83.3 ms                                                | 87.9 ms: 1.06x slower                                                 |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.06x slower                                                  |
| pickle_list                | 5.08 us                                                | 5.37 us: 1.06x slower                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 57.9 ms: 1.06x slower                                                 |
| generators                 | 31.2 ms                                                | 33.1 ms: 1.06x slower                                                 |
| sympy_integrate            | 21.4 ms                                                | 22.8 ms: 1.07x slower                                                 |
| docutils                   | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.98 ms: 1.09x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                 |
| telco                      | 7.10 ms                                                | 7.94 ms: 1.12x slower                                                 |
| coverage                   | 72.7 ms                                                | 84.5 ms: 1.16x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                                 |
| unpack_sequence            | 54.0 ns                                                | 106 ns: 1.97x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (5): pickle, sympy_str, pprint_pformat, bench_mp_pool, sqlglot_transpile
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240919-3.14.0a0-4711506-JIT/bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x