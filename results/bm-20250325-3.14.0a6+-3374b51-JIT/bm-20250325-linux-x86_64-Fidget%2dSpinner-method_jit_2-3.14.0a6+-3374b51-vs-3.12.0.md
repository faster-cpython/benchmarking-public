# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: method_jit_2
- machine: linux-x86_64
- commit hash: 3374b51
- commit date: 2025-03-25
- overall geometric mean: 1.086x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                     |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 624 ms: 1.89x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 628 ms: 1.84x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 320 ms: 1.80x faster                                                     |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.77x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.9 ms: 1.20x faster                                                    |
| nbody          | 97.0 ms                                                | 88.2 ms: 1.10x faster                                                    |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                  | 1.10x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.14x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.24 ms: 1.11x faster                                                    |
| regex_v8       | 23.1 ms                                                | 22.7 ms: 1.02x faster                                                    |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 100 ms: 1.06x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 223 us: 1.03x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 86.6 ms: 1.03x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 60.7 ms: 1.02x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 334 us: 1.03x slower                                                     |
| json_loads           | 28.5 us                                                | 29.9 us: 1.05x slower                                                    |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.23 ms: 1.19x slower                                                    |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 33.1 ms: 1.04x faster                                                    |
| mako            | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 624 ms: 1.89x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 628 ms: 1.84x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 320 ms: 1.80x faster                                                     |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.77x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                                     |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                    |
| scimark_fft                | 382 ms                                                 | 314 ms: 1.22x faster                                                     |
| float                      | 84.7 ms                                                | 70.9 ms: 1.20x faster                                                    |
| go                         | 139 ms                                                 | 119 ms: 1.17x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                   |
| async_generators           | 463 ms                                                 | 402 ms: 1.15x faster                                                     |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                                    |
| regex_compile              | 148 ms                                                 | 131 ms: 1.14x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                     |
| regex_effbot               | 3.61 ms                                                | 3.24 ms: 1.11x faster                                                    |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.11x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 61.7 ms: 1.11x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 68.0 ms: 1.10x faster                                                    |
| nbody                      | 97.0 ms                                                | 88.2 ms: 1.10x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.88 us: 1.10x faster                                                    |
| sqlalchemy_declarative     | 147 ms                                                 | 134 ms: 1.10x faster                                                     |
| chaos                      | 67.0 ms                                                | 61.2 ms: 1.09x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.62 ms: 1.09x faster                                                    |
| logging_format             | 7.23 us                                                | 6.65 us: 1.09x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.44 ms: 1.08x faster                                                    |
| raytrace                   | 312 ms                                                 | 289 ms: 1.08x faster                                                     |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 100 ms: 1.06x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 159 ms: 1.06x faster                                                     |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                     |
| comprehensions             | 21.8 us                                                | 20.7 us: 1.05x faster                                                    |
| mdp                        | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 78.0 ms: 1.05x faster                                                    |
| sympy_str                  | 300 ms                                                 | 286 ms: 1.05x faster                                                     |
| django_template            | 34.6 ms                                                | 33.1 ms: 1.04x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 20.6 ms: 1.04x faster                                                    |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                                     |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                   |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                     |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 223 us: 1.03x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 86.6 ms: 1.03x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                   |
| generators                 | 31.2 ms                                                | 30.5 ms: 1.02x faster                                                    |
| pyflate                    | 482 ms                                                 | 472 ms: 1.02x faster                                                     |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                    |
| regex_v8                   | 23.1 ms                                                | 22.7 ms: 1.02x faster                                                    |
| sqlalchemy_imperative      | 18.7 ms                                                | 18.3 ms: 1.02x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 60.7 ms: 1.02x faster                                                    |
| richards                   | 45.8 ms                                                | 45.1 ms: 1.02x faster                                                    |
| fannkuch                   | 417 ms                                                 | 411 ms: 1.01x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 768 ms: 1.01x faster                                                     |
| sympy_expand               | 478 ms                                                 | 474 ms: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                     |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                    |
| json                       | 5.26 ms                                                | 5.34 ms: 1.02x slower                                                    |
| richards_super             | 51.5 ms                                                | 52.5 ms: 1.02x slower                                                    |
| nqueens                    | 83.3 ms                                                | 85.2 ms: 1.02x slower                                                    |
| hexiom                     | 6.41 ms                                                | 6.56 ms: 1.02x slower                                                    |
| pickle_pure_python         | 324 us                                                 | 334 us: 1.03x slower                                                     |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                     |
| json_loads                 | 28.5 us                                                | 29.9 us: 1.05x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 908 us: 1.08x slower                                                     |
| telco                      | 7.10 ms                                                | 7.88 ms: 1.11x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 8.23 ms: 1.19x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 4.83 ms: 1.27x slower                                                    |
| coverage                   | 72.7 ms                                                | 93.7 ms: 1.29x slower                                                    |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 83.4 ms: 3.47x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                             |

Benchmark hidden because not significant (3): asyncio_websockets, pprint_pformat, scimark_lu
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250325-3.14.0a6+-3374b51-JIT/bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.086x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.14x