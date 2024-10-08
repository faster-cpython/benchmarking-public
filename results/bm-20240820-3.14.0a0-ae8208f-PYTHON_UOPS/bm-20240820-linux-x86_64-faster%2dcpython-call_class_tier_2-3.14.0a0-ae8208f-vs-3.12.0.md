# Results vs. 3.12.0

- fork: faster-cpython
- ref: call_class_tier_2
- machine: linux-x86_64
- commit hash: ae8208f
- commit date: 2024-08-20
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 327 ms: 1.19x slower                                                         |
| docutils       | 2.77 sec                                               | 3.26 sec: 1.18x slower                                                       |
| tornado_http   | 103 ms                                                 | 98.6 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                  | 1.11x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 319 ms: 1.41x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 411 ms: 1.40x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                         |
| async_tree_none            | 472 ms                                                 | 351 ms: 1.34x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.31x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 456 ms: 1.27x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 931 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 595 ms: 1.22x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 84.3 ms: 1.00x faster                                                        |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                         |
| nbody          | 97.0 ms                                                | 120 ms: 1.23x slower                                                         |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                        |
| regex_dna      | 212 ms                                                 | 226 ms: 1.07x slower                                                         |
| regex_v8       | 23.1 ms                                                | 26.6 ms: 1.15x slower                                                        |
| regex_compile  | 148 ms                                                 | 183 ms: 1.23x slower                                                         |
| Geometric mean | (ref)                                                  | 1.11x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.07x faster                                                         |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 108 ms: 1.01x slower                                                         |
| xml_etree_generate   | 89.2 ms                                                | 94.2 ms: 1.06x slower                                                        |
| xml_etree_process    | 61.7 ms                                                | 66.5 ms: 1.08x slower                                                        |
| tomli_loads          | 2.33 sec                                               | 2.54 sec: 1.09x slower                                                       |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                        |
| unpickle_pure_python | 230 us                                                 | 253 us: 1.10x slower                                                         |
| pickle_pure_python   | 324 us                                                 | 384 us: 1.19x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                        |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 13.6 ms: 1.14x slower                                                        |
| django_template | 34.6 ms                                                | 40.9 ms: 1.18x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.16x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 319 ms: 1.41x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 411 ms: 1.40x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                         |
| async_tree_none            | 472 ms                                                 | 351 ms: 1.34x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.31x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 456 ms: 1.27x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 931 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 595 ms: 1.22x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                                        |
| deepcopy                   | 371 us                                                 | 323 us: 1.15x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 3.02 us: 1.11x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.07x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 38.8 us: 1.05x faster                                                        |
| tornado_http               | 103 ms                                                 | 98.6 ms: 1.04x faster                                                        |
| gc_traversal               | 3.79 ms                                                | 3.73 ms: 1.02x faster                                                        |
| float                      | 84.7 ms                                                | 84.3 ms: 1.00x faster                                                        |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                                        |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                         |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                         |
| async_generators           | 463 ms                                                 | 467 ms: 1.01x slower                                                         |
| regex_effbot               | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 108 ms: 1.01x slower                                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                       |
| asyncio_tcp                | 491 ms                                                 | 500 ms: 1.02x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                        |
| logging_simple             | 6.46 us                                                | 6.63 us: 1.03x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 866 us: 1.03x slower                                                         |
| coroutines                 | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                        |
| logging_format             | 7.23 us                                                | 7.48 us: 1.03x slower                                                        |
| xml_etree_generate         | 89.2 ms                                                | 94.2 ms: 1.06x slower                                                        |
| json                       | 5.26 ms                                                | 5.59 ms: 1.06x slower                                                        |
| crypto_pyaes               | 81.9 ms                                                | 87.0 ms: 1.06x slower                                                        |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.07x slower                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 80.8 ms: 1.08x slower                                                        |
| xml_etree_process          | 61.7 ms                                                | 66.5 ms: 1.08x slower                                                        |
| sympy_sum                  | 169 ms                                                 | 183 ms: 1.08x slower                                                         |
| meteor_contest             | 112 ms                                                 | 122 ms: 1.08x slower                                                         |
| tomli_loads                | 2.33 sec                                               | 2.54 sec: 1.09x slower                                                       |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                        |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                        |
| mdp                        | 2.63 sec                                               | 2.89 sec: 1.10x slower                                                       |
| unpickle_pure_python       | 230 us                                                 | 253 us: 1.10x slower                                                         |
| comprehensions             | 21.8 us                                                | 24.2 us: 1.11x slower                                                        |
| raytrace                   | 312 ms                                                 | 349 ms: 1.12x slower                                                         |
| sympy_str                  | 300 ms                                                 | 338 ms: 1.13x slower                                                         |
| scimark_fft                | 382 ms                                                 | 433 ms: 1.13x slower                                                         |
| scimark_lu                 | 118 ms                                                 | 134 ms: 1.13x slower                                                         |
| mako                       | 11.9 ms                                                | 13.6 ms: 1.14x slower                                                        |
| fannkuch                   | 417 ms                                                 | 478 ms: 1.14x slower                                                         |
| sympy_integrate            | 21.4 ms                                                | 24.5 ms: 1.15x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 26.6 ms: 1.15x slower                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.82 ms: 1.15x slower                                                        |
| pyflate                    | 482 ms                                                 | 558 ms: 1.16x slower                                                         |
| coverage                   | 72.7 ms                                                | 84.9 ms: 1.17x slower                                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.60 ms: 1.17x slower                                                        |
| pprint_safe_repr           | 776 ms                                                 | 911 ms: 1.17x slower                                                         |
| sympy_expand               | 478 ms                                                 | 563 ms: 1.18x slower                                                         |
| docutils                   | 2.77 sec                                               | 3.26 sec: 1.18x slower                                                       |
| django_template            | 34.6 ms                                                | 40.9 ms: 1.18x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 187 us: 1.18x slower                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 2.00 ms: 1.18x slower                                                        |
| pickle_pure_python         | 324 us                                                 | 384 us: 1.19x slower                                                         |
| 2to3                       | 274 ms                                                 | 327 ms: 1.19x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.21x slower                                                        |
| spectral_norm              | 115 ms                                                 | 139 ms: 1.21x slower                                                         |
| scimark_sor                | 129 ms                                                 | 157 ms: 1.22x slower                                                         |
| sqlglot_optimize           | 54.8 ms                                                | 67.0 ms: 1.22x slower                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.93 sec: 1.23x slower                                                       |
| regex_compile              | 148 ms                                                 | 183 ms: 1.23x slower                                                         |
| sqlglot_normalize          | 110 ms                                                 | 136 ms: 1.23x slower                                                         |
| telco                      | 7.10 ms                                                | 8.76 ms: 1.23x slower                                                        |
| nbody                      | 97.0 ms                                                | 120 ms: 1.23x slower                                                         |
| nqueens                    | 83.3 ms                                                | 104 ms: 1.24x slower                                                         |
| chaos                      | 67.0 ms                                                | 83.4 ms: 1.25x slower                                                        |
| pycparser                  | 1.18 sec                                               | 1.47 sec: 1.25x slower                                                       |
| go                         | 139 ms                                                 | 175 ms: 1.26x slower                                                         |
| deltablue                  | 3.72 ms                                                | 4.70 ms: 1.26x slower                                                        |
| logging_silent             | 104 ns                                                 | 132 ns: 1.27x slower                                                         |
| generators                 | 31.2 ms                                                | 40.2 ms: 1.29x slower                                                        |
| hexiom                     | 6.41 ms                                                | 9.54 ms: 1.49x slower                                                        |
| richards_super             | 51.5 ms                                                | 80.7 ms: 1.57x slower                                                        |
| richards                   | 45.8 ms                                                | 72.0 ms: 1.57x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.08x slower                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240820-3.14.0a0-ae8208f-PYTHON_UOPS/bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 0.99x