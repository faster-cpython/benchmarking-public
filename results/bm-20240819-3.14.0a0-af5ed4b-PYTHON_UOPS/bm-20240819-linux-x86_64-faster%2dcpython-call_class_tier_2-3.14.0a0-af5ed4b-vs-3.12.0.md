# Results vs. 3.12.0

- fork: faster-cpython
- ref: call_class_tier_2
- machine: linux-x86_64
- commit hash: af5ed4b
- commit date: 2024-08-19
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 322 ms: 1.17x slower                                                         |
| docutils       | 2.77 sec                                               | 3.26 sec: 1.18x slower                                                       |
| tornado_http   | 103 ms                                                 | 99.3 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.10x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 313 ms: 1.43x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 410 ms: 1.40x faster                                                         |
| async_tree_none            | 472 ms                                                 | 349 ms: 1.35x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 890 ms: 1.33x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.31x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 454 ms: 1.27x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 935 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 594 ms: 1.22x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                         |
| nbody          | 97.0 ms                                                | 118 ms: 1.21x slower                                                         |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                         |
| regex_effbot   | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                        |
| regex_v8       | 23.1 ms                                                | 25.8 ms: 1.12x slower                                                        |
| regex_compile  | 148 ms                                                 | 180 ms: 1.21x slower                                                         |
| Geometric mean | (ref)                                                  | 1.10x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.07x faster                                                         |
| json_dumps           | 10.4 ms                                                | 10.8 ms: 1.04x slower                                                        |
| tomli_loads          | 2.33 sec                                               | 2.44 sec: 1.05x slower                                                       |
| xml_etree_generate   | 89.2 ms                                                | 93.7 ms: 1.05x slower                                                        |
| xml_etree_process    | 61.7 ms                                                | 66.1 ms: 1.07x slower                                                        |
| unpickle_pure_python | 230 us                                                 | 249 us: 1.08x slower                                                         |
| pickle_pure_python   | 324 us                                                 | 374 us: 1.15x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.04x slower                                                                 |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                        |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 13.5 ms: 1.13x slower                                                        |
| django_template | 34.6 ms                                                | 40.6 ms: 1.17x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.15x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 313 ms: 1.43x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 410 ms: 1.40x faster                                                         |
| async_tree_none            | 472 ms                                                 | 349 ms: 1.35x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 890 ms: 1.33x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.31x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 454 ms: 1.27x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 935 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 594 ms: 1.22x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                        |
| deepcopy                   | 371 us                                                 | 321 us: 1.15x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.94 us: 1.14x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 36.6 us: 1.11x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.07x faster                                                         |
| tornado_http               | 103 ms                                                 | 99.3 ms: 1.03x faster                                                        |
| gc_traversal               | 3.79 ms                                                | 3.81 ms: 1.00x slower                                                        |
| logging_format             | 7.23 us                                                | 7.28 us: 1.01x slower                                                        |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                         |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                         |
| async_generators           | 463 ms                                                 | 467 ms: 1.01x slower                                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                        |
| asyncio_tcp                | 491 ms                                                 | 501 ms: 1.02x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 863 us: 1.02x slower                                                         |
| coroutines                 | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                        |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 10.8 ms: 1.04x slower                                                        |
| mdp                        | 2.63 sec                                               | 2.75 sec: 1.04x slower                                                       |
| regex_effbot               | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                        |
| comprehensions             | 21.8 us                                                | 22.8 us: 1.05x slower                                                        |
| tomli_loads                | 2.33 sec                                               | 2.44 sec: 1.05x slower                                                       |
| xml_etree_generate         | 89.2 ms                                                | 93.7 ms: 1.05x slower                                                        |
| json                       | 5.26 ms                                                | 5.53 ms: 1.05x slower                                                        |
| crypto_pyaes               | 81.9 ms                                                | 86.7 ms: 1.06x slower                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 80.2 ms: 1.07x slower                                                        |
| xml_etree_process          | 61.7 ms                                                | 66.1 ms: 1.07x slower                                                        |
| meteor_contest             | 112 ms                                                 | 121 ms: 1.08x slower                                                         |
| sympy_sum                  | 169 ms                                                 | 183 ms: 1.08x slower                                                         |
| unpickle_pure_python       | 230 us                                                 | 249 us: 1.08x slower                                                         |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                        |
| raytrace                   | 312 ms                                                 | 344 ms: 1.10x slower                                                         |
| scimark_fft                | 382 ms                                                 | 423 ms: 1.11x slower                                                         |
| sympy_str                  | 300 ms                                                 | 335 ms: 1.12x slower                                                         |
| regex_v8                   | 23.1 ms                                                | 25.8 ms: 1.12x slower                                                        |
| fannkuch                   | 417 ms                                                 | 472 ms: 1.13x slower                                                         |
| mako                       | 11.9 ms                                                | 13.5 ms: 1.13x slower                                                        |
| scimark_lu                 | 118 ms                                                 | 134 ms: 1.14x slower                                                         |
| sympy_integrate            | 21.4 ms                                                | 24.5 ms: 1.14x slower                                                        |
| pprint_safe_repr           | 776 ms                                                 | 890 ms: 1.15x slower                                                         |
| pickle_pure_python         | 324 us                                                 | 374 us: 1.15x slower                                                         |
| scimark_sor                | 129 ms                                                 | 149 ms: 1.15x slower                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.58 ms: 1.16x slower                                                        |
| pyflate                    | 482 ms                                                 | 560 ms: 1.16x slower                                                         |
| coverage                   | 72.7 ms                                                | 84.6 ms: 1.16x slower                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.97 ms: 1.17x slower                                                        |
| django_template            | 34.6 ms                                                | 40.6 ms: 1.17x slower                                                        |
| spectral_norm              | 115 ms                                                 | 135 ms: 1.17x slower                                                         |
| 2to3                       | 274 ms                                                 | 322 ms: 1.17x slower                                                         |
| docutils                   | 2.77 sec                                               | 3.26 sec: 1.18x slower                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.98 ms: 1.18x slower                                                        |
| sympy_expand               | 478 ms                                                 | 566 ms: 1.18x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 187 us: 1.19x slower                                                         |
| logging_silent             | 104 ns                                                 | 124 ns: 1.19x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.88 sec: 1.20x slower                                                       |
| deltablue                  | 3.72 ms                                                | 4.48 ms: 1.20x slower                                                        |
| regex_compile              | 148 ms                                                 | 180 ms: 1.21x slower                                                         |
| sqlglot_normalize          | 110 ms                                                 | 134 ms: 1.21x slower                                                         |
| sqlglot_optimize           | 54.8 ms                                                | 66.5 ms: 1.21x slower                                                        |
| nbody                      | 97.0 ms                                                | 118 ms: 1.21x slower                                                         |
| chaos                      | 67.0 ms                                                | 82.2 ms: 1.23x slower                                                        |
| pycparser                  | 1.18 sec                                               | 1.45 sec: 1.23x slower                                                       |
| telco                      | 7.10 ms                                                | 8.80 ms: 1.24x slower                                                        |
| nqueens                    | 83.3 ms                                                | 104 ms: 1.25x slower                                                         |
| go                         | 139 ms                                                 | 177 ms: 1.27x slower                                                         |
| generators                 | 31.2 ms                                                | 40.8 ms: 1.31x slower                                                        |
| hexiom                     | 6.41 ms                                                | 9.07 ms: 1.41x slower                                                        |
| richards_super             | 51.5 ms                                                | 76.0 ms: 1.48x slower                                                        |
| richards                   | 45.8 ms                                                | 67.7 ms: 1.48x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.07x slower                                                                 |

Benchmark hidden because not significant (5): logging_simple, xml_etree_iterparse, bench_mp_pool, float, json_loads
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240819-3.14.0a0-af5ed4b-PYTHON_UOPS/bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 0.99x