# Results vs. 3.12.0

- fork: faster-cpython
- ref: split_load_const
- machine: linux-x86_64
- commit hash: f934559
- commit date: 2024-10-25
- overall geometric mean: 1.070x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                                         |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                       |
| tornado_http   | 103 ms                                                 | 91.1 ms: 1.13x faster                                                        |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 384 ms: 1.50x faster                                                         |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 413 ms: 1.40x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 838 ms: 1.38x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 559 ms: 1.30x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 981 ms: 1.21x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 79.4 ms: 1.07x faster                                                        |
| nbody          | 97.0 ms                                                | 94.4 ms: 1.03x faster                                                        |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                        |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                         |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.13 sec: 1.09x faster                                                       |
| json_loads           | 28.5 us                                                | 26.2 us: 1.09x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 313 us: 1.04x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                         |
| xml_etree_parse      | 159 ms                                                 | 157 ms: 1.01x faster                                                         |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                        |
| python_startup         | 9.55 ms                                                | 11.8 ms: 1.23x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 384 ms: 1.50x faster                                                         |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                         |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 413 ms: 1.40x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 838 ms: 1.38x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 30.6 us: 1.33x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 559 ms: 1.30x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 981 ms: 1.21x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                        |
| logging_format             | 7.23 us                                                | 6.23 us: 1.16x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.58 us: 1.16x faster                                                        |
| go                         | 139 ms                                                 | 121 ms: 1.16x faster                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 127 ms: 1.15x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                         |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                         |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.29 ms: 1.13x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 72.5 ms: 1.13x faster                                                        |
| tornado_http               | 103 ms                                                 | 91.1 ms: 1.13x faster                                                        |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                         |
| generators                 | 31.2 ms                                                | 28.0 ms: 1.11x faster                                                        |
| chaos                      | 67.0 ms                                                | 60.9 ms: 1.10x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 2.13 sec: 1.09x faster                                                       |
| json_loads                 | 28.5 us                                                | 26.2 us: 1.09x faster                                                        |
| json                       | 5.26 ms                                                | 4.84 ms: 1.09x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                                        |
| async_generators           | 463 ms                                                 | 428 ms: 1.08x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 63.6 ms: 1.08x faster                                                        |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 70.3 ms: 1.07x faster                                                        |
| float                      | 84.7 ms                                                | 79.4 ms: 1.07x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 730 ms: 1.06x faster                                                         |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.05x faster                                                        |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                       |
| scimark_fft                | 382 ms                                                 | 365 ms: 1.05x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                        |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.85 ms: 1.04x faster                                                        |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                         |
| pyflate                    | 482 ms                                                 | 465 ms: 1.04x faster                                                         |
| pickle_pure_python         | 324 us                                                 | 313 us: 1.04x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                        |
| nqueens                    | 83.3 ms                                                | 80.5 ms: 1.04x faster                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 53.2 ms: 1.03x faster                                                        |
| fannkuch                   | 417 ms                                                 | 405 ms: 1.03x faster                                                         |
| nbody                      | 97.0 ms                                                | 94.4 ms: 1.03x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                         |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                         |
| hexiom                     | 6.41 ms                                                | 6.29 ms: 1.02x faster                                                        |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                        |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.02x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 157 ms: 1.01x faster                                                         |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                         |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                         |
| richards_super             | 51.5 ms                                                | 52.3 ms: 1.01x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                        |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                                         |
| regex_effbot               | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                        |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                         |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.03x slower                                                         |
| coroutines                 | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.08x slower                                                        |
| telco                      | 7.10 ms                                                | 7.94 ms: 1.12x slower                                                        |
| coverage                   | 72.7 ms                                                | 84.7 ms: 1.16x slower                                                        |
| python_startup             | 9.55 ms                                                | 11.8 ms: 1.23x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.71 ms: 1.24x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.68 ms: 1.81x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 78.1 ms: 3.25x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (5): bench_thread_pool, richards, django_template, typing_runtime_protocols, pycparser
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241025-3.14.0a1+-f934559/bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.070x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.08x