# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_unknown_syms
- machine: linux-x86_64
- commit hash: 2ba5562
- commit date: 2025-03-28
- overall geometric mean: 1.117x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                     |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 611 ms: 1.89x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                     |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.48x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 64.8 ms: 1.31x faster                                                    |
| nbody          | 97.0 ms                                                | 87.9 ms: 1.10x faster                                                    |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.13x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.47 ms: 1.04x faster                                                    |
| regex_v8       | 23.1 ms                                                | 23.4 ms: 1.01x slower                                                    |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.86 sec: 1.25x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 79.1 ms: 1.13x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 55.2 ms: 1.12x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                                    |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                     |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                                    |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                             |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.19 ms: 1.18x slower                                                    |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.5 ms: 1.10x faster                                                    |
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 611 ms: 1.89x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                     |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.48x faster                                                     |
| deepcopy                   | 371 us                                                 | 257 us: 1.45x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                    |
| float                      | 84.7 ms                                                | 64.8 ms: 1.31x faster                                                    |
| richards                   | 45.8 ms                                                | 35.2 ms: 1.30x faster                                                    |
| richards_super             | 51.5 ms                                                | 40.0 ms: 1.29x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 1.86 sec: 1.25x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                    |
| spectral_norm              | 115 ms                                                 | 94.2 ms: 1.22x faster                                                    |
| scimark_fft                | 382 ms                                                 | 314 ms: 1.22x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.06 ms: 1.21x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                    |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                     |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                                     |
| comprehensions             | 21.8 us                                                | 18.7 us: 1.16x faster                                                    |
| logging_format             | 7.23 us                                                | 6.26 us: 1.16x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.63 us: 1.15x faster                                                    |
| dulwich_log                | 68.5 ms                                                | 60.5 ms: 1.13x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 79.1 ms: 1.13x faster                                                    |
| chaos                      | 67.0 ms                                                | 59.5 ms: 1.13x faster                                                    |
| async_generators           | 463 ms                                                 | 412 ms: 1.12x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 67.1 ms: 1.12x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 55.2 ms: 1.12x faster                                                    |
| generators                 | 31.2 ms                                                | 28.1 ms: 1.11x faster                                                    |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                                    |
| pyflate                    | 482 ms                                                 | 436 ms: 1.11x faster                                                     |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                     |
| nbody                      | 97.0 ms                                                | 87.9 ms: 1.10x faster                                                    |
| django_template            | 34.6 ms                                                | 31.5 ms: 1.10x faster                                                    |
| go                         | 139 ms                                                 | 127 ms: 1.10x faster                                                     |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                     |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.68 ms: 1.08x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.46 sec: 1.07x faster                                                   |
| logging_silent             | 104 ns                                                 | 98.1 ns: 1.06x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 20.2 ms: 1.06x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 77.7 ms: 1.05x faster                                                    |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                     |
| sqlite_synth               | 2.83 us                                                | 2.73 us: 1.04x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.47 ms: 1.04x faster                                                    |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                   |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                     |
| sympy_expand               | 478 ms                                                 | 469 ms: 1.02x faster                                                     |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                     |
| json                       | 5.26 ms                                                | 5.31 ms: 1.01x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 23.4 ms: 1.01x slower                                                    |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.01x slower                                                    |
| fannkuch                   | 417 ms                                                 | 423 ms: 1.01x slower                                                     |
| nqueens                    | 83.3 ms                                                | 86.4 ms: 1.04x slower                                                    |
| hexiom                     | 6.41 ms                                                | 6.69 ms: 1.04x slower                                                    |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                                    |
| bench_thread_pool          | 842 us                                                 | 882 us: 1.05x slower                                                     |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                    |
| telco                      | 7.10 ms                                                | 7.82 ms: 1.10x slower                                                    |
| coverage                   | 72.7 ms                                                | 84.2 ms: 1.16x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 8.19 ms: 1.18x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 4.99 ms: 1.32x slower                                                    |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 2.50 ms: 1.69x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 82.8 ms: 3.45x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                             |

Benchmark hidden because not significant (6): pprint_safe_repr, pickle_pure_python, pycparser, scimark_lu, asyncio_websockets, pprint_pformat
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250328-3.14.0a6+-2ba5562-JIT/bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.117x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x