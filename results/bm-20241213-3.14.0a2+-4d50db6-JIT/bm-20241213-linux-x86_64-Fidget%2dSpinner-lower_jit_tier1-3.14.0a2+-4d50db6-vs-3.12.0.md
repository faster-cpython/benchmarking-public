# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: lower_jit_tier1
- machine: linux-x86_64
- commit hash: 4d50db6
- commit date: 2024-12-13
- overall geometric mean: 1.100x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                                        |
| docutils       | 2.77 sec                                               | 2.73 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 605 ms: 1.95x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.83x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                        |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 335 ms: 1.73x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.52x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.8 ms: 1.16x faster                                                       |
| nbody          | 97.0 ms                                                | 83.6 ms: 1.16x faster                                                       |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                        |
| regex_effbot   | 3.61 ms                                                | 3.21 ms: 1.12x faster                                                       |
| regex_dna      | 212 ms                                                 | 211 ms: 1.00x faster                                                        |
| regex_v8       | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 194 us: 1.19x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 137 ms: 1.17x faster                                                        |
| xml_etree_generate   | 89.2 ms                                                | 77.3 ms: 1.15x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 54.6 ms: 1.13x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 94.7 ms: 1.13x faster                                                       |
| json_loads           | 28.5 us                                                | 26.0 us: 1.10x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 316 us: 1.02x faster                                                        |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                       |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.95 ms: 1.20x faster                                                       |
| django_template | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 605 ms: 1.95x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.83x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                        |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 335 ms: 1.73x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.52x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.38x faster                                                       |
| deepcopy                   | 371 us                                                 | 268 us: 1.38x faster                                                        |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.28x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                       |
| mako                       | 11.9 ms                                                | 9.95 ms: 1.20x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 62.8 ms: 1.20x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 194 us: 1.19x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 69.1 ms: 1.18x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 137 ms: 1.17x faster                                                        |
| float                      | 84.7 ms                                                | 72.8 ms: 1.16x faster                                                       |
| nbody                      | 97.0 ms                                                | 83.6 ms: 1.16x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 77.3 ms: 1.15x faster                                                       |
| scimark_fft                | 382 ms                                                 | 333 ms: 1.15x faster                                                        |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                        |
| logging_format             | 7.23 us                                                | 6.35 us: 1.14x faster                                                       |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.14x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 54.6 ms: 1.13x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 94.7 ms: 1.13x faster                                                       |
| regex_effbot               | 3.61 ms                                                | 3.21 ms: 1.12x faster                                                       |
| chaos                      | 67.0 ms                                                | 59.7 ms: 1.12x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.78 us: 1.12x faster                                                       |
| go                         | 139 ms                                                 | 125 ms: 1.12x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                                       |
| raytrace                   | 312 ms                                                 | 282 ms: 1.11x faster                                                        |
| json                       | 5.26 ms                                                | 4.76 ms: 1.11x faster                                                       |
| pyflate                    | 482 ms                                                 | 438 ms: 1.10x faster                                                        |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.10x faster                                                        |
| json_loads                 | 28.5 us                                                | 26.0 us: 1.10x faster                                                       |
| fannkuch                   | 417 ms                                                 | 382 ms: 1.09x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 157 ms: 1.08x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.76 ms: 1.06x faster                                                       |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                       |
| sympy_str                  | 300 ms                                                 | 287 ms: 1.05x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                        |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                       |
| async_generators           | 463 ms                                                 | 446 ms: 1.04x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 20.8 ms: 1.03x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 755 ms: 1.03x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 316 us: 1.02x faster                                                        |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                      |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                        |
| docutils                   | 2.77 sec                                               | 2.73 sec: 1.01x faster                                                      |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                        |
| django_template            | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                       |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                        |
| regex_dna                  | 212 ms                                                 | 211 ms: 1.00x faster                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 55.0 ms: 1.00x slower                                                       |
| dulwich_log                | 68.5 ms                                                | 68.9 ms: 1.01x slower                                                       |
| sympy_expand               | 478 ms                                                 | 484 ms: 1.01x slower                                                        |
| richards_super             | 51.5 ms                                                | 52.3 ms: 1.01x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                       |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                      |
| coroutines                 | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                       |
| nqueens                    | 83.3 ms                                                | 87.3 ms: 1.05x slower                                                       |
| telco                      | 7.10 ms                                                | 7.46 ms: 1.05x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 884 us: 1.05x slower                                                        |
| logging_silent             | 104 ns                                                 | 111 ns: 1.06x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                        |
| mdp                        | 2.63 sec                                               | 2.81 sec: 1.07x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                       |
| hexiom                     | 6.41 ms                                                | 6.93 ms: 1.08x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                       |
| generators                 | 31.2 ms                                                | 34.2 ms: 1.09x slower                                                       |
| coverage                   | 72.7 ms                                                | 82.9 ms: 1.14x slower                                                       |
| mypy2                      | 830 ms                                                 | 965 ms: 1.16x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.77 ms: 1.26x slower                                                       |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 2.44 ms: 1.65x slower                                                       |
| bench_mp_pool              | 24.0 ms                                                | 81.3 ms: 3.39x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                |

Benchmark hidden because not significant (2): richards, asyncio_websockets
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241213-3.14.0a2+-4d50db6-JIT/bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.100x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.11x