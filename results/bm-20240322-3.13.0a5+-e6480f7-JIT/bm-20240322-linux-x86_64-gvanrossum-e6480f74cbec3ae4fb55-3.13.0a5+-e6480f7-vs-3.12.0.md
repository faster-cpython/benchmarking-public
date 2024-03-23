# Results vs. 3.12.0

- fork: gvanrossum
- ref: e6480f74cbec3ae4fb55
- machine: linux-x86_64
- commit hash: e6480f7
- commit date: 2024-03-22
- overall geometric mean: 1.01x slower
- HPT reliability: 97.15%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 280 ms: 1.02x slower                                                       |
| chameleon      | 7.41 ms                                                | 7.11 ms: 1.04x faster                                                      |
| docutils       | 2.77 sec                                               | 2.80 sec: 1.01x slower                                                     |
| tornado_http   | 103 ms                                                 | 99.3 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 453 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 743 ms: 1.02x slower                                                       |
| async_tree_none_tg         | 450 ms                                                 | 464 ms: 1.03x slower                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 596 ms: 1.04x slower                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 1.24 sec: 1.05x slower                                                     |
| async_tree_io              | 1.16 sec                                               | 1.23 sec: 1.06x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 80.6 ms: 1.05x faster                                                      |
| nbody          | 97.0 ms                                                | 92.9 ms: 1.04x faster                                                      |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 143 ms: 1.03x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.85 ms: 1.07x slower                                                      |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                      |
| regex_dna      | 212 ms                                                 | 233 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                  | 1.05x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                     |
| unpickle_list        | 5.29 us                                                | 4.85 us: 1.09x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                                       |
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 87.4 ms: 1.02x faster                                                      |
| json_loads           | 28.5 us                                                | 28.0 us: 1.02x faster                                                      |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 109 ms: 1.02x slower                                                       |
| pickle               | 11.6 us                                                | 11.9 us: 1.02x slower                                                      |
| unpickle_pure_python | 230 us                                                 | 239 us: 1.04x slower                                                       |
| pickle_list          | 5.08 us                                                | 5.36 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (2): pickle_dict, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 11.5 ms: 1.20x slower                                                      |
| python_startup_no_site | 6.94 ms                                                | 10.1 ms: 1.46x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.32x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                      |
| django_template | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 112 us: 1.40x faster                                                       |
| comprehensions             | 21.8 us                                                | 17.9 us: 1.21x faster                                                      |
| scimark_fft                | 382 ms                                                 | 341 ms: 1.12x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                     |
| logging_format             | 7.23 us                                                | 6.53 us: 1.11x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.86 us: 1.10x faster                                                      |
| unpickle_list              | 5.29 us                                                | 4.85 us: 1.09x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 75.3 ms: 1.09x faster                                                      |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.49 ms: 1.07x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 70.6 ms: 1.06x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 3.15 us: 1.06x faster                                                      |
| raytrace                   | 312 ms                                                 | 294 ms: 1.06x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.78 ms: 1.06x faster                                                      |
| generators                 | 31.2 ms                                                | 29.5 ms: 1.06x faster                                                      |
| float                      | 84.7 ms                                                | 80.6 ms: 1.05x faster                                                      |
| unpickle                   | 15.9 us                                                | 15.1 us: 1.05x faster                                                      |
| chaos                      | 67.0 ms                                                | 63.9 ms: 1.05x faster                                                      |
| fannkuch                   | 417 ms                                                 | 399 ms: 1.05x faster                                                       |
| deepcopy                   | 371 us                                                 | 355 us: 1.04x faster                                                       |
| nbody                      | 97.0 ms                                                | 92.9 ms: 1.04x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 743 ms: 1.04x faster                                                       |
| chameleon                  | 7.41 ms                                                | 7.11 ms: 1.04x faster                                                      |
| async_tree_none            | 472 ms                                                 | 453 ms: 1.04x faster                                                       |
| sympy_str                  | 300 ms                                                 | 288 ms: 1.04x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                      |
| regex_compile              | 148 ms                                                 | 143 ms: 1.03x faster                                                       |
| tornado_http               | 103 ms                                                 | 99.3 ms: 1.03x faster                                                      |
| pathlib                    | 19.3 ms                                                | 18.7 ms: 1.03x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 164 ms: 1.03x faster                                                       |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 39.8 us: 1.02x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 87.4 ms: 1.02x faster                                                      |
| json_loads                 | 28.5 us                                                | 28.0 us: 1.02x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.66 ms: 1.02x faster                                                      |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                       |
| sqlite_synth               | 2.83 us                                                | 2.85 us: 1.01x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 850 us: 1.01x slower                                                       |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                                       |
| json                       | 5.26 ms                                                | 5.31 ms: 1.01x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 21.7 ms: 1.01x slower                                                      |
| docutils                   | 2.77 sec                                               | 2.80 sec: 1.01x slower                                                     |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                       |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                      |
| pyflate                    | 482 ms                                                 | 489 ms: 1.01x slower                                                       |
| scimark_sor                | 129 ms                                                 | 131 ms: 1.01x slower                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 109 ms: 1.02x slower                                                       |
| dulwich_log                | 68.5 ms                                                | 69.8 ms: 1.02x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                       |
| asyncio_websockets         | 551 ms                                                 | 563 ms: 1.02x slower                                                       |
| 2to3                       | 274 ms                                                 | 280 ms: 1.02x slower                                                       |
| richards_super             | 51.5 ms                                                | 52.7 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 743 ms: 1.02x slower                                                       |
| pickle                     | 11.6 us                                                | 11.9 us: 1.02x slower                                                      |
| async_generators           | 463 ms                                                 | 475 ms: 1.03x slower                                                       |
| sympy_expand               | 478 ms                                                 | 490 ms: 1.03x slower                                                       |
| async_tree_none_tg         | 450 ms                                                 | 464 ms: 1.03x slower                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.03x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 3.93 ms: 1.04x slower                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 596 ms: 1.04x slower                                                       |
| asyncio_tcp                | 491 ms                                                 | 509 ms: 1.04x slower                                                       |
| unpickle_pure_python       | 230 us                                                 | 239 us: 1.04x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.53 ms: 1.04x slower                                                      |
| django_template            | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                      |
| pycparser                  | 1.18 sec                                               | 1.23 sec: 1.05x slower                                                     |
| aiohttp                    | 1.15 ms                                                | 1.21 ms: 1.05x slower                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 1.24 sec: 1.05x slower                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 57.7 ms: 1.05x slower                                                      |
| gunicorn                   | 1.24 ms                                                | 1.31 ms: 1.05x slower                                                      |
| pickle_list                | 5.08 us                                                | 5.36 us: 1.05x slower                                                      |
| async_tree_io              | 1.16 sec                                               | 1.23 sec: 1.06x slower                                                     |
| regex_effbot               | 3.61 ms                                                | 3.85 ms: 1.07x slower                                                      |
| nqueens                    | 83.3 ms                                                | 89.8 ms: 1.08x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                      |
| hexiom                     | 6.41 ms                                                | 7.02 ms: 1.09x slower                                                      |
| regex_dna                  | 212 ms                                                 | 233 ms: 1.10x slower                                                       |
| go                         | 139 ms                                                 | 155 ms: 1.11x slower                                                       |
| scimark_lu                 | 118 ms                                                 | 131 ms: 1.11x slower                                                       |
| python_startup             | 9.55 ms                                                | 11.5 ms: 1.20x slower                                                      |
| telco                      | 7.10 ms                                                | 8.57 ms: 1.21x slower                                                      |
| coverage                   | 72.7 ms                                                | 98.2 ms: 1.35x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 10.1 ms: 1.46x slower                                                      |
| unpack_sequence            | 54.0 ns                                                | 89.0 ns: 1.65x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (11): pprint_pformat, bench_mp_pool, pickle_dict, mdp, xml_etree_parse, richards, async_tree_cpu_io_mixed, coroutines, async_tree_memoization, dask, mypy2
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240322-3.13.0a5+-e6480f7-JIT/bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 97.15% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.06x