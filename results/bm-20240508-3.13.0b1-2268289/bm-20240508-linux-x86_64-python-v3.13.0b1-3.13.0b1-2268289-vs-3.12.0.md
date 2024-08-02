# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b1
- machine: linux-x86_64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.01x slower
- HPT reliability: 99.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 272 ms: 1.01x faster                                       |
| chameleon      | 7.41 ms                                                | 7.11 ms: 1.04x faster                                      |
| docutils       | 2.77 sec                                               | 2.86 sec: 1.03x slower                                     |
| tornado_http   | 103 ms                                                 | 95.8 ms: 1.07x faster                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 346 ms: 1.30x faster                                       |
| async_tree_none            | 472 ms                                                 | 363 ms: 1.30x faster                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 454 ms: 1.27x faster                                       |
| async_tree_io              | 1.16 sec                                               | 936 ms: 1.23x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 589 ms: 1.23x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 477 ms: 1.21x faster                                       |
| async_tree_io_tg           | 1.18 sec                                               | 987 ms: 1.20x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 619 ms: 1.17x faster                                       |
| Geometric mean             | (ref)                                                  | 1.24x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 87.8 ms: 1.10x faster                                      |
| float          | 84.7 ms                                                | 78.5 ms: 1.08x faster                                      |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                  | 1.06x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                       |
| regex_effbot   | 3.61 ms                                                | 3.67 ms: 1.02x slower                                      |
| regex_dna      | 212 ms                                                 | 226 ms: 1.06x slower                                       |
| regex_v8       | 23.1 ms                                                | 26.2 ms: 1.13x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_dict          | 35.5 us                                                | 33.8 us: 1.05x faster                                      |
| tomli_loads          | 2.33 sec                                               | 2.22 sec: 1.05x faster                                     |
| pickle_pure_python   | 324 us                                                 | 311 us: 1.04x faster                                       |
| unpickle_pure_python | 230 us                                                 | 223 us: 1.03x faster                                       |
| xml_etree_process    | 61.7 ms                                                | 60.3 ms: 1.02x faster                                      |
| xml_etree_generate   | 89.2 ms                                                | 87.7 ms: 1.02x faster                                      |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| xml_etree_iterparse  | 107 ms                                                 | 108 ms: 1.01x slower                                       |
| json_loads           | 28.5 us                                                | 28.9 us: 1.01x slower                                      |
| unpickle_list        | 5.29 us                                                | 5.38 us: 1.02x slower                                      |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                      |
| pickle_list          | 5.08 us                                                | 5.30 us: 1.04x slower                                      |
| unpickle             | 15.9 us                                                | 17.0 us: 1.07x slower                                      |
| Geometric mean       | (ref)                                                  | 1.00x faster                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.19 ms: 1.04x slower                                      |
| python_startup         | 9.55 ms                                                | 10.7 ms: 1.12x slower                                      |
| Geometric mean         | (ref)                                                  | 1.08x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.9 ms: 1.09x faster                                      |
| django_template | 34.6 ms                                                | 35.1 ms: 1.01x slower                                      |
| Geometric mean  | (ref)                                                  | 1.04x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 346 ms: 1.30x faster                                       |
| async_tree_none            | 472 ms                                                 | 363 ms: 1.30x faster                                       |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 454 ms: 1.27x faster                                       |
| async_tree_io              | 1.16 sec                                               | 936 ms: 1.23x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 589 ms: 1.23x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 477 ms: 1.21x faster                                       |
| async_tree_io_tg           | 1.18 sec                                               | 987 ms: 1.20x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 619 ms: 1.17x faster                                       |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                       |
| chaos                      | 67.0 ms                                                | 58.8 ms: 1.14x faster                                      |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.14x faster                                      |
| mypy2                      | 830 ms                                                 | 743 ms: 1.12x faster                                       |
| logging_format             | 7.23 us                                                | 6.54 us: 1.10x faster                                      |
| nbody                      | 97.0 ms                                                | 87.8 ms: 1.10x faster                                      |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                       |
| logging_simple             | 6.46 us                                                | 5.91 us: 1.09x faster                                      |
| mako                       | 11.9 ms                                                | 10.9 ms: 1.09x faster                                      |
| pathlib                    | 19.3 ms                                                | 17.9 ms: 1.08x faster                                      |
| float                      | 84.7 ms                                                | 78.5 ms: 1.08x faster                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 69.9 ms: 1.07x faster                                      |
| crypto_pyaes               | 81.9 ms                                                | 76.2 ms: 1.07x faster                                      |
| sympy_sum                  | 169 ms                                                 | 157 ms: 1.07x faster                                       |
| tornado_http               | 103 ms                                                 | 95.8 ms: 1.07x faster                                      |
| generators                 | 31.2 ms                                                | 29.3 ms: 1.07x faster                                      |
| fannkuch                   | 417 ms                                                 | 393 ms: 1.06x faster                                       |
| sympy_str                  | 300 ms                                                 | 284 ms: 1.05x faster                                       |
| pickle_dict                | 35.5 us                                                | 33.8 us: 1.05x faster                                      |
| tomli_loads                | 2.33 sec                                               | 2.22 sec: 1.05x faster                                     |
| sympy_integrate            | 21.4 ms                                                | 20.5 ms: 1.04x faster                                      |
| hexiom                     | 6.41 ms                                                | 6.15 ms: 1.04x faster                                      |
| chameleon                  | 7.41 ms                                                | 7.11 ms: 1.04x faster                                      |
| pickle_pure_python         | 324 us                                                 | 311 us: 1.04x faster                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                      |
| deepcopy_memo              | 40.7 us                                                | 39.4 us: 1.03x faster                                      |
| unpickle_pure_python       | 230 us                                                 | 223 us: 1.03x faster                                       |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.03x faster                                      |
| deepcopy_reduce            | 3.35 us                                                | 3.26 us: 1.03x faster                                      |
| scimark_fft                | 382 ms                                                 | 373 ms: 1.02x faster                                       |
| xml_etree_process          | 61.7 ms                                                | 60.3 ms: 1.02x faster                                      |
| async_generators           | 463 ms                                                 | 452 ms: 1.02x faster                                       |
| nqueens                    | 83.3 ms                                                | 81.4 ms: 1.02x faster                                      |
| dulwich_log                | 68.5 ms                                                | 67.0 ms: 1.02x faster                                      |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                       |
| pyflate                    | 482 ms                                                 | 473 ms: 1.02x faster                                       |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                       |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                       |
| xml_etree_generate         | 89.2 ms                                                | 87.7 ms: 1.02x faster                                      |
| deepcopy                   | 371 us                                                 | 366 us: 1.01x faster                                       |
| scimark_sor                | 129 ms                                                 | 128 ms: 1.01x faster                                       |
| mdp                        | 2.63 sec                                               | 2.60 sec: 1.01x faster                                     |
| pprint_safe_repr           | 776 ms                                                 | 767 ms: 1.01x faster                                       |
| 2to3                       | 274 ms                                                 | 272 ms: 1.01x faster                                       |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.00x faster                                      |
| bench_thread_pool          | 842 us                                                 | 839 us: 1.00x faster                                       |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| xml_etree_iterparse        | 107 ms                                                 | 108 ms: 1.01x slower                                       |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                       |
| django_template            | 34.6 ms                                                | 35.1 ms: 1.01x slower                                      |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.01x slower                                      |
| gc_traversal               | 3.79 ms                                                | 3.85 ms: 1.01x slower                                      |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                       |
| regex_effbot               | 3.61 ms                                                | 3.67 ms: 1.02x slower                                      |
| unpickle_list              | 5.29 us                                                | 5.38 us: 1.02x slower                                      |
| sqlglot_optimize           | 54.8 ms                                                | 55.8 ms: 1.02x slower                                      |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                      |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                       |
| asyncio_websockets         | 551 ms                                                 | 564 ms: 1.02x slower                                       |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.02x slower                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.18 ms: 1.02x slower                                      |
| json                       | 5.26 ms                                                | 5.41 ms: 1.03x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                     |
| docutils                   | 2.77 sec                                               | 2.86 sec: 1.03x slower                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.19 ms: 1.04x slower                                      |
| asyncio_tcp                | 491 ms                                                 | 510 ms: 1.04x slower                                       |
| gunicorn                   | 1.24 ms                                                | 1.29 ms: 1.04x slower                                      |
| aiohttp                    | 1.15 ms                                                | 1.20 ms: 1.04x slower                                      |
| pickle_list                | 5.08 us                                                | 5.30 us: 1.04x slower                                      |
| sqlite_synth               | 2.83 us                                                | 2.96 us: 1.05x slower                                      |
| go                         | 139 ms                                                 | 146 ms: 1.05x slower                                       |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.06x slower                                       |
| unpickle                   | 15.9 us                                                | 17.0 us: 1.07x slower                                      |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.07x slower                                       |
| richards                   | 45.8 ms                                                | 50.5 ms: 1.10x slower                                      |
| richards_super             | 51.5 ms                                                | 57.4 ms: 1.11x slower                                      |
| python_startup             | 9.55 ms                                                | 10.7 ms: 1.12x slower                                      |
| regex_v8                   | 23.1 ms                                                | 26.2 ms: 1.13x slower                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.80 ms: 1.22x slower                                      |
| coverage                   | 72.7 ms                                                | 92.4 ms: 1.27x slower                                      |
| telco                      | 7.10 ms                                                | 173 ms: 24.30x slower                                      |
| Geometric mean             | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (4): xml_etree_parse, sympy_expand, pprint_pformat, dask
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (7) of results/bm-20240508-3.13.0b1-2268289/bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289.json: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.57% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x