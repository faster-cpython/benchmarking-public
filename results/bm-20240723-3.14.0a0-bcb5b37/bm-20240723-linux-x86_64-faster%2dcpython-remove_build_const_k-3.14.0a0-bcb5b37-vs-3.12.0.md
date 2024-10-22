# Results vs. 3.12.0

- fork: faster-cpython
- ref: remove_build_const_k
- machine: linux-x86_64
- commit hash: bcb5b37
- commit date: 2024-07-23
- overall geometric mean: 1.10x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                                            |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                          |
| tornado_http   | 103 ms                                                 | 89.7 ms: 1.14x faster                                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 291 ms: 1.55x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 373 ms: 1.54x faster                                                            |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 406 ms: 1.42x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 843 ms: 1.40x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 835 ms: 1.38x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 541 ms: 1.34x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.42x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.5 ms: 1.12x faster                                                           |
| float          | 84.7 ms                                                | 77.3 ms: 1.10x faster                                                           |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                           |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                                            |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.02 sec: 1.15x faster                                                          |
| unpickle_pure_python | 230 us                                                 | 209 us: 1.10x faster                                                            |
| pickle_pure_python   | 324 us                                                 | 296 us: 1.10x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 58.1 ms: 1.06x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 84.5 ms: 1.06x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 153 ms: 1.04x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.03x faster                                                            |
| json_loads           | 28.5 us                                                | 28.1 us: 1.02x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                    |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.8 ms: 1.11x faster                                                           |
| django_template | 34.6 ms                                                | 33.6 ms: 1.03x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 291 ms: 1.55x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 373 ms: 1.54x faster                                                            |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                            |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 406 ms: 1.42x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 843 ms: 1.40x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.40x faster                                                           |
| async_tree_io              | 1.16 sec                                               | 835 ms: 1.38x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 541 ms: 1.34x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                                           |
| pathlib                    | 19.3 ms                                                | 15.6 ms: 1.24x faster                                                           |
| raytrace                   | 312 ms                                                 | 253 ms: 1.24x faster                                                            |
| logging_format             | 7.23 us                                                | 6.03 us: 1.20x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.40 us: 1.20x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.16 ms: 1.18x faster                                                           |
| chaos                      | 67.0 ms                                                | 57.6 ms: 1.16x faster                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.35 ms: 1.16x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 70.5 ms: 1.16x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.02 sec: 1.15x faster                                                          |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                            |
| tornado_http               | 103 ms                                                 | 89.7 ms: 1.14x faster                                                           |
| generators                 | 31.2 ms                                                | 27.7 ms: 1.13x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 66.6 ms: 1.13x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                            |
| nbody                      | 97.0 ms                                                | 86.5 ms: 1.12x faster                                                           |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.11x faster                                                           |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.11x faster                                                            |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 209 us: 1.10x faster                                                            |
| float                      | 84.7 ms                                                | 77.3 ms: 1.10x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 296 us: 1.10x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.25 ms: 1.08x faster                                                           |
| async_generators           | 463 ms                                                 | 427 ms: 1.08x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 63.4 ms: 1.08x faster                                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.56 ms: 1.08x faster                                                           |
| pprint_safe_repr           | 776 ms                                                 | 722 ms: 1.07x faster                                                            |
| scimark_fft                | 382 ms                                                 | 356 ms: 1.07x faster                                                            |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.07x faster                                                            |
| bench_thread_pool          | 842 us                                                 | 785 us: 1.07x faster                                                            |
| gc_traversal               | 3.79 ms                                                | 3.54 ms: 1.07x faster                                                           |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                            |
| logging_silent             | 104 ns                                                 | 98.1 ns: 1.06x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 58.1 ms: 1.06x faster                                                           |
| hexiom                     | 6.41 ms                                                | 6.06 ms: 1.06x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                          |
| fannkuch                   | 417 ms                                                 | 395 ms: 1.06x faster                                                            |
| dask                       | 372 ms                                                 | 352 ms: 1.06x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 84.5 ms: 1.06x faster                                                           |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                                            |
| sqlglot_normalize          | 110 ms                                                 | 105 ms: 1.05x faster                                                            |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                            |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                            |
| coroutines                 | 23.2 ms                                                | 22.2 ms: 1.04x faster                                                           |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                          |
| xml_etree_parse            | 159 ms                                                 | 153 ms: 1.04x faster                                                            |
| json                       | 5.26 ms                                                | 5.06 ms: 1.04x faster                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 52.8 ms: 1.04x faster                                                           |
| nqueens                    | 83.3 ms                                                | 80.5 ms: 1.03x faster                                                           |
| django_template            | 34.6 ms                                                | 33.6 ms: 1.03x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.03x faster                                                            |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                          |
| json_loads                 | 28.5 us                                                | 28.1 us: 1.02x faster                                                           |
| asyncio_tcp                | 491 ms                                                 | 490 ms: 1.00x faster                                                            |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                            |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                           |
| regex_effbot               | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                            |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| telco                      | 7.10 ms                                                | 8.15 ms: 1.15x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.73 ms: 1.17x slower                                                           |
| coverage                   | 72.7 ms                                                | 90.9 ms: 1.25x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                                    |

Benchmark hidden because not significant (8): richards, pycparser, go, pyflate, bench_mp_pool, asyncio_tcp_ssl, json_dumps, richards_super
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240723-3.14.0a0-bcb5b37/bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.98x