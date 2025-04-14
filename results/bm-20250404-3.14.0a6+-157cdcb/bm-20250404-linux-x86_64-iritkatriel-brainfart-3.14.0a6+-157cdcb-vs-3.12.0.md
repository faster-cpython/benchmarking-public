# Results vs. 3.12.0

- fork: iritkatriel
- ref: brainfart
- machine: linux-x86_64
- commit hash: 157cdcb
- commit date: 2025-04-04
- overall geometric mean: 1.139x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-linux-x86_64-iritkatriel-brainfart-3.14.0a6+-157cdcb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 247 ms: 1.11x faster                                             |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.06x faster                                           |
| Geometric mean | (ref)                                                  | 1.08x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-linux-x86_64-iritkatriel-brainfart-3.14.0a6+-157cdcb |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                             |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                             |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 470 ms: 1.54x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 476 ms: 1.52x faster                                             |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-linux-x86_64-iritkatriel-brainfart-3.14.0a6+-157cdcb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 67.2 ms: 1.26x faster                                            |
| nbody          | 97.0 ms                                                | 90.1 ms: 1.08x faster                                            |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.11x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-linux-x86_64-iritkatriel-brainfart-3.14.0a6+-157cdcb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 124 ms: 1.20x faster                                             |
| regex_effbot   | 3.61 ms                                                | 3.18 ms: 1.13x faster                                            |
| regex_dna      | 212 ms                                                 | 214 ms: 1.01x slower                                             |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-linux-x86_64-iritkatriel-brainfart-3.14.0a6+-157cdcb |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                           |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.14x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 97.8 ms: 1.09x faster                                            |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.06x faster                                             |
| xml_etree_generate   | 89.2 ms                                                | 83.9 ms: 1.06x faster                                            |
| xml_etree_process    | 61.7 ms                                                | 58.5 ms: 1.06x faster                                            |
| pickle_pure_python   | 324 us                                                 | 311 us: 1.04x faster                                             |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                            |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.11x slower                                            |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-linux-x86_64-iritkatriel-brainfart-3.14.0a6+-157cdcb |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.20 ms: 1.18x slower                                            |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                            |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-linux-x86_64-iritkatriel-brainfart-3.14.0a6+-157cdcb |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.5 ms: 1.10x faster                                            |
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                            |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-linux-x86_64-iritkatriel-brainfart-3.14.0a6+-157cdcb |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.16x faster                                           |
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                             |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                             |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 470 ms: 1.54x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 476 ms: 1.52x faster                                             |
| deepcopy                   | 371 us                                                 | 250 us: 1.48x faster                                             |
| deepcopy_memo              | 40.7 us                                                | 28.4 us: 1.44x faster                                            |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                            |
| go                         | 139 ms                                                 | 109 ms: 1.28x faster                                             |
| float                      | 84.7 ms                                                | 67.2 ms: 1.26x faster                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.24x faster                                            |
| raytrace                   | 312 ms                                                 | 255 ms: 1.22x faster                                             |
| spectral_norm              | 115 ms                                                 | 94.5 ms: 1.22x faster                                            |
| chaos                      | 67.0 ms                                                | 55.1 ms: 1.21x faster                                            |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                           |
| logging_format             | 7.23 us                                                | 6.03 us: 1.20x faster                                            |
| regex_compile              | 148 ms                                                 | 124 ms: 1.20x faster                                             |
| async_generators           | 463 ms                                                 | 388 ms: 1.19x faster                                             |
| logging_simple             | 6.46 us                                                | 5.45 us: 1.19x faster                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 64.1 ms: 1.17x faster                                            |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                            |
| dulwich_log                | 68.5 ms                                                | 58.7 ms: 1.17x faster                                            |
| scimark_fft                | 382 ms                                                 | 331 ms: 1.16x faster                                             |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.14x faster                                             |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                             |
| crypto_pyaes               | 81.9 ms                                                | 72.2 ms: 1.13x faster                                            |
| regex_effbot               | 3.61 ms                                                | 3.18 ms: 1.13x faster                                            |
| deltablue                  | 3.72 ms                                                | 3.29 ms: 1.13x faster                                            |
| sympy_integrate            | 21.4 ms                                                | 19.1 ms: 1.12x faster                                            |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                             |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.11x faster                                             |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                             |
| 2to3                       | 274 ms                                                 | 247 ms: 1.11x faster                                             |
| logging_silent             | 104 ns                                                 | 94.0 ns: 1.11x faster                                            |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                            |
| django_template            | 34.6 ms                                                | 31.5 ms: 1.10x faster                                            |
| pyflate                    | 482 ms                                                 | 441 ms: 1.09x faster                                             |
| xml_etree_iterparse        | 107 ms                                                 | 97.8 ms: 1.09x faster                                            |
| pprint_safe_repr           | 776 ms                                                 | 713 ms: 1.09x faster                                             |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.08x faster                                           |
| nbody                      | 97.0 ms                                                | 90.1 ms: 1.08x faster                                            |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                            |
| richards                   | 45.8 ms                                                | 42.9 ms: 1.07x faster                                            |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.06x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 83.9 ms: 1.06x faster                                            |
| generators                 | 31.2 ms                                                | 29.4 ms: 1.06x faster                                            |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                             |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                           |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.06x faster                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.79 ms: 1.06x faster                                            |
| xml_etree_process          | 61.7 ms                                                | 58.5 ms: 1.06x faster                                            |
| hexiom                     | 6.41 ms                                                | 6.13 ms: 1.05x faster                                            |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                             |
| pickle_pure_python         | 324 us                                                 | 311 us: 1.04x faster                                             |
| richards_super             | 51.5 ms                                                | 49.6 ms: 1.04x faster                                            |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                             |
| nqueens                    | 83.3 ms                                                | 80.9 ms: 1.03x faster                                            |
| fannkuch                   | 417 ms                                                 | 407 ms: 1.02x faster                                             |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.01x faster                                            |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                             |
| regex_dna                  | 212 ms                                                 | 214 ms: 1.01x slower                                             |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                            |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                            |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                             |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                            |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                            |
| bench_thread_pool          | 842 us                                                 | 882 us: 1.05x slower                                             |
| telco                      | 7.10 ms                                                | 7.84 ms: 1.11x slower                                            |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                            |
| coverage                   | 72.7 ms                                                | 84.9 ms: 1.17x slower                                            |
| python_startup_no_site     | 6.94 ms                                                | 8.20 ms: 1.18x slower                                            |
| gc_traversal               | 3.79 ms                                                | 4.75 ms: 1.25x slower                                            |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                            |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                            |
| bench_mp_pool              | 24.0 ms                                                | 82.1 ms: 3.42x slower                                            |
| Geometric mean             | (ref)                                                  | 1.12x faster                                                     |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250404-3.14.0a6+-157cdcb/bm-20250404-linux-x86_64-iritkatriel-brainfart-3.14.0a6+-157cdcb.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.139x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.10x