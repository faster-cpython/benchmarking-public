# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_ghccc
- machine: linux-x86_64
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.23x slower
- HPT reliability: 99.61%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 303 ms: 1.10x slower                                                 |
| chameleon      | 7.41 ms                                                | 7.04 ms: 1.05x faster                                                |
| docutils       | 2.77 sec                                               | 4.82 sec: 1.74x slower                                               |
| tornado_http   | 103 ms                                                 | 101 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.16x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 726 ms                                                 | 4.17 sec: 5.75x slower                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 4.57 sec: 6.29x slower                                               |
| async_tree_none            | 472 ms                                                 | 3.43 sec: 7.27x slower                                               |
| async_tree_memoization     | 578 ms                                                 | 4.43 sec: 7.66x slower                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 4.71 sec: 8.20x slower                                               |
| async_tree_none_tg         | 450 ms                                                 | 3.75 sec: 8.34x slower                                               |
| async_tree_io              | 1.16 sec                                               | 13.3 sec: 11.48x slower                                              |
| async_tree_io_tg           | 1.18 sec                                               | 14.1 sec: 11.95x slower                                              |
| Geometric mean             | (ref)                                                  | 8.12x slower                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.4 ms: 1.19x faster                                                |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                 |
| float          | 84.7 ms                                                | 139 ms: 1.64x slower                                                 |
| Geometric mean | (ref)                                                  | 1.12x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.05x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.70 ms: 1.02x slower                                                |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                                 |
| regex_v8       | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                |
| Geometric mean | (ref)                                                  | 1.04x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.00 sec: 1.17x faster                                               |
| pickle_pure_python   | 324 us                                                 | 307 us: 1.06x faster                                                 |
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                                |
| unpickle_list        | 5.29 us                                                | 5.17 us: 1.02x faster                                                |
| unpickle_pure_python | 230 us                                                 | 227 us: 1.01x faster                                                 |
| json_loads           | 28.5 us                                                | 28.4 us: 1.00x faster                                                |
| pickle_dict          | 35.5 us                                                | 36.3 us: 1.02x slower                                                |
| pickle_list          | 5.08 us                                                | 5.20 us: 1.02x slower                                                |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                |
| pickle               | 11.6 us                                                | 12.0 us: 1.04x slower                                                |
| xml_etree_process    | 61.7 ms                                                | 68.3 ms: 1.11x slower                                                |
| xml_etree_generate   | 89.2 ms                                                | 99.2 ms: 1.11x slower                                                |
| xml_etree_parse      | 159 ms                                                 | 219 ms: 1.37x slower                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 162 ms: 1.52x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 11.8 ms: 1.23x slower                                                |
| python_startup_no_site | 6.94 ms                                                | 10.1 ms: 1.45x slower                                                |
| Geometric mean         | (ref)                                                  | 1.34x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.4 ms: 1.15x faster                                                |
| django_template | 34.6 ms                                                | 35.5 ms: 1.03x slower                                                |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 113 us: 1.40x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                |
| scimark_fft                | 382 ms                                                 | 316 ms: 1.21x faster                                                 |
| nbody                      | 97.0 ms                                                | 81.4 ms: 1.19x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 69.0 ms: 1.19x faster                                                |
| tomli_loads                | 2.33 sec                                               | 2.00 sec: 1.17x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 65.2 ms: 1.15x faster                                                |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.15x faster                                                 |
| mako                       | 11.9 ms                                                | 10.4 ms: 1.15x faster                                                |
| fannkuch                   | 417 ms                                                 | 373 ms: 1.12x faster                                                 |
| logging_format             | 7.23 us                                                | 6.49 us: 1.11x faster                                                |
| logging_simple             | 6.46 us                                                | 5.84 us: 1.11x faster                                                |
| raytrace                   | 312 ms                                                 | 283 ms: 1.10x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.61 ms: 1.10x faster                                                |
| chaos                      | 67.0 ms                                                | 61.6 ms: 1.09x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 3.12 us: 1.07x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 726 ms: 1.07x faster                                                 |
| pyflate                    | 482 ms                                                 | 456 ms: 1.06x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 38.6 us: 1.06x faster                                                |
| pickle_pure_python         | 324 us                                                 | 307 us: 1.06x faster                                                 |
| chameleon                  | 7.41 ms                                                | 7.04 ms: 1.05x faster                                                |
| unpickle                   | 15.9 us                                                | 15.1 us: 1.05x faster                                                |
| generators                 | 31.2 ms                                                | 29.7 ms: 1.05x faster                                                |
| sympy_str                  | 300 ms                                                 | 286 ms: 1.05x faster                                                 |
| deepcopy                   | 371 us                                                 | 354 us: 1.05x faster                                                 |
| regex_compile              | 148 ms                                                 | 142 ms: 1.05x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 162 ms: 1.05x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                               |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                                 |
| pathlib                    | 19.3 ms                                                | 18.8 ms: 1.03x faster                                                |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                 |
| unpickle_list              | 5.29 us                                                | 5.17 us: 1.02x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.64 ms: 1.02x faster                                                |
| richards                   | 45.8 ms                                                | 45.0 ms: 1.02x faster                                                |
| tornado_http               | 103 ms                                                 | 101 ms: 1.02x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 227 us: 1.01x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 3.75 ms: 1.01x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 21.3 ms: 1.01x faster                                                |
| json_loads                 | 28.5 us                                                | 28.4 us: 1.00x faster                                                |
| create_gc_cycles           | 1.48 ms                                                | 1.49 ms: 1.01x slower                                                |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 856 us: 1.02x slower                                                 |
| sympy_expand               | 478 ms                                                 | 487 ms: 1.02x slower                                                 |
| scimark_sor                | 129 ms                                                 | 132 ms: 1.02x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                 |
| pickle_dict                | 35.5 us                                                | 36.3 us: 1.02x slower                                                |
| pickle_list                | 5.08 us                                                | 5.20 us: 1.02x slower                                                |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                |
| regex_effbot               | 3.61 ms                                                | 3.70 ms: 1.02x slower                                                |
| mdp                        | 2.63 sec                                               | 2.70 sec: 1.03x slower                                               |
| django_template            | 34.6 ms                                                | 35.5 ms: 1.03x slower                                                |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                 |
| pickle                     | 11.6 us                                                | 12.0 us: 1.04x slower                                                |
| dulwich_log                | 68.5 ms                                                | 71.0 ms: 1.04x slower                                                |
| asyncio_tcp                | 491 ms                                                 | 510 ms: 1.04x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                               |
| hexiom                     | 6.41 ms                                                | 6.79 ms: 1.06x slower                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.45 ms: 1.07x slower                                                |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                                 |
| nqueens                    | 83.3 ms                                                | 89.4 ms: 1.07x slower                                                |
| scimark_lu                 | 118 ms                                                 | 127 ms: 1.08x slower                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 59.1 ms: 1.08x slower                                                |
| gunicorn                   | 1.24 ms                                                | 1.35 ms: 1.09x slower                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.84 ms: 1.09x slower                                                |
| aiohttp                    | 1.15 ms                                                | 1.26 ms: 1.10x slower                                                |
| 2to3                       | 274 ms                                                 | 303 ms: 1.10x slower                                                 |
| xml_etree_process          | 61.7 ms                                                | 68.3 ms: 1.11x slower                                                |
| xml_etree_generate         | 89.2 ms                                                | 99.2 ms: 1.11x slower                                                |
| regex_v8                   | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                |
| go                         | 139 ms                                                 | 159 ms: 1.14x slower                                                 |
| telco                      | 7.10 ms                                                | 8.50 ms: 1.20x slower                                                |
| async_generators           | 463 ms                                                 | 557 ms: 1.20x slower                                                 |
| python_startup             | 9.55 ms                                                | 11.8 ms: 1.23x slower                                                |
| pycparser                  | 1.18 sec                                               | 1.51 sec: 1.28x slower                                               |
| coverage                   | 72.7 ms                                                | 99.1 ms: 1.36x slower                                                |
| xml_etree_parse            | 159 ms                                                 | 219 ms: 1.37x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 10.1 ms: 1.45x slower                                                |
| xml_etree_iterparse        | 107 ms                                                 | 162 ms: 1.52x slower                                                 |
| float                      | 84.7 ms                                                | 139 ms: 1.64x slower                                                 |
| docutils                   | 2.77 sec                                               | 4.82 sec: 1.74x slower                                               |
| dask                       | 372 ms                                                 | 766 ms: 2.06x slower                                                 |
| unpack_sequence            | 54.0 ns                                                | 113 ns: 2.09x slower                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 4.17 sec: 5.75x slower                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 4.57 sec: 6.29x slower                                               |
| async_tree_none            | 472 ms                                                 | 3.43 sec: 7.27x slower                                               |
| async_tree_memoization     | 578 ms                                                 | 4.43 sec: 7.66x slower                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 4.71 sec: 8.20x slower                                               |
| async_tree_none_tg         | 450 ms                                                 | 3.75 sec: 8.34x slower                                               |
| async_tree_io              | 1.16 sec                                               | 13.3 sec: 11.48x slower                                              |
| async_tree_io_tg           | 1.18 sec                                               | 14.1 sec: 11.95x slower                                              |
| Geometric mean             | (ref)                                                  | 1.23x slower                                                         |

Benchmark hidden because not significant (6): json, sqlite_synth, bench_mp_pool, richards_super, coroutines, mypy2
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240321-3.13.0a5+-98575b4-JIT/bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 99.61% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.06x