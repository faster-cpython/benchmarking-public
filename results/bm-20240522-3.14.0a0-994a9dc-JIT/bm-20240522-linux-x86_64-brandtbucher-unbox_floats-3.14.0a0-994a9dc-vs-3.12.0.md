# Results vs. 3.12.0

- fork: brandtbucher
- ref: unbox_floats
- machine: linux-x86_64
- commit hash: 994a9dc
- commit date: 2024-05-22
- overall geometric mean: 1.03x faster
- HPT reliability: 92.68%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 279 ms: 1.02x slower                                                |
| chameleon      | 7.41 ms                                                | 7.13 ms: 1.04x faster                                               |
| docutils       | 2.77 sec                                               | 2.96 sec: 1.07x slower                                              |
| tornado_http   | 103 ms                                                 | 96.8 ms: 1.06x faster                                               |
| Geometric mean | (ref)                                                  | 1.00x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 335 ms: 1.34x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 446 ms: 1.29x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 464 ms: 1.24x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 952 ms: 1.24x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 585 ms: 1.24x faster                                                |
| async_tree_none            | 472 ms                                                 | 386 ms: 1.22x faster                                                |
| async_tree_io              | 1.16 sec                                               | 977 ms: 1.18x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 619 ms: 1.17x faster                                                |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 76.0 ms: 1.11x faster                                               |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                |
| nbody          | 97.0 ms                                                | 110 ms: 1.13x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 139 ms: 1.07x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.80 ms: 1.05x slower                                               |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                                |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                  | 1.04x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                              |
| pickle_pure_python   | 324 us                                                 | 298 us: 1.09x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 83.1 ms: 1.07x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 58.4 ms: 1.06x faster                                               |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                                |
| unpickle_list        | 5.29 us                                                | 5.18 us: 1.02x faster                                               |
| pickle_dict          | 35.5 us                                                | 35.0 us: 1.02x faster                                               |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                               |
| json_loads           | 28.5 us                                                | 29.1 us: 1.02x slower                                               |
| pickle_list          | 5.08 us                                                | 5.23 us: 1.03x slower                                               |
| pickle               | 11.6 us                                                | 12.1 us: 1.04x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.61 ms: 1.10x slower                                               |
| python_startup         | 9.55 ms                                                | 10.9 ms: 1.15x slower                                               |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.92 ms: 1.20x faster                                               |
| django_template | 34.6 ms                                                | 36.4 ms: 1.05x slower                                               |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 335 ms: 1.34x faster                                                |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 446 ms: 1.29x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 464 ms: 1.24x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 952 ms: 1.24x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 585 ms: 1.24x faster                                                |
| async_tree_none            | 472 ms                                                 | 386 ms: 1.22x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                              |
| crypto_pyaes               | 81.9 ms                                                | 68.0 ms: 1.20x faster                                               |
| mako                       | 11.9 ms                                                | 9.92 ms: 1.20x faster                                               |
| fannkuch                   | 417 ms                                                 | 351 ms: 1.19x faster                                                |
| async_tree_io              | 1.16 sec                                               | 977 ms: 1.18x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 63.7 ms: 1.18x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 619 ms: 1.17x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                               |
| logging_format             | 7.23 us                                                | 6.36 us: 1.14x faster                                               |
| logging_simple             | 6.46 us                                                | 5.78 us: 1.12x faster                                               |
| float                      | 84.7 ms                                                | 76.0 ms: 1.11x faster                                               |
| scimark_fft                | 382 ms                                                 | 345 ms: 1.11x faster                                                |
| pyflate                    | 482 ms                                                 | 439 ms: 1.10x faster                                                |
| raytrace                   | 312 ms                                                 | 284 ms: 1.10x faster                                                |
| richards                   | 45.8 ms                                                | 42.0 ms: 1.09x faster                                               |
| pickle_pure_python         | 324 us                                                 | 298 us: 1.09x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 714 ms: 1.09x faster                                                |
| spectral_norm              | 115 ms                                                 | 106 ms: 1.09x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 37.8 us: 1.08x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 83.1 ms: 1.07x faster                                               |
| richards_super             | 51.5 ms                                                | 48.2 ms: 1.07x faster                                               |
| regex_compile              | 148 ms                                                 | 139 ms: 1.07x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                              |
| tornado_http               | 103 ms                                                 | 96.8 ms: 1.06x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                |
| chaos                      | 67.0 ms                                                | 63.2 ms: 1.06x faster                                               |
| xml_etree_process          | 61.7 ms                                                | 58.4 ms: 1.06x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.80 ms: 1.05x faster                                               |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                               |
| chameleon                  | 7.41 ms                                                | 7.13 ms: 1.04x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                                |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.03x faster                                               |
| unpickle_list              | 5.29 us                                                | 5.18 us: 1.02x faster                                               |
| pickle_dict                | 35.5 us                                                | 35.0 us: 1.02x faster                                               |
| generators                 | 31.2 ms                                                | 30.8 ms: 1.01x faster                                               |
| mdp                        | 2.63 sec                                               | 2.60 sec: 1.01x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 3.31 us: 1.01x faster                                               |
| deepcopy                   | 371 us                                                 | 369 us: 1.01x faster                                                |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                |
| dulwich_log                | 68.5 ms                                                | 68.9 ms: 1.01x slower                                               |
| sympy_str                  | 300 ms                                                 | 302 ms: 1.01x slower                                                |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                               |
| async_generators           | 463 ms                                                 | 467 ms: 1.01x slower                                                |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                                |
| 2to3                       | 274 ms                                                 | 279 ms: 1.02x slower                                                |
| dask                       | 372 ms                                                 | 378 ms: 1.02x slower                                                |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                              |
| json_loads                 | 28.5 us                                                | 29.1 us: 1.02x slower                                               |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                |
| sympy_sum                  | 169 ms                                                 | 173 ms: 1.02x slower                                                |
| sqlite_synth               | 2.83 us                                                | 2.91 us: 1.03x slower                                               |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                |
| pickle_list                | 5.08 us                                                | 5.23 us: 1.03x slower                                               |
| bench_thread_pool          | 842 us                                                 | 866 us: 1.03x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.62 ms: 1.03x slower                                               |
| sqlglot_optimize           | 54.8 ms                                                | 56.7 ms: 1.03x slower                                               |
| pickle                     | 11.6 us                                                | 12.1 us: 1.04x slower                                               |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                              |
| nqueens                    | 83.3 ms                                                | 87.0 ms: 1.04x slower                                               |
| django_template            | 34.6 ms                                                | 36.4 ms: 1.05x slower                                               |
| regex_effbot               | 3.61 ms                                                | 3.80 ms: 1.05x slower                                               |
| scimark_sor                | 129 ms                                                 | 136 ms: 1.05x slower                                                |
| sympy_integrate            | 21.4 ms                                                | 22.6 ms: 1.05x slower                                               |
| asyncio_tcp                | 491 ms                                                 | 520 ms: 1.06x slower                                                |
| scimark_lu                 | 118 ms                                                 | 126 ms: 1.07x slower                                                |
| sympy_expand               | 478 ms                                                 | 511 ms: 1.07x slower                                                |
| docutils                   | 2.77 sec                                               | 2.96 sec: 1.07x slower                                              |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                                |
| go                         | 139 ms                                                 | 149 ms: 1.07x slower                                                |
| gc_traversal               | 3.79 ms                                                | 4.08 ms: 1.08x slower                                               |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.09x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 7.61 ms: 1.10x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 174 us: 1.10x slower                                                |
| nbody                      | 97.0 ms                                                | 110 ms: 1.13x slower                                                |
| python_startup             | 9.55 ms                                                | 10.9 ms: 1.15x slower                                               |
| telco                      | 7.10 ms                                                | 8.23 ms: 1.16x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 1.82 ms: 1.23x slower                                               |
| coverage                   | 72.7 ms                                                | 94.8 ms: 1.30x slower                                               |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (4): unpickle, coroutines, deltablue, bench_mp_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, json, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240522-3.14.0a0-994a9dc-JIT/bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint

# HPT report

- Reliability score: 92.68% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x