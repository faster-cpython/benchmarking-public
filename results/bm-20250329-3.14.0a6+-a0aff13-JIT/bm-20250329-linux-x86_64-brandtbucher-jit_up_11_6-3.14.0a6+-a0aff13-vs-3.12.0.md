# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_11_6
- machine: linux-x86_64
- commit hash: a0aff13
- commit date: 2025-03-29
- overall geometric mean: 1.109x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 265 ms: 1.04x faster                                                |
| docutils       | 2.77 sec                                               | 2.71 sec: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                                |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.7 ms: 1.29x faster                                               |
| nbody          | 97.0 ms                                                | 86.8 ms: 1.12x faster                                               |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.13x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.36 ms: 1.08x faster                                               |
| regex_v8       | 23.1 ms                                                | 23.6 ms: 1.02x slower                                               |
| regex_dna      | 212 ms                                                 | 226 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.88 sec: 1.24x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 80.6 ms: 1.11x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 98.0 ms: 1.09x faster                                               |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 56.9 ms: 1.08x faster                                               |
| json_loads           | 28.5 us                                                | 30.1 us: 1.05x slower                                               |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.11x slower                                               |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.19 ms: 1.18x slower                                               |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                               |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                               |
| django_template | 34.6 ms                                                | 32.0 ms: 1.08x faster                                               |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                                |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                |
| deepcopy                   | 371 us                                                 | 264 us: 1.41x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.1 us: 1.40x faster                                               |
| float                      | 84.7 ms                                                | 65.7 ms: 1.29x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.88 sec: 1.24x faster                                              |
| scimark_fft                | 382 ms                                                 | 311 ms: 1.23x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.23x faster                                               |
| richards                   | 45.8 ms                                                | 37.7 ms: 1.22x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.07 ms: 1.21x faster                                               |
| richards_super             | 51.5 ms                                                | 42.8 ms: 1.20x faster                                               |
| spectral_norm              | 115 ms                                                 | 96.6 ms: 1.19x faster                                               |
| raytrace                   | 312 ms                                                 | 268 ms: 1.17x faster                                                |
| logging_format             | 7.23 us                                                | 6.26 us: 1.16x faster                                               |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                |
| comprehensions             | 21.8 us                                                | 19.0 us: 1.15x faster                                               |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                               |
| dulwich_log                | 68.5 ms                                                | 60.7 ms: 1.13x faster                                               |
| nbody                      | 97.0 ms                                                | 86.8 ms: 1.12x faster                                               |
| chaos                      | 67.0 ms                                                | 60.0 ms: 1.12x faster                                               |
| async_generators           | 463 ms                                                 | 415 ms: 1.11x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 80.6 ms: 1.11x faster                                               |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 68.6 ms: 1.10x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 98.0 ms: 1.09x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.2 ms: 1.09x faster                                               |
| xml_etree_process          | 61.7 ms                                                | 56.9 ms: 1.08x faster                                               |
| generators                 | 31.2 ms                                                | 28.8 ms: 1.08x faster                                               |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                               |
| sympy_str                  | 300 ms                                                 | 277 ms: 1.08x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.68 ms: 1.08x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 75.8 ms: 1.08x faster                                               |
| django_template            | 34.6 ms                                                | 32.0 ms: 1.08x faster                                               |
| sqlalchemy_declarative     | 147 ms                                                 | 136 ms: 1.08x faster                                                |
| go                         | 139 ms                                                 | 130 ms: 1.08x faster                                                |
| regex_effbot               | 3.61 ms                                                | 3.36 ms: 1.08x faster                                               |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 20.3 ms: 1.06x faster                                               |
| pyflate                    | 482 ms                                                 | 458 ms: 1.05x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 738 ms: 1.05x faster                                                |
| mdp                        | 2.63 sec                                               | 2.51 sec: 1.05x faster                                              |
| logging_silent             | 104 ns                                                 | 99.6 ns: 1.05x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.71 us: 1.05x faster                                               |
| 2to3                       | 274 ms                                                 | 265 ms: 1.04x faster                                                |
| docutils                   | 2.77 sec                                               | 2.71 sec: 1.02x faster                                              |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                              |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                |
| sympy_expand               | 478 ms                                                 | 474 ms: 1.01x faster                                                |
| fannkuch                   | 417 ms                                                 | 424 ms: 1.02x slower                                                |
| regex_v8                   | 23.1 ms                                                | 23.6 ms: 1.02x slower                                               |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                               |
| json                       | 5.26 ms                                                | 5.40 ms: 1.03x slower                                               |
| nqueens                    | 83.3 ms                                                | 86.7 ms: 1.04x slower                                               |
| bench_thread_pool          | 842 us                                                 | 887 us: 1.05x slower                                                |
| json_loads                 | 28.5 us                                                | 30.1 us: 1.05x slower                                               |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.06x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.88 ms: 1.07x slower                                               |
| telco                      | 7.10 ms                                                | 7.86 ms: 1.11x slower                                               |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 8.19 ms: 1.18x slower                                               |
| coverage                   | 72.7 ms                                                | 86.2 ms: 1.19x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.65 ms: 1.22x slower                                               |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 83.1 ms: 3.46x slower                                               |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                        |

Benchmark hidden because not significant (3): asyncio_websockets, pickle_pure_python, pycparser
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-a0aff13-JIT/bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.109x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.12x