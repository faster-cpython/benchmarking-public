# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: method_jit_bench
- machine: linux-x86_64
- commit hash: d456718
- commit date: 2025-03-18
- overall geometric mean: 1.104x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils  | 2.77 sec                                               | 2.63 sec: 1.05x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                                         |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.83x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.82x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 475 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.2 ms: 1.22x faster                                                        |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.18 ms: 1.13x faster                                                        |
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                                         |
| regex_v8       | 23.1 ms                                                | 23.1 ms: 1.00x faster                                                        |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                         |
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.12x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                                        |
| xml_etree_generate   | 89.2 ms                                                | 83.7 ms: 1.06x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 58.3 ms: 1.06x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                         |
| json_loads           | 28.5 us                                                | 29.5 us: 1.04x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.29 ms: 1.20x slower                                                        |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.39x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.29x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                        |
| mako            | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                                         |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.83x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.82x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 475 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                         |
| deepcopy                   | 371 us                                                 | 264 us: 1.41x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.39x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                        |
| float                      | 84.7 ms                                                | 69.2 ms: 1.22x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.76 us: 1.21x faster                                                        |
| async_generators           | 463 ms                                                 | 393 ms: 1.18x faster                                                         |
| logging_format             | 7.23 us                                                | 6.15 us: 1.18x faster                                                        |
| go                         | 139 ms                                                 | 120 ms: 1.16x faster                                                         |
| spectral_norm              | 115 ms                                                 | 99.2 ms: 1.16x faster                                                        |
| dulwich_log                | 68.5 ms                                                | 59.2 ms: 1.16x faster                                                        |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.63 us: 1.15x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.18 ms: 1.13x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                         |
| raytrace                   | 312 ms                                                 | 278 ms: 1.12x faster                                                         |
| generators                 | 31.2 ms                                                | 27.8 ms: 1.12x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                         |
| chaos                      | 67.0 ms                                                | 59.9 ms: 1.12x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.12x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 67.4 ms: 1.11x faster                                                        |
| scimark_fft                | 382 ms                                                 | 343 ms: 1.11x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                        |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                         |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                                         |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                                        |
| sqlalchemy_declarative     | 147 ms                                                 | 135 ms: 1.09x faster                                                         |
| django_template            | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 75.7 ms: 1.08x faster                                                        |
| pyflate                    | 482 ms                                                 | 446 ms: 1.08x faster                                                         |
| logging_silent             | 104 ns                                                 | 96.8 ns: 1.08x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 83.7 ms: 1.06x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 20.2 ms: 1.06x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 58.3 ms: 1.06x faster                                                        |
| richards                   | 45.8 ms                                                | 43.4 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.81 ms: 1.05x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.63 sec: 1.05x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 739 ms: 1.05x faster                                                         |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                       |
| richards_super             | 51.5 ms                                                | 49.5 ms: 1.04x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                       |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                       |
| hexiom                     | 6.41 ms                                                | 6.19 ms: 1.04x faster                                                        |
| sympy_expand               | 478 ms                                                 | 464 ms: 1.03x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.63 ms: 1.02x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                         |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                        |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.01x faster                                                        |
| fannkuch                   | 417 ms                                                 | 413 ms: 1.01x faster                                                         |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                         |
| regex_v8                   | 23.1 ms                                                | 23.1 ms: 1.00x faster                                                        |
| nqueens                    | 83.3 ms                                                | 83.8 ms: 1.01x slower                                                        |
| json                       | 5.26 ms                                                | 5.35 ms: 1.02x slower                                                        |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                         |
| coroutines                 | 23.2 ms                                                | 24.0 ms: 1.04x slower                                                        |
| json_loads                 | 28.5 us                                                | 29.5 us: 1.04x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 875 us: 1.04x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                        |
| telco                      | 7.10 ms                                                | 7.95 ms: 1.12x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 8.29 ms: 1.20x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.83 ms: 1.27x slower                                                        |
| coverage                   | 72.7 ms                                                | 93.3 ms: 1.28x slower                                                        |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.39x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.50 ms: 1.69x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 85.8 ms: 3.57x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                 |

Benchmark hidden because not significant (3): pickle_pure_python, nbody, asyncio_websockets
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: 2to3, aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250318-3.14.0a6+-d456718-JIT/bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.104x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.13x