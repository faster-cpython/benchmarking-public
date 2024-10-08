# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_call_ex
- machine: linux-x86_64
- commit hash: ade1f65
- commit date: 2024-08-15
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                                          |
| docutils       | 2.77 sec                                               | 2.72 sec: 1.02x faster                                                        |
| tornado_http   | 103 ms                                                 | 90.1 ms: 1.14x faster                                                         |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.49x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 395 ms: 1.46x faster                                                          |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 425 ms: 1.36x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 537 ms: 1.35x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 897 ms: 1.32x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 570 ms: 1.27x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 908 ms: 1.27x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.9 ms: 1.12x faster                                                         |
| float          | 84.7 ms                                                | 79.8 ms: 1.06x faster                                                         |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.13x faster                                                          |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                                          |
| regex_v8       | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.11x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                          |
| pickle_pure_python   | 324 us                                                 | 306 us: 1.06x faster                                                          |
| xml_etree_process    | 61.7 ms                                                | 59.2 ms: 1.04x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 86.2 ms: 1.03x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.02x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                          |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                                         |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                         |
| python_startup         | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                         |
| django_template | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.49x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 395 ms: 1.46x faster                                                          |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                          |
| deepcopy                   | 371 us                                                 | 267 us: 1.39x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 425 ms: 1.36x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 537 ms: 1.35x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 897 ms: 1.32x faster                                                          |
| deepcopy_memo              | 40.7 us                                                | 30.9 us: 1.32x faster                                                         |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 570 ms: 1.27x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 908 ms: 1.27x faster                                                          |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                         |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                         |
| raytrace                   | 312 ms                                                 | 259 ms: 1.20x faster                                                          |
| logging_format             | 7.23 us                                                | 6.09 us: 1.19x faster                                                         |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                                         |
| chaos                      | 67.0 ms                                                | 58.5 ms: 1.14x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.25 ms: 1.14x faster                                                         |
| tornado_http               | 103 ms                                                 | 90.1 ms: 1.14x faster                                                         |
| regex_compile              | 148 ms                                                 | 131 ms: 1.13x faster                                                          |
| crypto_pyaes               | 81.9 ms                                                | 73.1 ms: 1.12x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                          |
| nbody                      | 97.0 ms                                                | 86.9 ms: 1.12x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.11x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 68.6 ms: 1.10x faster                                                         |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.09x faster                                                          |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                                         |
| bench_thread_pool          | 842 us                                                 | 785 us: 1.07x faster                                                          |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                         |
| float                      | 84.7 ms                                                | 79.8 ms: 1.06x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                          |
| pickle_pure_python         | 324 us                                                 | 306 us: 1.06x faster                                                          |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                         |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                         |
| fannkuch                   | 417 ms                                                 | 396 ms: 1.05x faster                                                          |
| nqueens                    | 83.3 ms                                                | 79.2 ms: 1.05x faster                                                         |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.05x faster                                                          |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                          |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                                          |
| pyflate                    | 482 ms                                                 | 462 ms: 1.05x faster                                                          |
| xml_etree_process          | 61.7 ms                                                | 59.2 ms: 1.04x faster                                                         |
| async_generators           | 463 ms                                                 | 444 ms: 1.04x faster                                                          |
| hexiom                     | 6.41 ms                                                | 6.17 ms: 1.04x faster                                                         |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                                          |
| xml_etree_generate         | 89.2 ms                                                | 86.2 ms: 1.03x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 754 ms: 1.03x faster                                                          |
| sympy_expand               | 478 ms                                                 | 465 ms: 1.03x faster                                                          |
| asyncio_tcp                | 491 ms                                                 | 479 ms: 1.03x faster                                                          |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.02x faster                                                          |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                          |
| scimark_fft                | 382 ms                                                 | 374 ms: 1.02x faster                                                          |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                          |
| sqlglot_optimize           | 54.8 ms                                                | 53.8 ms: 1.02x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.72 sec: 1.02x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                        |
| django_template            | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                         |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.00x faster                                                        |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                                         |
| logging_silent             | 104 ns                                                 | 105 ns: 1.01x slower                                                          |
| gc_traversal               | 3.79 ms                                                | 3.82 ms: 1.01x slower                                                         |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                         |
| richards                   | 45.8 ms                                                | 46.4 ms: 1.01x slower                                                         |
| go                         | 139 ms                                                 | 142 ms: 1.02x slower                                                          |
| asyncio_websockets         | 551 ms                                                 | 561 ms: 1.02x slower                                                          |
| richards_super             | 51.5 ms                                                | 52.8 ms: 1.03x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                          |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                                          |
| python_startup             | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                         |
| regex_v8                   | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                         |
| telco                      | 7.10 ms                                                | 8.16 ms: 1.15x slower                                                         |
| coverage                   | 72.7 ms                                                | 84.7 ms: 1.17x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.18x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                  |

Benchmark hidden because not significant (6): scimark_sor, bench_mp_pool, regex_effbot, scimark_sparse_mat_mult, json, coroutines
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240815-3.14.0a0-ade1f65/bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.98x