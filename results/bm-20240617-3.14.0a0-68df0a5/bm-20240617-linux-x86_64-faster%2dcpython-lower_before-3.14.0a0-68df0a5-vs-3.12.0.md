# Results vs. 3.12.0

- fork: faster-cpython
- ref: lower_before
- machine: linux-x86_64
- commit hash: 68df0a5
- commit date: 2024-06-17
- overall geometric mean: 1.04x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 270 ms: 1.01x faster                                                    |
| docutils       | 2.77 sec                                               | 2.79 sec: 1.01x slower                                                  |
| tornado_http   | 103 ms                                                 | 93.6 ms: 1.10x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 332 ms: 1.35x faster                                                    |
| async_tree_none            | 472 ms                                                 | 370 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 580 ms: 1.25x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 460 ms: 1.25x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 951 ms: 1.22x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 489 ms: 1.18x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 1.01 sec: 1.17x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 622 ms: 1.17x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 88.3 ms: 1.10x faster                                                   |
| float          | 84.7 ms                                                | 78.1 ms: 1.08x faster                                                   |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.11x faster                                                    |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                   |
| regex_effbot   | 3.61 ms                                                | 3.79 ms: 1.05x slower                                                   |
| regex_dna      | 212 ms                                                 | 232 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.18 sec: 1.07x faster                                                  |
| unpickle             | 15.9 us                                                | 14.8 us: 1.07x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 86.3 ms: 1.03x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                   |
| pickle_dict          | 35.5 us                                                | 34.7 us: 1.02x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 106 ms: 1.01x faster                                                    |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                   |
| json_loads           | 28.5 us                                                | 29.0 us: 1.02x slower                                                   |
| unpickle_list        | 5.29 us                                                | 5.50 us: 1.04x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (3): pickle_list, pickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.10 ms: 1.02x slower                                                   |
| python_startup         | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                   |
| django_template | 34.6 ms                                                | 34.4 ms: 1.00x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 371 us                                                 | 270 us: 1.38x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 29.9 us: 1.36x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 332 ms: 1.35x faster                                                    |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                   |
| async_tree_none            | 472 ms                                                 | 370 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 580 ms: 1.25x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 460 ms: 1.25x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 951 ms: 1.22x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.78 us: 1.20x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 489 ms: 1.18x faster                                                    |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 1.01 sec: 1.17x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 622 ms: 1.17x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.24 ms: 1.15x faster                                                   |
| logging_format             | 7.23 us                                                | 6.35 us: 1.14x faster                                                   |
| regex_compile              | 148 ms                                                 | 134 ms: 1.11x faster                                                    |
| chaos                      | 67.0 ms                                                | 60.4 ms: 1.11x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 74.0 ms: 1.11x faster                                                   |
| nbody                      | 97.0 ms                                                | 88.3 ms: 1.10x faster                                                   |
| tornado_http               | 103 ms                                                 | 93.6 ms: 1.10x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.09x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 69.1 ms: 1.09x faster                                                   |
| float                      | 84.7 ms                                                | 78.1 ms: 1.08x faster                                                   |
| sympy_str                  | 300 ms                                                 | 280 ms: 1.07x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 2.18 sec: 1.07x faster                                                  |
| unpickle                   | 15.9 us                                                | 14.8 us: 1.07x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                    |
| nqueens                    | 83.3 ms                                                | 78.2 ms: 1.06x faster                                                   |
| generators                 | 31.2 ms                                                | 29.4 ms: 1.06x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 20.2 ms: 1.06x faster                                                   |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.09 ms: 1.05x faster                                                   |
| async_generators           | 463 ms                                                 | 442 ms: 1.05x faster                                                    |
| dulwich_log                | 68.5 ms                                                | 65.6 ms: 1.04x faster                                                   |
| bench_thread_pool          | 842 us                                                 | 807 us: 1.04x faster                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                   |
| fannkuch                   | 417 ms                                                 | 401 ms: 1.04x faster                                                    |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 86.3 ms: 1.03x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 755 ms: 1.03x faster                                                    |
| pickle_dict                | 35.5 us                                                | 34.7 us: 1.02x faster                                                   |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                  |
| 2to3                       | 274 ms                                                 | 270 ms: 1.01x faster                                                    |
| dask                       | 372 ms                                                 | 367 ms: 1.01x faster                                                    |
| scimark_fft                | 382 ms                                                 | 377 ms: 1.01x faster                                                    |
| sympy_expand               | 478 ms                                                 | 473 ms: 1.01x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 106 ms: 1.01x faster                                                    |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.00x faster                                                   |
| django_template            | 34.6 ms                                                | 34.4 ms: 1.00x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 3.80 ms: 1.00x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 55.0 ms: 1.00x slower                                                   |
| docutils                   | 2.77 sec                                               | 2.79 sec: 1.01x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                   |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                    |
| json_loads                 | 28.5 us                                                | 29.0 us: 1.02x slower                                                   |
| json                       | 5.26 ms                                                | 5.35 ms: 1.02x slower                                                   |
| pyflate                    | 482 ms                                                 | 492 ms: 1.02x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 7.10 ms: 1.02x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                    |
| asyncio_tcp                | 491 ms                                                 | 505 ms: 1.03x slower                                                    |
| scimark_sor                | 129 ms                                                 | 133 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.03x slower                                                  |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                                    |
| unpickle_list              | 5.29 us                                                | 5.50 us: 1.04x slower                                                   |
| sqlite_synth               | 2.83 us                                                | 2.96 us: 1.04x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                   |
| coroutines                 | 23.2 ms                                                | 24.3 ms: 1.05x slower                                                   |
| regex_effbot               | 3.61 ms                                                | 3.79 ms: 1.05x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                    |
| richards                   | 45.8 ms                                                | 49.8 ms: 1.09x slower                                                   |
| richards_super             | 51.5 ms                                                | 56.1 ms: 1.09x slower                                                   |
| regex_dna                  | 212 ms                                                 | 232 ms: 1.09x slower                                                    |
| python_startup             | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                   |
| telco                      | 7.10 ms                                                | 8.33 ms: 1.17x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                   |
| coverage                   | 72.7 ms                                                | 94.5 ms: 1.30x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                            |

Benchmark hidden because not significant (7): mdp, pickle_list, pickle, xml_etree_parse, sqlglot_normalize, scimark_sparse_mat_mult, logging_silent
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240617-3.14.0a0-68df0a5/bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x