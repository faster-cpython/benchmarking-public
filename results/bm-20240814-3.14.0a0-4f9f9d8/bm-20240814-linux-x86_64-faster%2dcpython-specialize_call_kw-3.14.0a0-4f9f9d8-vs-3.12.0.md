# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_call_kw
- machine: linux-x86_64
- commit hash: 4f9f9d8
- commit date: 2024-08-14
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                                          |
| docutils       | 2.77 sec                                               | 2.73 sec: 1.01x faster                                                        |
| tornado_http   | 103 ms                                                 | 90.4 ms: 1.14x faster                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.51x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 392 ms: 1.47x faster                                                          |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 413 ms: 1.40x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 533 ms: 1.36x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 889 ms: 1.33x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 898 ms: 1.29x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.28x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.8 ms: 1.12x faster                                                         |
| float          | 84.7 ms                                                | 78.3 ms: 1.08x faster                                                         |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                          |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                                          |
| regex_effbot   | 3.61 ms                                                | 3.80 ms: 1.05x slower                                                         |
| regex_v8       | 23.1 ms                                                | 26.2 ms: 1.13x slower                                                         |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.05 sec: 1.13x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 212 us: 1.08x faster                                                          |
| pickle_pure_python   | 324 us                                                 | 301 us: 1.08x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 155 ms: 1.03x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 86.8 ms: 1.03x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                          |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                  |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                         |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.09x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                         |
| django_template | 34.6 ms                                                | 33.7 ms: 1.03x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.51x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 392 ms: 1.47x faster                                                          |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                          |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 413 ms: 1.40x faster                                                          |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 533 ms: 1.36x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 889 ms: 1.33x faster                                                          |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 898 ms: 1.29x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.28x faster                                                          |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                         |
| pathlib                    | 19.3 ms                                                | 15.7 ms: 1.23x faster                                                         |
| raytrace                   | 312 ms                                                 | 254 ms: 1.23x faster                                                          |
| logging_format             | 7.23 us                                                | 6.05 us: 1.20x faster                                                         |
| logging_simple             | 6.46 us                                                | 5.42 us: 1.19x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.14 ms: 1.18x faster                                                         |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                          |
| chaos                      | 67.0 ms                                                | 58.7 ms: 1.14x faster                                                         |
| tornado_http               | 103 ms                                                 | 90.4 ms: 1.14x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 2.05 sec: 1.13x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.12x faster                                                          |
| crypto_pyaes               | 81.9 ms                                                | 73.1 ms: 1.12x faster                                                         |
| nbody                      | 97.0 ms                                                | 86.8 ms: 1.12x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 67.5 ms: 1.11x faster                                                         |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                          |
| generators                 | 31.2 ms                                                | 28.5 ms: 1.10x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 212 us: 1.08x faster                                                          |
| float                      | 84.7 ms                                                | 78.3 ms: 1.08x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                                         |
| logging_silent             | 104 ns                                                 | 97.0 ns: 1.08x faster                                                         |
| pickle_pure_python         | 324 us                                                 | 301 us: 1.08x faster                                                          |
| bench_thread_pool          | 842 us                                                 | 785 us: 1.07x faster                                                          |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.74 ms: 1.07x faster                                                         |
| async_generators           | 463 ms                                                 | 434 ms: 1.07x faster                                                          |
| hexiom                     | 6.41 ms                                                | 6.02 ms: 1.07x faster                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                         |
| nqueens                    | 83.3 ms                                                | 78.6 ms: 1.06x faster                                                         |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                         |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                                          |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                                          |
| scimark_fft                | 382 ms                                                 | 364 ms: 1.05x faster                                                          |
| fannkuch                   | 417 ms                                                 | 398 ms: 1.05x faster                                                          |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                          |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.05x faster                                                          |
| pprint_safe_repr           | 776 ms                                                 | 742 ms: 1.04x faster                                                          |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                        |
| sympy_expand               | 478 ms                                                 | 461 ms: 1.04x faster                                                          |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 155 ms: 1.03x faster                                                          |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.03x faster                                                          |
| xml_etree_generate         | 89.2 ms                                                | 86.8 ms: 1.03x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                         |
| django_template            | 34.6 ms                                                | 33.7 ms: 1.03x faster                                                         |
| pyflate                    | 482 ms                                                 | 470 ms: 1.03x faster                                                          |
| asyncio_tcp                | 491 ms                                                 | 478 ms: 1.03x faster                                                          |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                          |
| sqlglot_optimize           | 54.8 ms                                                | 53.6 ms: 1.02x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                          |
| docutils                   | 2.77 sec                                               | 2.73 sec: 1.01x faster                                                        |
| gc_traversal               | 3.79 ms                                                | 3.75 ms: 1.01x faster                                                         |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                          |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                                          |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                          |
| python_startup_no_site     | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                          |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                                          |
| regex_effbot               | 3.61 ms                                                | 3.80 ms: 1.05x slower                                                         |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.09x slower                                                         |
| regex_v8                   | 23.1 ms                                                | 26.2 ms: 1.13x slower                                                         |
| telco                      | 7.10 ms                                                | 8.16 ms: 1.15x slower                                                         |
| coverage                   | 72.7 ms                                                | 83.8 ms: 1.15x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                  |

Benchmark hidden because not significant (7): json, json_loads, json_dumps, bench_mp_pool, richards, pycparser, richards_super
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240814-3.14.0a0-4f9f9d8/bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x