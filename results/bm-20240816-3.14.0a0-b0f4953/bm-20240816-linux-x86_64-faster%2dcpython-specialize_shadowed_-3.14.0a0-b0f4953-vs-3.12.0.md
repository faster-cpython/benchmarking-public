# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_shadowed_
- machine: linux-x86_64
- commit hash: b0f4953
- commit date: 2024-08-16
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                            |
| docutils       | 2.77 sec                                               | 2.71 sec: 1.02x faster                                                          |
| tornado_http   | 103 ms                                                 | 90.3 ms: 1.14x faster                                                           |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.50x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                            |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 527 ms: 1.38x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 422 ms: 1.37x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 886 ms: 1.33x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 897 ms: 1.29x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 88.1 ms: 1.10x faster                                                           |
| float          | 84.7 ms                                                | 78.9 ms: 1.07x faster                                                           |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                           |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                                            |
| regex_v8       | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                          |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                            |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 85.7 ms: 1.04x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                           |
| django_template | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.50x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                            |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                            |
| deepcopy                   | 371 us                                                 | 260 us: 1.42x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 527 ms: 1.38x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 422 ms: 1.37x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 30.1 us: 1.35x faster                                                           |
| async_tree_io_tg           | 1.18 sec                                               | 886 ms: 1.33x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 897 ms: 1.29x faster                                                            |
| pathlib                    | 19.3 ms                                                | 15.6 ms: 1.24x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                           |
| raytrace                   | 312 ms                                                 | 260 ms: 1.20x faster                                                            |
| logging_format             | 7.23 us                                                | 6.18 us: 1.17x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.55 us: 1.16x faster                                                           |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.15x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 71.5 ms: 1.15x faster                                                           |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                                           |
| tornado_http               | 103 ms                                                 | 90.3 ms: 1.14x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                            |
| generators                 | 31.2 ms                                                | 28.0 ms: 1.11x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                          |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.11x faster                                                            |
| nbody                      | 97.0 ms                                                | 88.1 ms: 1.10x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 68.3 ms: 1.10x faster                                                           |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                                           |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                            |
| bench_thread_pool          | 842 us                                                 | 784 us: 1.07x faster                                                            |
| float                      | 84.7 ms                                                | 78.9 ms: 1.07x faster                                                           |
| pprint_safe_repr           | 776 ms                                                 | 724 ms: 1.07x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.72 ms: 1.07x faster                                                           |
| async_generators           | 463 ms                                                 | 434 ms: 1.07x faster                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                           |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                            |
| scimark_fft                | 382 ms                                                 | 361 ms: 1.06x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.05x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                          |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                           |
| nqueens                    | 83.3 ms                                                | 79.5 ms: 1.05x faster                                                           |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                            |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                          |
| xml_etree_generate         | 89.2 ms                                                | 85.7 ms: 1.04x faster                                                           |
| fannkuch                   | 417 ms                                                 | 404 ms: 1.03x faster                                                            |
| hexiom                     | 6.41 ms                                                | 6.24 ms: 1.03x faster                                                           |
| pyflate                    | 482 ms                                                 | 469 ms: 1.03x faster                                                            |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                                            |
| gc_traversal               | 3.79 ms                                                | 3.71 ms: 1.02x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.71 sec: 1.02x faster                                                          |
| sqlglot_optimize           | 54.8 ms                                                | 53.6 ms: 1.02x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                            |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                            |
| asyncio_tcp                | 491 ms                                                 | 481 ms: 1.02x faster                                                            |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.02x faster                                                            |
| django_template            | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                           |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                          |
| typing_runtime_protocols   | 158 us                                                 | 159 us: 1.01x slower                                                            |
| logging_silent             | 104 ns                                                 | 105 ns: 1.01x slower                                                            |
| json                       | 5.26 ms                                                | 5.31 ms: 1.01x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                            |
| richards                   | 45.8 ms                                                | 46.5 ms: 1.02x slower                                                           |
| go                         | 139 ms                                                 | 142 ms: 1.02x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                           |
| regex_effbot               | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                           |
| richards_super             | 51.5 ms                                                | 52.8 ms: 1.02x slower                                                           |
| mdp                        | 2.63 sec                                               | 2.72 sec: 1.03x slower                                                          |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| coverage                   | 72.7 ms                                                | 84.4 ms: 1.16x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.73 ms: 1.17x slower                                                           |
| telco                      | 7.10 ms                                                | 8.33 ms: 1.17x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (5): coroutines, scimark_sor, json_loads, bench_mp_pool, json_dumps
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240816-3.14.0a0-b0f4953/bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.98x