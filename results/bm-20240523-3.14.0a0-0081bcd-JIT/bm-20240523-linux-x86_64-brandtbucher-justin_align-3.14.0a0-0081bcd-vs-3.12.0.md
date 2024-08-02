# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_align
- machine: linux-x86_64
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.04x faster
- HPT reliability: 98.64%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 280 ms: 1.02x slower                                                |
| chameleon      | 7.41 ms                                                | 7.07 ms: 1.05x faster                                               |
| docutils       | 2.77 sec                                               | 2.96 sec: 1.07x slower                                              |
| tornado_http   | 103 ms                                                 | 96.8 ms: 1.06x faster                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 336 ms: 1.34x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 444 ms: 1.29x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 464 ms: 1.24x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 585 ms: 1.24x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 954 ms: 1.24x faster                                                |
| async_tree_none            | 472 ms                                                 | 386 ms: 1.22x faster                                                |
| async_tree_io              | 1.16 sec                                               | 959 ms: 1.21x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 619 ms: 1.17x faster                                                |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.3 ms: 1.21x faster                                               |
| float          | 84.7 ms                                                | 72.3 ms: 1.17x faster                                               |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.12x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.08x faster                                                |
| regex_dna      | 212 ms                                                 | 230 ms: 1.09x slower                                                |
| regex_effbot   | 3.61 ms                                                | 3.94 ms: 1.09x slower                                               |
| regex_v8       | 23.1 ms                                                | 25.7 ms: 1.11x slower                                               |
| Geometric mean | (ref)                                                  | 1.05x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                              |
| pickle_pure_python   | 324 us                                                 | 297 us: 1.09x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 82.8 ms: 1.08x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 151 ms: 1.06x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 58.6 ms: 1.05x faster                                               |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.05x faster                                                |
| pickle_dict          | 35.5 us                                                | 34.6 us: 1.03x faster                                               |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                               |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                               |
| pickle               | 11.6 us                                                | 11.8 us: 1.01x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (3): unpickle, unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.61 ms: 1.10x slower                                               |
| python_startup         | 9.55 ms                                                | 10.9 ms: 1.14x slower                                               |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.00 ms: 1.19x faster                                              |
| django_template | 34.6 ms                                                | 36.9 ms: 1.07x slower                                               |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 336 ms: 1.34x faster                                                |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 444 ms: 1.29x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 464 ms: 1.24x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 585 ms: 1.24x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 954 ms: 1.24x faster                                                |
| async_tree_none            | 472 ms                                                 | 386 ms: 1.22x faster                                                |
| scimark_fft                | 382 ms                                                 | 314 ms: 1.22x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 67.5 ms: 1.21x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 62.1 ms: 1.21x faster                                               |
| nbody                      | 97.0 ms                                                | 80.3 ms: 1.21x faster                                               |
| async_tree_io              | 1.16 sec                                               | 959 ms: 1.21x faster                                                |
| fannkuch                   | 417 ms                                                 | 350 ms: 1.19x faster                                                |
| mako                       | 11.9 ms                                                | 10.00 ms: 1.19x faster                                              |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 619 ms: 1.17x faster                                                |
| float                      | 84.7 ms                                                | 72.3 ms: 1.17x faster                                               |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                               |
| logging_format             | 7.23 us                                                | 6.26 us: 1.16x faster                                               |
| spectral_norm              | 115 ms                                                 | 99.5 ms: 1.15x faster                                               |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                               |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                |
| chaos                      | 67.0 ms                                                | 59.3 ms: 1.13x faster                                               |
| pyflate                    | 482 ms                                                 | 437 ms: 1.10x faster                                                |
| richards                   | 45.8 ms                                                | 41.6 ms: 1.10x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.59 ms: 1.10x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 711 ms: 1.09x faster                                                |
| pickle_pure_python         | 324 us                                                 | 297 us: 1.09x faster                                                |
| richards_super             | 51.5 ms                                                | 47.3 ms: 1.09x faster                                               |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                              |
| xml_etree_generate         | 89.2 ms                                                | 82.8 ms: 1.08x faster                                               |
| regex_compile              | 148 ms                                                 | 138 ms: 1.08x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 38.3 us: 1.06x faster                                               |
| tornado_http               | 103 ms                                                 | 96.8 ms: 1.06x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 151 ms: 1.06x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 58.6 ms: 1.05x faster                                               |
| chameleon                  | 7.41 ms                                                | 7.07 ms: 1.05x faster                                               |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.05x faster                                                |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                               |
| pickle_dict                | 35.5 us                                                | 34.6 us: 1.03x faster                                               |
| mdp                        | 2.63 sec                                               | 2.59 sec: 1.02x faster                                              |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                               |
| generators                 | 31.2 ms                                                | 30.9 ms: 1.01x faster                                               |
| json                       | 5.26 ms                                                | 5.22 ms: 1.01x faster                                               |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                               |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                               |
| sqlite_synth               | 2.83 us                                                | 2.85 us: 1.01x slower                                               |
| dulwich_log                | 68.5 ms                                                | 69.1 ms: 1.01x slower                                               |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                |
| pickle                     | 11.6 us                                                | 11.8 us: 1.01x slower                                               |
| dask                       | 372 ms                                                 | 377 ms: 1.01x slower                                                |
| gc_traversal               | 3.79 ms                                                | 3.86 ms: 1.02x slower                                               |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                              |
| 2to3                       | 274 ms                                                 | 280 ms: 1.02x slower                                                |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                                |
| nqueens                    | 83.3 ms                                                | 85.4 ms: 1.03x slower                                               |
| bench_thread_pool          | 842 us                                                 | 864 us: 1.03x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.58 ms: 1.03x slower                                               |
| sqlglot_optimize           | 54.8 ms                                                | 56.4 ms: 1.03x slower                                               |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                              |
| sympy_integrate            | 21.4 ms                                                | 22.4 ms: 1.05x slower                                               |
| go                         | 139 ms                                                 | 147 ms: 1.05x slower                                                |
| asyncio_tcp                | 491 ms                                                 | 522 ms: 1.06x slower                                                |
| scimark_lu                 | 118 ms                                                 | 126 ms: 1.06x slower                                                |
| sympy_expand               | 478 ms                                                 | 509 ms: 1.07x slower                                                |
| django_template            | 34.6 ms                                                | 36.9 ms: 1.07x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                |
| docutils                   | 2.77 sec                                               | 2.96 sec: 1.07x slower                                              |
| regex_dna                  | 212 ms                                                 | 230 ms: 1.09x slower                                                |
| regex_effbot               | 3.61 ms                                                | 3.94 ms: 1.09x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 7.61 ms: 1.10x slower                                               |
| regex_v8                   | 23.1 ms                                                | 25.7 ms: 1.11x slower                                               |
| python_startup             | 9.55 ms                                                | 10.9 ms: 1.14x slower                                               |
| telco                      | 7.10 ms                                                | 8.16 ms: 1.15x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 1.82 ms: 1.23x slower                                               |
| coverage                   | 72.7 ms                                                | 92.7 ms: 1.27x slower                                               |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (10): deepcopy_reduce, unpickle, unpickle_list, pickle_list, bench_mp_pool, async_generators, deepcopy, scimark_sor, deltablue, sympy_str
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240523-3.14.0a0-0081bcd-JIT/bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.64% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x