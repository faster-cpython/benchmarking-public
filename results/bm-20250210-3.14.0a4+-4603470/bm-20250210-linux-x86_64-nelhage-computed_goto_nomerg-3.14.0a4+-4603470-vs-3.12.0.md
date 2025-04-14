# Results vs. 3.12.0

- fork: nelhage
- ref: computed_goto_nomerg
- machine: linux-x86_64
- commit hash: 4603470
- commit date: 2025-02-10
- overall geometric mean: 1.123x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 252 ms: 1.09x faster                                                    |
| docutils       | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 621 ms: 1.86x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 325 ms: 1.78x faster                                                    |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 259 ms: 1.73x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 68.4 ms: 1.24x faster                                                   |
| nbody          | 97.0 ms                                                | 91.7 ms: 1.06x faster                                                   |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.10x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.21 ms: 1.12x faster                                                   |
| regex_dna      | 212 ms                                                 | 211 ms: 1.01x faster                                                    |
| regex_v8       | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 96.5 ms: 1.11x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 83.4 ms: 1.07x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 58.4 ms: 1.06x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 317 us: 1.02x faster                                                    |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                                   |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                   |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.6 ms: 1.10x faster                                                   |
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 621 ms: 1.86x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 325 ms: 1.78x faster                                                    |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 259 ms: 1.73x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                    |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 30.4 us: 1.34x faster                                                   |
| comprehensions             | 21.8 us                                                | 16.3 us: 1.33x faster                                                   |
| float                      | 84.7 ms                                                | 68.4 ms: 1.24x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                   |
| spectral_norm              | 115 ms                                                 | 94.1 ms: 1.22x faster                                                   |
| async_generators           | 463 ms                                                 | 381 ms: 1.21x faster                                                    |
| go                         | 139 ms                                                 | 116 ms: 1.21x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.39 us: 1.20x faster                                                   |
| logging_format             | 7.23 us                                                | 6.07 us: 1.19x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                  |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.18 ms: 1.17x faster                                                   |
| chaos                      | 67.0 ms                                                | 57.5 ms: 1.17x faster                                                   |
| raytrace                   | 312 ms                                                 | 268 ms: 1.17x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 70.4 ms: 1.16x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.15x faster                                                    |
| sqlalchemy_declarative     | 147 ms                                                 | 127 ms: 1.15x faster                                                    |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.3 ms: 1.14x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 66.2 ms: 1.13x faster                                                   |
| scimark_fft                | 382 ms                                                 | 339 ms: 1.13x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.21 ms: 1.12x faster                                                   |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                    |
| generators                 | 31.2 ms                                                | 27.8 ms: 1.12x faster                                                   |
| pyflate                    | 482 ms                                                 | 435 ms: 1.11x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 96.5 ms: 1.11x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.23 ms: 1.10x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 707 ms: 1.10x faster                                                    |
| django_template            | 34.6 ms                                                | 31.6 ms: 1.10x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.54 ms: 1.09x faster                                                   |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                   |
| 2to3                       | 274 ms                                                 | 252 ms: 1.09x faster                                                    |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 103 ms: 1.07x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 83.4 ms: 1.07x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                    |
| mdp                        | 2.63 sec                                               | 2.46 sec: 1.07x faster                                                  |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                    |
| sqlglot_optimize           | 54.8 ms                                                | 51.5 ms: 1.06x faster                                                   |
| sympy_expand               | 478 ms                                                 | 450 ms: 1.06x faster                                                    |
| dulwich_log                | 68.5 ms                                                | 64.5 ms: 1.06x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 58.4 ms: 1.06x faster                                                   |
| nbody                      | 97.0 ms                                                | 91.7 ms: 1.06x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.10 ms: 1.05x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.85 ms: 1.04x faster                                                   |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.04x faster                                                    |
| richards                   | 45.8 ms                                                | 44.3 ms: 1.04x faster                                                   |
| nqueens                    | 83.3 ms                                                | 81.0 ms: 1.03x faster                                                   |
| richards_super             | 51.5 ms                                                | 50.2 ms: 1.03x faster                                                   |
| json                       | 5.26 ms                                                | 5.15 ms: 1.02x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 317 us: 1.02x faster                                                    |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| regex_dna                  | 212 ms                                                 | 211 ms: 1.01x faster                                                    |
| logging_silent             | 104 ns                                                 | 104 ns: 1.00x faster                                                    |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.00x slower                                                   |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 860 us: 1.02x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                   |
| telco                      | 7.10 ms                                                | 7.80 ms: 1.10x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                   |
| coverage                   | 72.7 ms                                                | 89.5 ms: 1.23x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 4.73 ms: 1.25x slower                                                   |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.68x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                            |

Benchmark hidden because not significant (3): scimark_lu, asyncio_websockets, typing_runtime_protocols
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250210-3.14.0a4+-4603470/bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.123x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.09x