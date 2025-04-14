# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: py_likely_unlikely
- machine: linux-x86_64
- commit hash: 2b26797
- commit date: 2025-01-29
- overall geometric mean: 1.112x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 252 ms: 1.09x faster                                                           |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                         |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                           |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.82x faster                                                           |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                           |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.76x faster                                                           |
| async_tree_memoization     | 578 ms                                                 | 331 ms: 1.74x faster                                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                           |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                          |
| nbody          | 97.0 ms                                                | 93.0 ms: 1.04x faster                                                          |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                           |
| regex_effbot   | 3.61 ms                                                | 3.38 ms: 1.07x faster                                                          |
| regex_dna      | 212 ms                                                 | 213 ms: 1.00x slower                                                           |
| regex_v8       | 23.1 ms                                                | 26.0 ms: 1.12x slower                                                          |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                         |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                                          |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 83.9 ms: 1.06x faster                                                          |
| xml_etree_process    | 61.7 ms                                                | 59.0 ms: 1.05x faster                                                          |
| pickle_pure_python   | 324 us                                                 | 314 us: 1.03x faster                                                           |
| json_loads           | 28.5 us                                                | 29.1 us: 1.02x slower                                                          |
| json_dumps           | 10.4 ms                                                | 11.9 ms: 1.14x slower                                                          |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                          |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                          |
| mako            | 11.9 ms                                                | 11.4 ms: 1.05x faster                                                          |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                           |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.82x faster                                                           |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                           |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.76x faster                                                           |
| async_tree_memoization     | 578 ms                                                 | 331 ms: 1.74x faster                                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                           |
| deepcopy                   | 371 us                                                 | 256 us: 1.45x faster                                                           |
| deepcopy_memo              | 40.7 us                                                | 30.8 us: 1.32x faster                                                          |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                          |
| deepcopy_reduce            | 3.35 us                                                | 2.62 us: 1.28x faster                                                          |
| spectral_norm              | 115 ms                                                 | 94.9 ms: 1.21x faster                                                          |
| float                      | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                          |
| async_generators           | 463 ms                                                 | 387 ms: 1.20x faster                                                           |
| go                         | 139 ms                                                 | 117 ms: 1.19x faster                                                           |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                          |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                                          |
| tomli_loads                | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                         |
| logging_simple             | 6.46 us                                                | 5.51 us: 1.17x faster                                                          |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.15x faster                                                          |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                           |
| chaos                      | 67.0 ms                                                | 58.3 ms: 1.15x faster                                                          |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                           |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.3 ms: 1.15x faster                                                          |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 71.4 ms: 1.15x faster                                                          |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.14x faster                                                           |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                                           |
| generators                 | 31.2 ms                                                | 27.7 ms: 1.13x faster                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 67.4 ms: 1.11x faster                                                          |
| scimark_fft                | 382 ms                                                 | 347 ms: 1.10x faster                                                           |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                          |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                                          |
| 2to3                       | 274 ms                                                 | 252 ms: 1.09x faster                                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.25 ms: 1.09x faster                                                          |
| pprint_safe_repr           | 776 ms                                                 | 717 ms: 1.08x faster                                                           |
| django_template            | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                          |
| sqlglot_transpile          | 1.68 ms                                                | 1.56 ms: 1.08x faster                                                          |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.08x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 64.0 ms: 1.07x faster                                                          |
| regex_effbot               | 3.61 ms                                                | 3.38 ms: 1.07x faster                                                          |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                           |
| mdp                        | 2.63 sec                                               | 2.47 sec: 1.06x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 83.9 ms: 1.06x faster                                                          |
| sympy_expand               | 478 ms                                                 | 451 ms: 1.06x faster                                                           |
| sqlglot_normalize          | 110 ms                                                 | 104 ms: 1.06x faster                                                           |
| pyflate                    | 482 ms                                                 | 458 ms: 1.05x faster                                                           |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                                           |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.05x faster                                                          |
| xml_etree_process          | 61.7 ms                                                | 59.0 ms: 1.05x faster                                                          |
| richards                   | 45.8 ms                                                | 43.8 ms: 1.05x faster                                                          |
| nbody                      | 97.0 ms                                                | 93.0 ms: 1.04x faster                                                          |
| sqlglot_optimize           | 54.8 ms                                                | 52.7 ms: 1.04x faster                                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.86 ms: 1.04x faster                                                          |
| fannkuch                   | 417 ms                                                 | 402 ms: 1.04x faster                                                           |
| hexiom                     | 6.41 ms                                                | 6.19 ms: 1.04x faster                                                          |
| pickle_pure_python         | 324 us                                                 | 314 us: 1.03x faster                                                           |
| nqueens                    | 83.3 ms                                                | 81.1 ms: 1.03x faster                                                          |
| richards_super             | 51.5 ms                                                | 50.2 ms: 1.03x faster                                                          |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.01x faster                                                           |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                          |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                           |
| regex_dna                  | 212 ms                                                 | 213 ms: 1.00x slower                                                           |
| logging_silent             | 104 ns                                                 | 105 ns: 1.01x slower                                                           |
| python_startup_no_site     | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                          |
| json_loads                 | 28.5 us                                                | 29.1 us: 1.02x slower                                                          |
| bench_thread_pool          | 842 us                                                 | 863 us: 1.03x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                           |
| coroutines                 | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                          |
| telco                      | 7.10 ms                                                | 7.80 ms: 1.10x slower                                                          |
| regex_v8                   | 23.1 ms                                                | 26.0 ms: 1.12x slower                                                          |
| json_dumps                 | 10.4 ms                                                | 11.9 ms: 1.14x slower                                                          |
| gc_traversal               | 3.79 ms                                                | 4.57 ms: 1.20x slower                                                          |
| coverage                   | 72.7 ms                                                | 90.9 ms: 1.25x slower                                                          |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                          |
| create_gc_cycles           | 1.48 ms                                                | 2.44 ms: 1.66x slower                                                          |
| bench_mp_pool              | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                   |

Benchmark hidden because not significant (3): pycparser, json, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250129-3.14.0a4+-2b26797/bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.112x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.09x