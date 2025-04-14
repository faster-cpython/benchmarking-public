# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: py_likely_unlikely
- machine: linux-x86_64
- commit hash: 2b26797
- commit date: 2025-01-29
- overall geometric mean: 1.098x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                                           |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                           |
| async_tree_io              | 1.16 sec                                               | 625 ms: 1.85x faster                                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                           |
| async_tree_none_tg         | 450 ms                                                 | 258 ms: 1.75x faster                                                           |
| async_tree_none            | 472 ms                                                 | 273 ms: 1.73x faster                                                           |
| async_tree_memoization     | 578 ms                                                 | 341 ms: 1.70x faster                                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                           |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 66.4 ms: 1.28x faster                                                          |
| nbody          | 97.0 ms                                                | 86.6 ms: 1.12x faster                                                          |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.13x faster                                                           |
| regex_effbot   | 3.61 ms                                                | 3.23 ms: 1.12x faster                                                          |
| regex_dna      | 212 ms                                                 | 208 ms: 1.02x faster                                                           |
| regex_v8       | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.86 sec: 1.25x faster                                                         |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 202 us: 1.14x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 95.9 ms: 1.11x faster                                                          |
| xml_etree_process    | 61.7 ms                                                | 55.6 ms: 1.11x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 81.5 ms: 1.09x faster                                                          |
| pickle_pure_python   | 324 us                                                 | 317 us: 1.02x faster                                                           |
| json_loads           | 28.5 us                                                | 29.3 us: 1.03x slower                                                          |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                          |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                          |
| python_startup         | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                          |
| django_template | 34.6 ms                                                | 33.6 ms: 1.03x faster                                                          |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                           |
| async_tree_io              | 1.16 sec                                               | 625 ms: 1.85x faster                                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                           |
| async_tree_none_tg         | 450 ms                                                 | 258 ms: 1.75x faster                                                           |
| async_tree_none            | 472 ms                                                 | 273 ms: 1.73x faster                                                           |
| async_tree_memoization     | 578 ms                                                 | 341 ms: 1.70x faster                                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                           |
| deepcopy                   | 371 us                                                 | 270 us: 1.38x faster                                                           |
| deepcopy_memo              | 40.7 us                                                | 31.5 us: 1.29x faster                                                          |
| float                      | 84.7 ms                                                | 66.4 ms: 1.28x faster                                                          |
| tomli_loads                | 2.33 sec                                               | 1.86 sec: 1.25x faster                                                         |
| scimark_fft                | 382 ms                                                 | 314 ms: 1.22x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                                          |
| crypto_pyaes               | 81.9 ms                                                | 67.7 ms: 1.21x faster                                                          |
| comprehensions             | 21.8 us                                                | 18.1 us: 1.20x faster                                                          |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                          |
| spectral_norm              | 115 ms                                                 | 97.1 ms: 1.18x faster                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 63.5 ms: 1.18x faster                                                          |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                          |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                           |
| async_generators           | 463 ms                                                 | 406 ms: 1.14x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 202 us: 1.14x faster                                                           |
| logging_format             | 7.23 us                                                | 6.34 us: 1.14x faster                                                          |
| chaos                      | 67.0 ms                                                | 59.0 ms: 1.14x faster                                                          |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                                          |
| regex_compile              | 148 ms                                                 | 131 ms: 1.13x faster                                                           |
| nbody                      | 97.0 ms                                                | 86.6 ms: 1.12x faster                                                          |
| regex_effbot               | 3.61 ms                                                | 3.23 ms: 1.12x faster                                                          |
| logging_simple             | 6.46 us                                                | 5.78 us: 1.12x faster                                                          |
| xml_etree_iterparse        | 107 ms                                                 | 95.9 ms: 1.11x faster                                                          |
| xml_etree_process          | 61.7 ms                                                | 55.6 ms: 1.11x faster                                                          |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                                           |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.11x faster                                                           |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                                          |
| xml_etree_generate         | 89.2 ms                                                | 81.5 ms: 1.09x faster                                                          |
| raytrace                   | 312 ms                                                 | 287 ms: 1.09x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 157 ms: 1.08x faster                                                           |
| pyflate                    | 482 ms                                                 | 449 ms: 1.08x faster                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.71 ms: 1.07x faster                                                          |
| sympy_str                  | 300 ms                                                 | 282 ms: 1.06x faster                                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                          |
| richards_super             | 51.5 ms                                                | 48.8 ms: 1.06x faster                                                          |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                          |
| fannkuch                   | 417 ms                                                 | 397 ms: 1.05x faster                                                           |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                                           |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.04x faster                                                          |
| sympy_integrate            | 21.4 ms                                                | 20.8 ms: 1.03x faster                                                          |
| django_template            | 34.6 ms                                                | 33.6 ms: 1.03x faster                                                          |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                           |
| go                         | 139 ms                                                 | 136 ms: 1.03x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                         |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                         |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                         |
| pickle_pure_python         | 324 us                                                 | 317 us: 1.02x faster                                                           |
| regex_dna                  | 212 ms                                                 | 208 ms: 1.02x faster                                                           |
| pprint_safe_repr           | 776 ms                                                 | 762 ms: 1.02x faster                                                           |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.01x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                         |
| json                       | 5.26 ms                                                | 5.21 ms: 1.01x faster                                                          |
| dulwich_log                | 68.5 ms                                                | 67.9 ms: 1.01x faster                                                          |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                           |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                           |
| sympy_expand               | 478 ms                                                 | 476 ms: 1.00x faster                                                           |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 55.1 ms: 1.01x slower                                                          |
| python_startup_no_site     | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                          |
| json_loads                 | 28.5 us                                                | 29.3 us: 1.03x slower                                                          |
| regex_v8                   | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                          |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                           |
| logging_silent             | 104 ns                                                 | 111 ns: 1.06x slower                                                           |
| bench_thread_pool          | 842 us                                                 | 898 us: 1.07x slower                                                           |
| telco                      | 7.10 ms                                                | 7.70 ms: 1.09x slower                                                          |
| nqueens                    | 83.3 ms                                                | 91.3 ms: 1.10x slower                                                          |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                          |
| hexiom                     | 6.41 ms                                                | 7.31 ms: 1.14x slower                                                          |
| generators                 | 31.2 ms                                                | 37.3 ms: 1.19x slower                                                          |
| coverage                   | 72.7 ms                                                | 90.5 ms: 1.24x slower                                                          |
| gc_traversal               | 3.79 ms                                                | 4.73 ms: 1.25x slower                                                          |
| python_startup             | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                          |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                          |
| bench_mp_pool              | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                   |

Benchmark hidden because not significant (2): richards, coroutines
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250129-3.14.0a4+-2b26797-JIT/bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.098x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.10x