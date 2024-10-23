# Results vs. 3.12.0

- fork: faster-cpython
- ref: load_const_return_re
- machine: linux-x86_64
- commit hash: 2a3b1e2
- commit date: 2024-10-23
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                             |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                           |
| tornado_http   | 103 ms                                                 | 91.4 ms: 1.12x faster                                                            |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 386 ms: 1.49x faster                                                             |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 322 ms: 1.40x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.39x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 855 ms: 1.35x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 556 ms: 1.31x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 977 ms: 1.21x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 80.3 ms: 1.05x faster                                                            |
| nbody          | 97.0 ms                                                | 95.8 ms: 1.01x faster                                                            |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.13x faster                                                             |
| regex_dna      | 212 ms                                                 | 214 ms: 1.01x slower                                                             |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.12 sec: 1.10x faster                                                           |
| json_loads           | 28.5 us                                                | 26.2 us: 1.09x faster                                                            |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                             |
| pickle_pure_python   | 324 us                                                 | 315 us: 1.03x faster                                                             |
| xml_etree_process    | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 87.1 ms: 1.02x faster                                                            |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                             |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.06x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                            |
| python_startup         | 9.55 ms                                                | 11.8 ms: 1.24x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.4 ms: 1.05x faster                                                            |
| django_template | 34.6 ms                                                | 34.8 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 386 ms: 1.49x faster                                                             |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                             |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 322 ms: 1.40x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.39x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 855 ms: 1.35x faster                                                             |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 31.1 us: 1.31x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 556 ms: 1.31x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                            |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 977 ms: 1.21x faster                                                             |
| logging_format             | 7.23 us                                                | 6.18 us: 1.17x faster                                                            |
| go                         | 139 ms                                                 | 120 ms: 1.16x faster                                                             |
| generators                 | 31.2 ms                                                | 26.8 ms: 1.16x faster                                                            |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                                             |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                             |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.15x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 71.8 ms: 1.14x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.26 ms: 1.14x faster                                                            |
| regex_compile              | 148 ms                                                 | 131 ms: 1.13x faster                                                             |
| tornado_http               | 103 ms                                                 | 91.4 ms: 1.12x faster                                                            |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                             |
| tomli_loads                | 2.33 sec                                               | 2.12 sec: 1.10x faster                                                           |
| json_loads                 | 28.5 us                                                | 26.2 us: 1.09x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 69.1 ms: 1.09x faster                                                            |
| async_generators           | 463 ms                                                 | 427 ms: 1.08x faster                                                             |
| json                       | 5.26 ms                                                | 4.85 ms: 1.08x faster                                                            |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                             |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.07x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 64.0 ms: 1.07x faster                                                            |
| chaos                      | 67.0 ms                                                | 62.6 ms: 1.07x faster                                                            |
| logging_silent             | 104 ns                                                 | 98.3 ns: 1.06x faster                                                            |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                             |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                             |
| float                      | 84.7 ms                                                | 80.3 ms: 1.05x faster                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                            |
| pyflate                    | 482 ms                                                 | 459 ms: 1.05x faster                                                             |
| mdp                        | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                           |
| pprint_safe_repr           | 776 ms                                                 | 738 ms: 1.05x faster                                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                            |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                                             |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.05x faster                                                            |
| scimark_fft                | 382 ms                                                 | 365 ms: 1.05x faster                                                             |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                           |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                             |
| nqueens                    | 83.3 ms                                                | 80.6 ms: 1.03x faster                                                            |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                           |
| fannkuch                   | 417 ms                                                 | 405 ms: 1.03x faster                                                             |
| sqlglot_optimize           | 54.8 ms                                                | 53.3 ms: 1.03x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 315 us: 1.03x faster                                                             |
| xml_etree_process          | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 87.1 ms: 1.02x faster                                                            |
| hexiom                     | 6.41 ms                                                | 6.28 ms: 1.02x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                             |
| nbody                      | 97.0 ms                                                | 95.8 ms: 1.01x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.01 ms: 1.01x faster                                                            |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                             |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                             |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                                             |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                             |
| django_template            | 34.6 ms                                                | 34.8 ms: 1.01x slower                                                            |
| richards                   | 45.8 ms                                                | 46.1 ms: 1.01x slower                                                            |
| regex_dna                  | 212 ms                                                 | 214 ms: 1.01x slower                                                             |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                            |
| scimark_sor                | 129 ms                                                 | 132 ms: 1.02x slower                                                             |
| richards_super             | 51.5 ms                                                | 52.7 ms: 1.02x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                             |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.06x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.09x slower                                                            |
| telco                      | 7.10 ms                                                | 8.02 ms: 1.13x slower                                                            |
| coverage                   | 72.7 ms                                                | 84.4 ms: 1.16x slower                                                            |
| gc_traversal               | 3.79 ms                                                | 4.47 ms: 1.18x slower                                                            |
| python_startup             | 9.55 ms                                                | 11.8 ms: 1.24x slower                                                            |
| create_gc_cycles           | 1.48 ms                                                | 2.67 ms: 1.81x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 78.7 ms: 3.28x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                                     |

Benchmark hidden because not significant (4): xml_etree_iterparse, regex_effbot, bench_thread_pool, coroutines
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241023-3.14.0a1+-2a3b1e2/bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.09x