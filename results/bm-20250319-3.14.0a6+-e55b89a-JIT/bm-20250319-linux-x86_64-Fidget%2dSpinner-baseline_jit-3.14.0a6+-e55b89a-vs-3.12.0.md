# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: baseline_jit
- machine: linux-x86_64
- commit hash: e55b89a
- commit date: 2025-03-19
- overall geometric mean: 1.093x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                                     |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 319 ms: 1.81x faster                                                     |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.2 ms: 1.17x faster                                                    |
| nbody          | 97.0 ms                                                | 91.1 ms: 1.06x faster                                                    |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.21 ms: 1.12x faster                                                    |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                     |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                  | 1.06x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.83 sec: 1.27x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 97.4 ms: 1.10x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 60.4 ms: 1.02x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 235 us: 1.02x slower                                                     |
| json_loads           | 28.5 us                                                | 29.9 us: 1.05x slower                                                    |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.18 ms: 1.18x slower                                                    |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.9 ms: 1.09x faster                                                    |
| mako            | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 319 ms: 1.81x faster                                                     |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                                     |
| deepcopy                   | 371 us                                                 | 256 us: 1.45x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.39x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 1.83 sec: 1.27x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                    |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                     |
| logging_format             | 7.23 us                                                | 6.10 us: 1.19x faster                                                    |
| float                      | 84.7 ms                                                | 72.2 ms: 1.17x faster                                                    |
| raytrace                   | 312 ms                                                 | 268 ms: 1.16x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.55 us: 1.16x faster                                                    |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                                    |
| dulwich_log                | 68.5 ms                                                | 59.8 ms: 1.15x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                     |
| async_generators           | 463 ms                                                 | 411 ms: 1.13x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.12x faster                                                     |
| regex_effbot               | 3.61 ms                                                | 3.21 ms: 1.12x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.50 ms: 1.12x faster                                                    |
| go                         | 139 ms                                                 | 125 ms: 1.12x faster                                                     |
| chaos                      | 67.0 ms                                                | 60.5 ms: 1.11x faster                                                    |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.11x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.36 ms: 1.11x faster                                                    |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.10x faster                                                    |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 97.4 ms: 1.10x faster                                                    |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.09x faster                                                     |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                     |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                                    |
| django_template            | 34.6 ms                                                | 31.9 ms: 1.09x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 69.4 ms: 1.08x faster                                                    |
| logging_silent             | 104 ns                                                 | 97.0 ns: 1.08x faster                                                    |
| nbody                      | 97.0 ms                                                | 91.1 ms: 1.06x faster                                                    |
| mdp                        | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 20.2 ms: 1.06x faster                                                    |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                    |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                     |
| richards                   | 45.8 ms                                                | 44.1 ms: 1.04x faster                                                    |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 79.7 ms: 1.03x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.03x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 759 ms: 1.02x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 60.4 ms: 1.02x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                   |
| richards_super             | 51.5 ms                                                | 50.5 ms: 1.02x faster                                                    |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                                    |
| sympy_expand               | 478 ms                                                 | 471 ms: 1.02x faster                                                     |
| comprehensions             | 21.8 us                                                | 21.5 us: 1.01x faster                                                    |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                     |
| mako                       | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                     |
| pyflate                    | 482 ms                                                 | 487 ms: 1.01x slower                                                     |
| json                       | 5.26 ms                                                | 5.34 ms: 1.02x slower                                                    |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                     |
| unpickle_pure_python       | 230 us                                                 | 235 us: 1.02x slower                                                     |
| nqueens                    | 83.3 ms                                                | 85.4 ms: 1.03x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                    |
| bench_thread_pool          | 842 us                                                 | 880 us: 1.05x slower                                                     |
| json_loads                 | 28.5 us                                                | 29.9 us: 1.05x slower                                                    |
| fannkuch                   | 417 ms                                                 | 438 ms: 1.05x slower                                                     |
| coroutines                 | 23.2 ms                                                | 24.4 ms: 1.05x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                    |
| telco                      | 7.10 ms                                                | 8.16 ms: 1.15x slower                                                    |
| hexiom                     | 6.41 ms                                                | 7.41 ms: 1.16x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 8.18 ms: 1.18x slower                                                    |
| coverage                   | 72.7 ms                                                | 91.5 ms: 1.26x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 4.98 ms: 1.31x slower                                                    |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.68x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.45x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250319-3.14.0a6+-e55b89a-JIT/bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.093x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.11x