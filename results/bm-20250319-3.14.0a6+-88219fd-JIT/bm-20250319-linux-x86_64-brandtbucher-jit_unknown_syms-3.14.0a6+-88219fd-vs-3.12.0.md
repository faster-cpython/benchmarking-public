# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_unknown_syms
- machine: linux-x86_64
- commit hash: 88219fd
- commit date: 2025-03-19
- overall geometric mean: 1.117x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                                     |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.84x faster                                                     |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.0 ms: 1.30x faster                                                    |
| nbody          | 97.0 ms                                                | 87.0 ms: 1.11x faster                                                    |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.14x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.53 ms: 1.02x faster                                                    |
| regex_v8       | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                    |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 80.1 ms: 1.11x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 97.8 ms: 1.09x faster                                                    |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                     |
| json_loads           | 28.5 us                                                | 29.6 us: 1.04x slower                                                    |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.16 ms: 1.18x slower                                                    |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                    |
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.84x faster                                                     |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                     |
| deepcopy                   | 371 us                                                 | 256 us: 1.45x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 29.2 us: 1.40x faster                                                    |
| float                      | 84.7 ms                                                | 65.0 ms: 1.30x faster                                                    |
| richards                   | 45.8 ms                                                | 35.3 ms: 1.30x faster                                                    |
| richards_super             | 51.5 ms                                                | 40.6 ms: 1.27x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                    |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.07 ms: 1.21x faster                                                    |
| spectral_norm              | 115 ms                                                 | 96.3 ms: 1.19x faster                                                    |
| raytrace                   | 312 ms                                                 | 268 ms: 1.17x faster                                                     |
| comprehensions             | 21.8 us                                                | 18.8 us: 1.16x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                                    |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                     |
| logging_format             | 7.23 us                                                | 6.25 us: 1.16x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 60.4 ms: 1.13x faster                                                    |
| chaos                      | 67.0 ms                                                | 59.8 ms: 1.12x faster                                                    |
| async_generators           | 463 ms                                                 | 415 ms: 1.12x faster                                                     |
| nbody                      | 97.0 ms                                                | 87.0 ms: 1.11x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 80.1 ms: 1.11x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 67.9 ms: 1.11x faster                                                    |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.10x faster                                                     |
| django_template            | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                    |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.62 ms: 1.10x faster                                                    |
| logging_silent             | 104 ns                                                 | 95.4 ns: 1.09x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 97.8 ms: 1.09x faster                                                    |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                     |
| generators                 | 31.2 ms                                                | 28.7 ms: 1.09x faster                                                    |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                    |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                     |
| pyflate                    | 482 ms                                                 | 451 ms: 1.07x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 78.1 ms: 1.05x faster                                                    |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                                     |
| sqlite_synth               | 2.83 us                                                | 2.72 us: 1.04x faster                                                    |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                   |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                     |
| regex_effbot               | 3.61 ms                                                | 3.53 ms: 1.02x faster                                                    |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 769 ms: 1.01x faster                                                     |
| regex_v8                   | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                    |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                    |
| fannkuch                   | 417 ms                                                 | 424 ms: 1.02x slower                                                     |
| nqueens                    | 83.3 ms                                                | 85.9 ms: 1.03x slower                                                    |
| json_loads                 | 28.5 us                                                | 29.6 us: 1.04x slower                                                    |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 881 us: 1.05x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                     |
| hexiom                     | 6.41 ms                                                | 6.79 ms: 1.06x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                    |
| telco                      | 7.10 ms                                                | 7.87 ms: 1.11x slower                                                    |
| coverage                   | 72.7 ms                                                | 84.4 ms: 1.16x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 8.16 ms: 1.18x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 4.98 ms: 1.31x slower                                                    |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.69x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 82.6 ms: 3.44x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                             |

Benchmark hidden because not significant (5): pprint_pformat, asyncio_websockets, scimark_lu, pycparser, json
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250319-3.14.0a6+-88219fd-JIT/bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.117x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.11x