# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_10_7
- machine: linux-x86_64
- commit hash: c421917
- commit date: 2025-03-29
- overall geometric mean: 1.108x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 267 ms: 1.03x faster                                                |
| docutils       | 2.77 sec                                               | 2.71 sec: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                                |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.82x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 472 ms: 1.54x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 486 ms: 1.49x faster                                                |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.5 ms: 1.29x faster                                               |
| nbody          | 97.0 ms                                                | 90.2 ms: 1.08x faster                                               |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.12x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.45 ms: 1.05x faster                                               |
| regex_v8       | 23.1 ms                                                | 23.6 ms: 1.02x slower                                               |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.89 sec: 1.24x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 80.3 ms: 1.11x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 56.3 ms: 1.10x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 98.1 ms: 1.09x faster                                               |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.08x faster                                                |
| json_loads           | 28.5 us                                                | 30.2 us: 1.06x slower                                               |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.13x slower                                               |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.19 ms: 1.18x slower                                               |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                               |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                               |
| django_template | 34.6 ms                                                | 32.1 ms: 1.08x faster                                               |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                                |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.82x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 472 ms: 1.54x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 486 ms: 1.49x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 28.9 us: 1.41x faster                                               |
| deepcopy                   | 371 us                                                 | 266 us: 1.40x faster                                                |
| float                      | 84.7 ms                                                | 65.5 ms: 1.29x faster                                               |
| richards_super             | 51.5 ms                                                | 40.1 ms: 1.28x faster                                               |
| richards                   | 45.8 ms                                                | 35.8 ms: 1.28x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.89 sec: 1.24x faster                                              |
| deltablue                  | 3.72 ms                                                | 3.04 ms: 1.22x faster                                               |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                |
| spectral_norm              | 115 ms                                                 | 94.9 ms: 1.21x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.80 us: 1.20x faster                                               |
| logging_format             | 7.23 us                                                | 6.17 us: 1.17x faster                                               |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                                |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                               |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                               |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                |
| comprehensions             | 21.8 us                                                | 19.0 us: 1.14x faster                                               |
| dulwich_log                | 68.5 ms                                                | 60.4 ms: 1.13x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                |
| async_generators           | 463 ms                                                 | 414 ms: 1.12x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 80.3 ms: 1.11x faster                                               |
| chaos                      | 67.0 ms                                                | 60.5 ms: 1.11x faster                                               |
| pyflate                    | 482 ms                                                 | 436 ms: 1.11x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 56.3 ms: 1.10x faster                                               |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 69.0 ms: 1.09x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 98.1 ms: 1.09x faster                                               |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                               |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.08x faster                                                |
| django_template            | 34.6 ms                                                | 32.1 ms: 1.08x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.08x faster                                                |
| nbody                      | 97.0 ms                                                | 90.2 ms: 1.08x faster                                               |
| sympy_str                  | 300 ms                                                 | 279 ms: 1.08x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 76.4 ms: 1.07x faster                                               |
| sqlalchemy_declarative     | 147 ms                                                 | 137 ms: 1.07x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.6 ms: 1.06x faster                                               |
| generators                 | 31.2 ms                                                | 29.4 ms: 1.06x faster                                               |
| logging_silent             | 104 ns                                                 | 98.5 ns: 1.06x faster                                               |
| go                         | 139 ms                                                 | 132 ms: 1.06x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.78 ms: 1.06x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 20.4 ms: 1.05x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.45 ms: 1.05x faster                                               |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.73 us: 1.04x faster                                               |
| 2to3                       | 274 ms                                                 | 267 ms: 1.03x faster                                                |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.03x faster                                              |
| docutils                   | 2.77 sec                                               | 2.71 sec: 1.02x faster                                              |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                |
| sympy_expand               | 478 ms                                                 | 481 ms: 1.01x slower                                                |
| fannkuch                   | 417 ms                                                 | 422 ms: 1.01x slower                                                |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.01x slower                                               |
| json                       | 5.26 ms                                                | 5.34 ms: 1.01x slower                                               |
| regex_v8                   | 23.1 ms                                                | 23.6 ms: 1.02x slower                                               |
| nqueens                    | 83.3 ms                                                | 86.1 ms: 1.03x slower                                               |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                |
| bench_thread_pool          | 842 us                                                 | 892 us: 1.06x slower                                                |
| json_loads                 | 28.5 us                                                | 30.2 us: 1.06x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                |
| hexiom                     | 6.41 ms                                                | 7.04 ms: 1.10x slower                                               |
| telco                      | 7.10 ms                                                | 7.82 ms: 1.10x slower                                               |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.13x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 8.19 ms: 1.18x slower                                               |
| coverage                   | 72.7 ms                                                | 85.8 ms: 1.18x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.98 ms: 1.31x slower                                               |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.69x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.45x slower                                               |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                        |

Benchmark hidden because not significant (6): scimark_lu, asyncio_websockets, pickle_pure_python, pycparser, pprint_pformat, pprint_safe_repr
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-c421917-JIT/bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x