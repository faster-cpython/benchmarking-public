# Results vs. 3.12.0

- fork: faster-cpython
- ref: immortal_ref_count_s
- machine: linux-x86_64
- commit hash: 506492e
- commit date: 2024-09-20
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                            |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                          |
| tornado_http   | 103 ms                                                 | 91.1 ms: 1.13x faster                                                           |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 312 ms: 1.51x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 390 ms: 1.48x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 306 ms: 1.47x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 850 ms: 1.36x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 547 ms: 1.33x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 557 ms: 1.30x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 76.2 ms: 1.11x faster                                                           |
| nbody          | 97.0 ms                                                | 87.7 ms: 1.11x faster                                                           |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.16x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.66 ms: 1.01x slower                                                           |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                            |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.06 sec: 1.13x faster                                                          |
| unpickle             | 15.9 us                                                | 14.7 us: 1.08x faster                                                           |
| json_loads           | 28.5 us                                                | 26.6 us: 1.07x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                            |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                                            |
| pickle_dict          | 35.5 us                                                | 33.5 us: 1.06x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 84.4 ms: 1.06x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 58.5 ms: 1.06x faster                                                           |
| pickle               | 11.6 us                                                | 11.2 us: 1.04x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                            |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 106 ms: 1.01x faster                                                            |
| pickle_list          | 5.08 us                                                | 5.13 us: 1.01x slower                                                           |
| unpickle_list        | 5.29 us                                                | 5.40 us: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.98 ms: 1.01x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                           |
| django_template | 34.6 ms                                                | 34.4 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 312 ms: 1.51x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 390 ms: 1.48x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 306 ms: 1.47x faster                                                            |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 850 ms: 1.36x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 30.0 us: 1.36x faster                                                           |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 547 ms: 1.33x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 557 ms: 1.30x faster                                                            |
| unpack_sequence            | 54.0 ns                                                | 42.2 ns: 1.28x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                           |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                           |
| raytrace                   | 312 ms                                                 | 262 ms: 1.19x faster                                                            |
| go                         | 139 ms                                                 | 118 ms: 1.18x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.17x faster                                                           |
| regex_compile              | 148 ms                                                 | 127 ms: 1.16x faster                                                            |
| logging_format             | 7.23 us                                                | 6.23 us: 1.16x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.15x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.15x faster                                                            |
| chaos                      | 67.0 ms                                                | 59.0 ms: 1.13x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.06 sec: 1.13x faster                                                          |
| crypto_pyaes               | 81.9 ms                                                | 72.4 ms: 1.13x faster                                                           |
| tornado_http               | 103 ms                                                 | 91.1 ms: 1.13x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 67.1 ms: 1.12x faster                                                           |
| generators                 | 31.2 ms                                                | 28.0 ms: 1.12x faster                                                           |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.12x faster                                                            |
| float                      | 84.7 ms                                                | 76.2 ms: 1.11x faster                                                           |
| nbody                      | 97.0 ms                                                | 87.7 ms: 1.11x faster                                                           |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                           |
| pprint_safe_repr           | 776 ms                                                 | 707 ms: 1.10x faster                                                            |
| unpickle                   | 15.9 us                                                | 14.7 us: 1.08x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                          |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                            |
| json_loads                 | 28.5 us                                                | 26.6 us: 1.07x faster                                                           |
| async_generators           | 463 ms                                                 | 433 ms: 1.07x faster                                                            |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                            |
| json                       | 5.26 ms                                                | 4.95 ms: 1.06x faster                                                           |
| bench_thread_pool          | 842 us                                                 | 792 us: 1.06x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                                            |
| pickle_dict                | 35.5 us                                                | 33.5 us: 1.06x faster                                                           |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 84.4 ms: 1.06x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 58.5 ms: 1.06x faster                                                           |
| dulwich_log                | 68.5 ms                                                | 65.2 ms: 1.05x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                          |
| fannkuch                   | 417 ms                                                 | 400 ms: 1.04x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.85 ms: 1.04x faster                                                           |
| scimark_fft                | 382 ms                                                 | 368 ms: 1.04x faster                                                            |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                          |
| sympy_expand               | 478 ms                                                 | 460 ms: 1.04x faster                                                            |
| nqueens                    | 83.3 ms                                                | 80.3 ms: 1.04x faster                                                           |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                            |
| pickle                     | 11.6 us                                                | 11.2 us: 1.04x faster                                                           |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                            |
| hexiom                     | 6.41 ms                                                | 6.21 ms: 1.03x faster                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 53.2 ms: 1.03x faster                                                           |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                            |
| asyncio_tcp                | 491 ms                                                 | 481 ms: 1.02x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                            |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                            |
| pyflate                    | 482 ms                                                 | 474 ms: 1.02x faster                                                            |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 106 ms: 1.01x faster                                                            |
| django_template            | 34.6 ms                                                | 34.4 ms: 1.01x faster                                                           |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                            |
| gc_traversal               | 3.79 ms                                                | 3.79 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                          |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.00x slower                                                           |
| python_startup_no_site     | 6.94 ms                                                | 6.98 ms: 1.01x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                            |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                           |
| pickle_list                | 5.08 us                                                | 5.13 us: 1.01x slower                                                           |
| richards_super             | 51.5 ms                                                | 52.0 ms: 1.01x slower                                                           |
| regex_effbot               | 3.61 ms                                                | 3.66 ms: 1.01x slower                                                           |
| unpickle_list              | 5.29 us                                                | 5.40 us: 1.02x slower                                                           |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.73 ms: 1.17x slower                                                           |
| telco                      | 7.10 ms                                                | 8.32 ms: 1.17x slower                                                           |
| coverage                   | 72.7 ms                                                | 87.1 ms: 1.20x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                    |

Benchmark hidden because not significant (5): logging_silent, pycparser, bench_mp_pool, richards, typing_runtime_protocols
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240920-3.14.0a0-506492e/bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.97x