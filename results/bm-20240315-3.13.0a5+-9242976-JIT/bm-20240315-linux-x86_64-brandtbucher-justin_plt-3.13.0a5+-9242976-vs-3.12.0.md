# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_plt
- machine: linux-x86_64
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.02x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 285 ms: 1.04x slower                                               |
| chameleon      | 7.41 ms                                                | 6.86 ms: 1.08x faster                                              |
| docutils       | 2.77 sec                                               | 2.79 sec: 1.01x slower                                             |
| tornado_http   | 103 ms                                                 | 99.3 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 450 ms: 1.05x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 456 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 737 ms: 1.02x slower                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 599 ms: 1.04x slower                                               |
| async_tree_io_tg           | 1.18 sec                                               | 1.24 sec: 1.05x slower                                             |
| async_tree_io              | 1.16 sec                                               | 1.22 sec: 1.05x slower                                             |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                       |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 81.5 ms: 1.04x faster                                              |
| nbody          | 97.0 ms                                                | 97.9 ms: 1.01x slower                                              |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 155 ms: 1.04x slower                                               |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                               |
| regex_effbot   | 3.61 ms                                                | 3.92 ms: 1.08x slower                                              |
| regex_v8       | 23.1 ms                                                | 25.7 ms: 1.11x slower                                              |
| Geometric mean | (ref)                                                  | 1.07x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                               |
| tomli_loads          | 2.33 sec                                               | 2.17 sec: 1.08x faster                                             |
| unpickle             | 15.9 us                                                | 14.8 us: 1.07x faster                                              |
| unpickle_list        | 5.29 us                                                | 5.09 us: 1.04x faster                                              |
| pickle_dict          | 35.5 us                                                | 34.5 us: 1.03x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 60.1 ms: 1.03x faster                                              |
| json_loads           | 28.5 us                                                | 28.1 us: 1.02x faster                                              |
| xml_etree_generate   | 89.2 ms                                                | 88.4 ms: 1.01x faster                                              |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                              |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                              |
| pickle_list          | 5.08 us                                                | 5.19 us: 1.02x slower                                              |
| xml_etree_iterparse  | 107 ms                                                 | 109 ms: 1.02x slower                                               |
| unpickle_pure_python | 230 us                                                 | 246 us: 1.07x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 11.5 ms: 1.20x slower                                              |
| python_startup_no_site | 6.94 ms                                                | 10.1 ms: 1.46x slower                                              |
| Geometric mean         | (ref)                                                  | 1.32x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.4 ms: 1.04x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 109 us: 1.44x faster                                               |
| comprehensions             | 21.8 us                                                | 18.3 us: 1.19x faster                                              |
| logging_format             | 7.23 us                                                | 6.46 us: 1.12x faster                                              |
| logging_simple             | 6.46 us                                                | 5.83 us: 1.11x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 3.08 us: 1.09x faster                                              |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                               |
| chameleon                  | 7.41 ms                                                | 6.86 ms: 1.08x faster                                              |
| tomli_loads                | 2.33 sec                                               | 2.17 sec: 1.08x faster                                             |
| unpickle                   | 15.9 us                                                | 14.8 us: 1.07x faster                                              |
| deltablue                  | 3.72 ms                                                | 3.48 ms: 1.07x faster                                              |
| deepcopy                   | 371 us                                                 | 351 us: 1.06x faster                                               |
| scimark_fft                | 382 ms                                                 | 363 ms: 1.05x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 77.9 ms: 1.05x faster                                              |
| async_tree_none            | 472 ms                                                 | 450 ms: 1.05x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 38.9 us: 1.05x faster                                              |
| generators                 | 31.2 ms                                                | 29.8 ms: 1.05x faster                                              |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                              |
| float                      | 84.7 ms                                                | 81.5 ms: 1.04x faster                                              |
| logging_silent             | 104 ns                                                 | 100 ns: 1.04x faster                                               |
| unpickle_list              | 5.29 us                                                | 5.09 us: 1.04x faster                                              |
| sympy_sum                  | 169 ms                                                 | 163 ms: 1.04x faster                                               |
| sympy_str                  | 300 ms                                                 | 290 ms: 1.03x faster                                               |
| tornado_http               | 103 ms                                                 | 99.3 ms: 1.03x faster                                              |
| raytrace                   | 312 ms                                                 | 303 ms: 1.03x faster                                               |
| pathlib                    | 19.3 ms                                                | 18.8 ms: 1.03x faster                                              |
| pickle_dict                | 35.5 us                                                | 34.5 us: 1.03x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 60.1 ms: 1.03x faster                                              |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                              |
| json_loads                 | 28.5 us                                                | 28.1 us: 1.02x faster                                              |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.02x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 88.4 ms: 1.01x faster                                              |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                              |
| meteor_contest             | 112 ms                                                 | 112 ms: 1.00x faster                                               |
| docutils                   | 2.77 sec                                               | 2.79 sec: 1.01x slower                                             |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                              |
| nbody                      | 97.0 ms                                                | 97.9 ms: 1.01x slower                                              |
| scimark_sor                | 129 ms                                                 | 130 ms: 1.01x slower                                               |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                               |
| async_generators           | 463 ms                                                 | 469 ms: 1.01x slower                                               |
| async_tree_none_tg         | 450 ms                                                 | 456 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 737 ms: 1.02x slower                                               |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                              |
| sqlite_synth               | 2.83 us                                                | 2.89 us: 1.02x slower                                              |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.16 ms: 1.02x slower                                              |
| pickle_list                | 5.08 us                                                | 5.19 us: 1.02x slower                                              |
| asyncio_tcp                | 491 ms                                                 | 501 ms: 1.02x slower                                               |
| xml_etree_iterparse        | 107 ms                                                 | 109 ms: 1.02x slower                                               |
| pprint_safe_repr           | 776 ms                                                 | 792 ms: 1.02x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 1.51 ms: 1.02x slower                                              |
| asyncio_websockets         | 551 ms                                                 | 564 ms: 1.02x slower                                               |
| bench_thread_pool          | 842 us                                                 | 862 us: 1.02x slower                                               |
| fannkuch                   | 417 ms                                                 | 429 ms: 1.03x slower                                               |
| sympy_expand               | 478 ms                                                 | 492 ms: 1.03x slower                                               |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.03x slower                                             |
| richards_super             | 51.5 ms                                                | 53.3 ms: 1.03x slower                                              |
| richards                   | 45.8 ms                                                | 47.5 ms: 1.04x slower                                              |
| 2to3                       | 274 ms                                                 | 285 ms: 1.04x slower                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 599 ms: 1.04x slower                                               |
| pycparser                  | 1.18 sec                                               | 1.23 sec: 1.04x slower                                             |
| regex_compile              | 148 ms                                                 | 155 ms: 1.04x slower                                               |
| async_tree_io_tg           | 1.18 sec                                               | 1.24 sec: 1.05x slower                                             |
| dulwich_log                | 68.5 ms                                                | 71.8 ms: 1.05x slower                                              |
| gunicorn                   | 1.24 ms                                                | 1.30 ms: 1.05x slower                                              |
| aiohttp                    | 1.15 ms                                                | 1.21 ms: 1.05x slower                                              |
| sqlglot_optimize           | 54.8 ms                                                | 57.6 ms: 1.05x slower                                              |
| async_tree_io              | 1.16 sec                                               | 1.22 sec: 1.05x slower                                             |
| mdp                        | 2.63 sec                                               | 2.77 sec: 1.05x slower                                             |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.06x slower                                               |
| pyflate                    | 482 ms                                                 | 513 ms: 1.06x slower                                               |
| unpickle_pure_python       | 230 us                                                 | 246 us: 1.07x slower                                               |
| pprint_pformat             | 1.57 sec                                               | 1.69 sec: 1.08x slower                                             |
| gc_traversal               | 3.79 ms                                                | 4.09 ms: 1.08x slower                                              |
| regex_effbot               | 3.61 ms                                                | 3.92 ms: 1.08x slower                                              |
| spectral_norm              | 115 ms                                                 | 125 ms: 1.09x slower                                               |
| regex_v8                   | 23.1 ms                                                | 25.7 ms: 1.11x slower                                              |
| nqueens                    | 83.3 ms                                                | 93.2 ms: 1.12x slower                                              |
| scimark_lu                 | 118 ms                                                 | 133 ms: 1.13x slower                                               |
| go                         | 139 ms                                                 | 159 ms: 1.14x slower                                               |
| hexiom                     | 6.41 ms                                                | 7.60 ms: 1.19x slower                                              |
| python_startup             | 9.55 ms                                                | 11.5 ms: 1.20x slower                                              |
| telco                      | 7.10 ms                                                | 8.55 ms: 1.20x slower                                              |
| coverage                   | 72.7 ms                                                | 98.8 ms: 1.36x slower                                              |
| python_startup_no_site     | 6.94 ms                                                | 10.1 ms: 1.46x slower                                              |
| unpack_sequence            | 54.0 ns                                                | 122 ns: 2.26x slower                                               |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                       |

Benchmark hidden because not significant (12): sqlglot_transpile, async_tree_cpu_io_mixed, sympy_integrate, chaos, scimark_monte_carlo, django_template, xml_etree_parse, bench_mp_pool, dask, async_tree_memoization, json, mypy2
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240315-3.13.0a5+-9242976-JIT/bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.07x