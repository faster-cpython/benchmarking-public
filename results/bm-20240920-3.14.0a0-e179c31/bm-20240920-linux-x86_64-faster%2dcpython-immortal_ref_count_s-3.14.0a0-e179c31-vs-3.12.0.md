# Results vs. 3.12.0

- fork: faster-cpython
- ref: immortal_ref_count_s
- machine: linux-x86_64
- commit hash: e179c31
- commit date: 2024-09-20
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                                            |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.05x faster                                                          |
| tornado_http   | 103 ms                                                 | 89.8 ms: 1.14x faster                                                           |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 310 ms: 1.52x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 297 ms: 1.51x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 385 ms: 1.49x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 391 ms: 1.48x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 868 ms: 1.36x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 856 ms: 1.35x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 554 ms: 1.31x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 76.6 ms: 1.11x faster                                                           |
| nbody          | 97.0 ms                                                | 89.9 ms: 1.08x faster                                                           |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.16x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                           |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                                            |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                          |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                                            |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                                            |
| json_loads           | 28.5 us                                                | 26.8 us: 1.06x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 84.8 ms: 1.05x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 154 ms: 1.04x faster                                                            |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.02x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                            |
| pickle_dict          | 35.5 us                                                | 35.4 us: 1.00x faster                                                           |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                           |
| pickle_list          | 5.08 us                                                | 5.18 us: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.00 ms: 1.01x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.4 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 310 ms: 1.52x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 297 ms: 1.51x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 385 ms: 1.49x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 391 ms: 1.48x faster                                                            |
| deepcopy                   | 371 us                                                 | 256 us: 1.45x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 868 ms: 1.36x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 856 ms: 1.35x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 30.4 us: 1.34x faster                                                           |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 554 ms: 1.31x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                           |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                           |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                                            |
| logging_format             | 7.23 us                                                | 6.19 us: 1.17x faster                                                           |
| regex_compile              | 148 ms                                                 | 127 ms: 1.16x faster                                                            |
| unpack_sequence            | 54.0 ns                                                | 46.4 ns: 1.16x faster                                                           |
| go                         | 139 ms                                                 | 120 ms: 1.16x faster                                                            |
| logging_simple             | 6.46 us                                                | 5.59 us: 1.16x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.15x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 71.0 ms: 1.15x faster                                                           |
| tornado_http               | 103 ms                                                 | 89.8 ms: 1.14x faster                                                           |
| chaos                      | 67.0 ms                                                | 59.0 ms: 1.14x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                                           |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                            |
| generators                 | 31.2 ms                                                | 27.9 ms: 1.12x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 67.7 ms: 1.11x faster                                                           |
| float                      | 84.7 ms                                                | 76.6 ms: 1.11x faster                                                           |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                           |
| pprint_safe_repr           | 776 ms                                                 | 710 ms: 1.09x faster                                                            |
| json                       | 5.26 ms                                                | 4.86 ms: 1.08x faster                                                           |
| nbody                      | 97.0 ms                                                | 89.9 ms: 1.08x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.08x faster                                                          |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                                            |
| async_generators           | 463 ms                                                 | 432 ms: 1.07x faster                                                            |
| gc_traversal               | 3.79 ms                                                | 3.55 ms: 1.07x faster                                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 64.3 ms: 1.06x faster                                                           |
| bench_thread_pool          | 842 us                                                 | 791 us: 1.06x faster                                                            |
| json_loads                 | 28.5 us                                                | 26.8 us: 1.06x faster                                                           |
| nqueens                    | 83.3 ms                                                | 78.9 ms: 1.06x faster                                                           |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 84.8 ms: 1.05x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                           |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.05x faster                                                            |
| asyncio_tcp                | 491 ms                                                 | 468 ms: 1.05x faster                                                            |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                                            |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.05x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.05x faster                                                          |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                            |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                            |
| scimark_fft                | 382 ms                                                 | 367 ms: 1.04x faster                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 52.9 ms: 1.04x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 154 ms: 1.04x faster                                                            |
| hexiom                     | 6.41 ms                                                | 6.20 ms: 1.03x faster                                                           |
| fannkuch                   | 417 ms                                                 | 404 ms: 1.03x faster                                                            |
| pyflate                    | 482 ms                                                 | 468 ms: 1.03x faster                                                            |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.02x faster                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.96 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                            |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                            |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                          |
| logging_silent             | 104 ns                                                 | 104 ns: 1.01x faster                                                            |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                            |
| pickle_dict                | 35.5 us                                                | 35.4 us: 1.00x faster                                                           |
| sqlite_synth               | 2.83 us                                                | 2.85 us: 1.01x slower                                                           |
| python_startup_no_site     | 6.94 ms                                                | 7.00 ms: 1.01x slower                                                           |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                            |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                           |
| richards                   | 45.8 ms                                                | 46.5 ms: 1.01x slower                                                           |
| richards_super             | 51.5 ms                                                | 52.3 ms: 1.02x slower                                                           |
| pickle_list                | 5.08 us                                                | 5.18 us: 1.02x slower                                                           |
| regex_effbot               | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                           |
| mdp                        | 2.63 sec                                               | 2.69 sec: 1.02x slower                                                          |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.73 ms: 1.17x slower                                                           |
| coverage                   | 72.7 ms                                                | 86.8 ms: 1.19x slower                                                           |
| telco                      | 7.10 ms                                                | 8.51 ms: 1.20x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (6): typing_runtime_protocols, unpickle_list, django_template, bench_mp_pool, asyncio_tcp_ssl, unpickle
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240920-3.14.0a0-e179c31/bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.97x