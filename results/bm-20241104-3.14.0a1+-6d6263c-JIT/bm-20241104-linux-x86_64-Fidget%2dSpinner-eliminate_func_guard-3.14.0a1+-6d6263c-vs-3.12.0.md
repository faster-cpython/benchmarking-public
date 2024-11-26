# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: eliminate_func_guard
- machine: linux-x86_64
- commit hash: 6d6263c
- commit date: 2024-11-04
- overall geometric mean: 1.057x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 280 ms: 1.02x slower                                                             |
| docutils       | 2.77 sec                                               | 2.95 sec: 1.07x slower                                                           |
| tornado_http   | 103 ms                                                 | 94.9 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 381 ms: 1.51x faster                                                             |
| async_tree_none            | 472 ms                                                 | 331 ms: 1.42x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 321 ms: 1.40x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 419 ms: 1.38x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 863 ms: 1.34x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 555 ms: 1.31x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 983 ms: 1.20x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.35x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.7 ms: 1.17x faster                                                            |
| float          | 84.7 ms                                                | 76.1 ms: 1.11x faster                                                            |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 140 ms: 1.06x faster                                                             |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                             |
| regex_effbot   | 3.61 ms                                                | 3.81 ms: 1.06x slower                                                            |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.10x slower                                                            |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.20x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 79.0 ms: 1.13x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                            |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.08x faster                                                             |
| xml_etree_iterparse  | 107 ms                                                 | 100 ms: 1.06x faster                                                             |
| json_loads           | 28.5 us                                                | 26.8 us: 1.06x faster                                                            |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                             |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.06x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                     |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                            |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                            |
| django_template | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 381 ms: 1.51x faster                                                             |
| async_tree_none            | 472 ms                                                 | 331 ms: 1.42x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 321 ms: 1.40x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 419 ms: 1.38x faster                                                             |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.37x faster                                                            |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 863 ms: 1.34x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 555 ms: 1.31x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                                             |
| comprehensions             | 21.8 us                                                | 17.3 us: 1.26x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 983 ms: 1.20x faster                                                             |
| crypto_pyaes               | 81.9 ms                                                | 68.1 ms: 1.20x faster                                                            |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.20x faster                                                           |
| scimark_fft                | 382 ms                                                 | 320 ms: 1.19x faster                                                             |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                            |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                                            |
| nbody                      | 97.0 ms                                                | 82.7 ms: 1.17x faster                                                            |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 64.8 ms: 1.16x faster                                                            |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.15x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 79.0 ms: 1.13x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.30 ms: 1.13x faster                                                            |
| chaos                      | 67.0 ms                                                | 59.7 ms: 1.12x faster                                                            |
| raytrace                   | 312 ms                                                 | 280 ms: 1.11x faster                                                             |
| float                      | 84.7 ms                                                | 76.1 ms: 1.11x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                            |
| richards                   | 45.8 ms                                                | 41.9 ms: 1.09x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.08x faster                                                             |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                             |
| tornado_http               | 103 ms                                                 | 94.9 ms: 1.08x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 721 ms: 1.08x faster                                                             |
| richards_super             | 51.5 ms                                                | 48.2 ms: 1.07x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 100 ms: 1.06x faster                                                             |
| json_loads                 | 28.5 us                                                | 26.8 us: 1.06x faster                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                           |
| json                       | 5.26 ms                                                | 4.96 ms: 1.06x faster                                                            |
| regex_compile              | 148 ms                                                 | 140 ms: 1.06x faster                                                             |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.6 ms: 1.06x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.78 ms: 1.06x faster                                                            |
| pyflate                    | 482 ms                                                 | 458 ms: 1.05x faster                                                             |
| go                         | 139 ms                                                 | 133 ms: 1.05x faster                                                             |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                             |
| async_generators           | 463 ms                                                 | 448 ms: 1.03x faster                                                             |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                             |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                                             |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                           |
| fannkuch                   | 417 ms                                                 | 404 ms: 1.03x faster                                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.02x faster                                                            |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                           |
| dulwich_log                | 68.5 ms                                                | 67.7 ms: 1.01x faster                                                            |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                            |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                                             |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                             |
| sympy_str                  | 300 ms                                                 | 303 ms: 1.01x slower                                                             |
| 2to3                       | 274 ms                                                 | 280 ms: 1.02x slower                                                             |
| python_startup_no_site     | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                            |
| sqlglot_normalize          | 110 ms                                                 | 115 ms: 1.04x slower                                                             |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                             |
| sympy_sum                  | 169 ms                                                 | 176 ms: 1.04x slower                                                             |
| django_template            | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                            |
| sympy_expand               | 478 ms                                                 | 504 ms: 1.05x slower                                                             |
| nqueens                    | 83.3 ms                                                | 87.9 ms: 1.05x slower                                                            |
| bench_thread_pool          | 842 us                                                 | 888 us: 1.06x slower                                                             |
| regex_effbot               | 3.61 ms                                                | 3.81 ms: 1.06x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                             |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.06x slower                                                            |
| docutils                   | 2.77 sec                                               | 2.95 sec: 1.07x slower                                                           |
| telco                      | 7.10 ms                                                | 7.68 ms: 1.08x slower                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 59.7 ms: 1.09x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.10x slower                                                            |
| sympy_integrate            | 21.4 ms                                                | 23.5 ms: 1.10x slower                                                            |
| hexiom                     | 6.41 ms                                                | 7.06 ms: 1.10x slower                                                            |
| generators                 | 31.2 ms                                                | 35.4 ms: 1.13x slower                                                            |
| coverage                   | 72.7 ms                                                | 84.8 ms: 1.17x slower                                                            |
| gc_traversal               | 3.79 ms                                                | 4.57 ms: 1.20x slower                                                            |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                            |
| create_gc_cycles           | 1.48 ms                                                | 2.67 ms: 1.81x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 84.4 ms: 3.52x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (5): sqlalchemy_declarative, spectral_norm, pickle_pure_python, sqlglot_transpile, coroutines
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241104-3.14.0a1+-6d6263c-JIT/bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.057x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.15x