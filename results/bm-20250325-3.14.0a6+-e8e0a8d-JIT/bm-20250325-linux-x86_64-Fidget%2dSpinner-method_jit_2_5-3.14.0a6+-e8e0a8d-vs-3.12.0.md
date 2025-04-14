# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: method_jit_2_5
- machine: linux-x86_64
- commit hash: e8e0a8d
- commit date: 2025-03-25
- overall geometric mean: 1.087x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3      | 274 ms                                                 | 259 ms: 1.06x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 623 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 319 ms: 1.81x faster                                                       |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.52x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.4 ms: 1.20x faster                                                      |
| nbody          | 97.0 ms                                                | 87.7 ms: 1.11x faster                                                      |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.47 ms: 1.04x faster                                                      |
| regex_v8       | 23.1 ms                                                | 23.5 ms: 1.02x slower                                                      |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.04 sec: 1.14x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 99.0 ms: 1.08x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 85.7 ms: 1.04x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 224 us: 1.02x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 331 us: 1.02x slower                                                       |
| json_loads           | 28.5 us                                                | 30.0 us: 1.05x slower                                                      |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.21 ms: 1.18x slower                                                      |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.7 ms: 1.06x faster                                                      |
| mako            | 11.9 ms                                                | 12.0 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 623 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 319 ms: 1.81x faster                                                       |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.52x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                       |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 30.7 us: 1.32x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                                      |
| scimark_fft                | 382 ms                                                 | 315 ms: 1.21x faster                                                       |
| float                      | 84.7 ms                                                | 70.4 ms: 1.20x faster                                                      |
| go                         | 139 ms                                                 | 121 ms: 1.16x faster                                                       |
| spectral_norm              | 115 ms                                                 | 99.7 ms: 1.15x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 59.8 ms: 1.15x faster                                                      |
| logging_format             | 7.23 us                                                | 6.33 us: 1.14x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 2.04 sec: 1.14x faster                                                     |
| async_generators           | 463 ms                                                 | 406 ms: 1.14x faster                                                       |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.72 us: 1.13x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.32 ms: 1.12x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                                       |
| nbody                      | 97.0 ms                                                | 87.7 ms: 1.11x faster                                                      |
| chaos                      | 67.0 ms                                                | 61.1 ms: 1.10x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 68.7 ms: 1.09x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.2 ms: 1.09x faster                                                      |
| raytrace                   | 312 ms                                                 | 288 ms: 1.09x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.68 ms: 1.08x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 99.0 ms: 1.08x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 157 ms: 1.08x faster                                                       |
| generators                 | 31.2 ms                                                | 29.2 ms: 1.07x faster                                                      |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.06x faster                                                      |
| sympy_str                  | 300 ms                                                 | 282 ms: 1.06x faster                                                       |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                       |
| django_template            | 34.6 ms                                                | 32.7 ms: 1.06x faster                                                      |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 77.8 ms: 1.05x faster                                                      |
| comprehensions             | 21.8 us                                                | 20.8 us: 1.05x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 85.7 ms: 1.04x faster                                                      |
| regex_effbot               | 3.61 ms                                                | 3.47 ms: 1.04x faster                                                      |
| pyflate                    | 482 ms                                                 | 464 ms: 1.04x faster                                                       |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                      |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                                      |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.03x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 224 us: 1.02x faster                                                       |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                                       |
| fannkuch                   | 417 ms                                                 | 412 ms: 1.01x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                       |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                       |
| mako                       | 11.9 ms                                                | 12.0 ms: 1.01x slower                                                      |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                                     |
| richards                   | 45.8 ms                                                | 46.6 ms: 1.02x slower                                                      |
| json                       | 5.26 ms                                                | 5.34 ms: 1.02x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 23.5 ms: 1.02x slower                                                      |
| pickle_pure_python         | 324 us                                                 | 331 us: 1.02x slower                                                       |
| richards_super             | 51.5 ms                                                | 53.0 ms: 1.03x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                       |
| nqueens                    | 83.3 ms                                                | 85.9 ms: 1.03x slower                                                      |
| hexiom                     | 6.41 ms                                                | 6.68 ms: 1.04x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 883 us: 1.05x slower                                                       |
| pprint_safe_repr           | 776 ms                                                 | 815 ms: 1.05x slower                                                       |
| json_loads                 | 28.5 us                                                | 30.0 us: 1.05x slower                                                      |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.06x slower                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.66 sec: 1.06x slower                                                     |
| coroutines                 | 23.2 ms                                                | 24.9 ms: 1.08x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                      |
| telco                      | 7.10 ms                                                | 7.99 ms: 1.13x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 8.21 ms: 1.18x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 4.65 ms: 1.23x slower                                                      |
| coverage                   | 72.7 ms                                                | 92.9 ms: 1.28x slower                                                      |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 83.1 ms: 3.46x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, docutils, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250325-3.14.0a6+-e8e0a8d-JIT/bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.087x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x