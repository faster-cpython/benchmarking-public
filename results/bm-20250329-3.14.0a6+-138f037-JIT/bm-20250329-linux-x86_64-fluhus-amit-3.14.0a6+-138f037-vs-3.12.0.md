# Results vs. 3.12.0

- fork: fluhus
- ref: amit
- machine: linux-x86_64
- commit hash: 138f037
- commit date: 2025-03-29
- overall geometric mean: 1.130x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                   |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                   |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.89x faster                                   |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                   |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                   |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                   |
| Geometric mean             | (ref)                                                  | 1.76x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 84.7 ms                                                | 63.0 ms: 1.34x faster                                  |
| nbody          | 97.0 ms                                                | 84.9 ms: 1.14x faster                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.16x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                   |
| regex_effbot   | 3.61 ms                                                | 3.47 ms: 1.04x faster                                  |
| regex_v8       | 23.1 ms                                                | 23.1 ms: 1.00x faster                                  |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.85 sec: 1.26x faster                                 |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                   |
| xml_etree_generate   | 89.2 ms                                                | 80.2 ms: 1.11x faster                                  |
| xml_etree_process    | 61.7 ms                                                | 55.7 ms: 1.11x faster                                  |
| xml_etree_iterparse  | 107 ms                                                 | 97.7 ms: 1.09x faster                                  |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                   |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                   |
| json_loads           | 28.5 us                                                | 30.0 us: 1.05x slower                                  |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.11x slower                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.20 ms: 1.18x slower                                  |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                  |
| Geometric mean         | (ref)                                                  | 1.27x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.1 ms: 1.08x faster                                  |
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                  |
| Geometric mean  | (ref)                                                  | 1.07x faster                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.12x faster                                 |
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                   |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.89x faster                                   |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                   |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                   |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                   |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                   |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.41x faster                                  |
| float                      | 84.7 ms                                                | 63.0 ms: 1.34x faster                                  |
| richards                   | 45.8 ms                                                | 35.2 ms: 1.30x faster                                  |
| richards_super             | 51.5 ms                                                | 40.7 ms: 1.26x faster                                  |
| tomli_loads                | 2.33 sec                                               | 1.85 sec: 1.26x faster                                 |
| spectral_norm              | 115 ms                                                 | 92.9 ms: 1.24x faster                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.24x faster                                  |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.24x faster                                   |
| deltablue                  | 3.72 ms                                                | 3.01 ms: 1.24x faster                                  |
| raytrace                   | 312 ms                                                 | 266 ms: 1.18x faster                                   |
| logging_simple             | 6.46 us                                                | 5.50 us: 1.17x faster                                  |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                  |
| logging_format             | 7.23 us                                                | 6.18 us: 1.17x faster                                  |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                   |
| comprehensions             | 21.8 us                                                | 18.8 us: 1.16x faster                                  |
| nbody                      | 97.0 ms                                                | 84.9 ms: 1.14x faster                                  |
| chaos                      | 67.0 ms                                                | 58.8 ms: 1.14x faster                                  |
| dulwich_log                | 68.5 ms                                                | 60.4 ms: 1.14x faster                                  |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                   |
| async_generators           | 463 ms                                                 | 412 ms: 1.12x faster                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                   |
| xml_etree_generate         | 89.2 ms                                                | 80.2 ms: 1.11x faster                                  |
| xml_etree_process          | 61.7 ms                                                | 55.7 ms: 1.11x faster                                  |
| sympy_sum                  | 169 ms                                                 | 153 ms: 1.11x faster                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 68.0 ms: 1.10x faster                                  |
| go                         | 139 ms                                                 | 127 ms: 1.10x faster                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                  |
| generators                 | 31.2 ms                                                | 28.4 ms: 1.10x faster                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.63 ms: 1.09x faster                                  |
| xml_etree_iterparse        | 107 ms                                                 | 97.7 ms: 1.09x faster                                  |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                   |
| pyflate                    | 482 ms                                                 | 443 ms: 1.09x faster                                   |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                   |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                   |
| crypto_pyaes               | 81.9 ms                                                | 75.7 ms: 1.08x faster                                  |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.08x faster                                  |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                  |
| logging_silent             | 104 ns                                                 | 97.6 ns: 1.07x faster                                  |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                  |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                   |
| sqlite_synth               | 2.83 us                                                | 2.71 us: 1.05x faster                                  |
| regex_effbot               | 3.61 ms                                                | 3.47 ms: 1.04x faster                                  |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                   |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                 |
| pprint_safe_repr           | 776 ms                                                 | 764 ms: 1.02x faster                                   |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                   |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                   |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                   |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                  |
| sympy_expand               | 478 ms                                                 | 476 ms: 1.00x faster                                   |
| regex_v8                   | 23.1 ms                                                | 23.1 ms: 1.00x faster                                  |
| fannkuch                   | 417 ms                                                 | 419 ms: 1.01x slower                                   |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                  |
| bench_thread_pool          | 842 us                                                 | 882 us: 1.05x slower                                   |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                   |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                   |
| json_loads                 | 28.5 us                                                | 30.0 us: 1.05x slower                                  |
| hexiom                     | 6.41 ms                                                | 6.78 ms: 1.06x slower                                  |
| telco                      | 7.10 ms                                                | 7.76 ms: 1.09x slower                                  |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                  |
| coverage                   | 72.7 ms                                                | 84.6 ms: 1.16x slower                                  |
| python_startup_no_site     | 6.94 ms                                                | 8.20 ms: 1.18x slower                                  |
| gc_traversal               | 3.79 ms                                                | 4.76 ms: 1.25x slower                                  |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                  |
| bench_mp_pool              | 24.0 ms                                                | 83.0 ms: 3.46x slower                                  |
| Geometric mean             | (ref)                                                  | 1.11x faster                                           |

Benchmark hidden because not significant (4): nqueens, asyncio_websockets, pprint_pformat, pycparser
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250329-3.14.0a6+-138f037-JIT/bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.130x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.12x