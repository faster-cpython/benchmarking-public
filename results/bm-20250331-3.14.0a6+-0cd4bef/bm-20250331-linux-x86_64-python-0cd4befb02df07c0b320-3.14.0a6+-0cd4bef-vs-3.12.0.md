# Results vs. 3.12.0

- fork: python
- ref: 0cd4befb02df07c0b320
- machine: linux-x86_64
- commit hash: 0cd4bef
- commit date: 2025-03-31
- overall geometric mean: 1.121x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                   |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 610 ms: 1.89x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                   |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 483 ms: 1.50x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.3 ms: 1.22x faster                                                  |
| nbody          | 97.0 ms                                                | 96.4 ms: 1.01x faster                                                  |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                   |
| regex_v8       | 23.1 ms                                                | 22.9 ms: 1.01x faster                                                  |
| regex_dna      | 212 ms                                                 | 215 ms: 1.02x slower                                                   |
| regex_effbot   | 3.61 ms                                                | 3.80 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 99.1 ms: 1.08x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 85.0 ms: 1.05x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                                   |
| json_loads           | 28.5 us                                                | 29.9 us: 1.05x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.16 ms: 1.18x slower                                                  |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                  |
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.13x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 610 ms: 1.89x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                   |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 483 ms: 1.50x faster                                                   |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 30.0 us: 1.36x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.31x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                  |
| float                      | 84.7 ms                                                | 69.3 ms: 1.22x faster                                                  |
| go                         | 139 ms                                                 | 115 ms: 1.22x faster                                                   |
| spectral_norm              | 115 ms                                                 | 96.3 ms: 1.19x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                 |
| async_generators           | 463 ms                                                 | 389 ms: 1.19x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.15 ms: 1.18x faster                                                  |
| raytrace                   | 312 ms                                                 | 266 ms: 1.18x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 58.4 ms: 1.17x faster                                                  |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                   |
| logging_format             | 7.23 us                                                | 6.21 us: 1.16x faster                                                  |
| chaos                      | 67.0 ms                                                | 58.1 ms: 1.15x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.66 us: 1.14x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.12x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.2 ms: 1.12x faster                                                  |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 73.8 ms: 1.11x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.9 ms: 1.11x faster                                                  |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                                  |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                   |
| django_template            | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                  |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 99.1 ms: 1.08x faster                                                  |
| scimark_fft                | 382 ms                                                 | 355 ms: 1.07x faster                                                   |
| pyflate                    | 482 ms                                                 | 449 ms: 1.07x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 726 ms: 1.07x faster                                                   |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.06x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                 |
| logging_silent             | 104 ns                                                 | 98.9 ns: 1.06x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 85.0 ms: 1.05x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                  |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.86 ms: 1.04x faster                                                  |
| sympy_expand               | 478 ms                                                 | 461 ms: 1.04x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.25 ms: 1.03x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                   |
| richards                   | 45.8 ms                                                | 44.9 ms: 1.02x faster                                                  |
| richards_super             | 51.5 ms                                                | 50.6 ms: 1.02x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                                  |
| regex_v8                   | 23.1 ms                                                | 22.9 ms: 1.01x faster                                                  |
| nqueens                    | 83.3 ms                                                | 82.6 ms: 1.01x faster                                                  |
| nbody                      | 97.0 ms                                                | 96.4 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                  |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.02x slower                                                   |
| json                       | 5.26 ms                                                | 5.35 ms: 1.02x slower                                                  |
| fannkuch                   | 417 ms                                                 | 426 ms: 1.02x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 872 us: 1.04x slower                                                   |
| json_loads                 | 28.5 us                                                | 29.9 us: 1.05x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.80 ms: 1.05x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                  |
| telco                      | 7.10 ms                                                | 7.86 ms: 1.11x slower                                                  |
| coverage                   | 72.7 ms                                                | 84.3 ms: 1.16x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 8.16 ms: 1.18x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 5.02 ms: 1.32x slower                                                  |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.50 ms: 1.69x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 82.5 ms: 3.44x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (2): pycparser, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250331-3.14.0a6+-0cd4bef/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.121x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.11x