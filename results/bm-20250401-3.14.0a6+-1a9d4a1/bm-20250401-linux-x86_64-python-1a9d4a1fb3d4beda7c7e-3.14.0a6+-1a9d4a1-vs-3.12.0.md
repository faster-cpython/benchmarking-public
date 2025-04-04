# Results vs. 3.12.0

- fork: python
- ref: 1a9d4a1fb3d4beda7c7e
- machine: linux-x86_64
- commit hash: 1a9d4a1
- commit date: 2025-04-01
- overall geometric mean: 1.129x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 252 ms: 1.09x faster                                                   |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                   |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 68.6 ms: 1.24x faster                                                  |
| nbody          | 97.0 ms                                                | 93.8 ms: 1.03x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.29 ms: 1.10x faster                                                  |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 144 ms: 1.11x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 98.8 ms: 1.08x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 84.1 ms: 1.06x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 313 us: 1.03x faster                                                   |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.18 ms: 1.18x slower                                                  |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.3 ms: 1.10x faster                                                  |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.16x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                   |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                   |
| deepcopy                   | 371 us                                                 | 251 us: 1.48x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 28.9 us: 1.41x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                  |
| go                         | 139 ms                                                 | 111 ms: 1.25x faster                                                   |
| float                      | 84.7 ms                                                | 68.6 ms: 1.24x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                                  |
| raytrace                   | 312 ms                                                 | 256 ms: 1.22x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                 |
| chaos                      | 67.0 ms                                                | 56.3 ms: 1.19x faster                                                  |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                                   |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                  |
| async_generators           | 463 ms                                                 | 394 ms: 1.17x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 64.3 ms: 1.17x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 58.9 ms: 1.16x faster                                                  |
| spectral_norm              | 115 ms                                                 | 98.9 ms: 1.16x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 72.6 ms: 1.13x faster                                                  |
| scimark_fft                | 382 ms                                                 | 340 ms: 1.12x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                   |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                   |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.11x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 19.2 ms: 1.11x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 144 ms: 1.11x faster                                                   |
| django_template            | 34.6 ms                                                | 31.3 ms: 1.10x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.37 ms: 1.10x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.29 ms: 1.10x faster                                                  |
| 2to3                       | 274 ms                                                 | 252 ms: 1.09x faster                                                   |
| pyflate                    | 482 ms                                                 | 444 ms: 1.09x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.66 ms: 1.08x faster                                                  |
| logging_silent             | 104 ns                                                 | 96.5 ns: 1.08x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 98.8 ms: 1.08x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 725 ms: 1.07x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.07x faster                                                 |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 84.1 ms: 1.06x faster                                                  |
| richards                   | 45.8 ms                                                | 43.3 ms: 1.06x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                  |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                   |
| richards_super             | 51.5 ms                                                | 49.4 ms: 1.04x faster                                                  |
| sympy_expand               | 478 ms                                                 | 459 ms: 1.04x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.18 ms: 1.04x faster                                                  |
| nbody                      | 97.0 ms                                                | 93.8 ms: 1.03x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 313 us: 1.03x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                 |
| nqueens                    | 83.3 ms                                                | 82.3 ms: 1.01x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                  |
| fannkuch                   | 417 ms                                                 | 413 ms: 1.01x faster                                                   |
| generators                 | 31.2 ms                                                | 30.9 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                                  |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                   |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 878 us: 1.04x slower                                                   |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                  |
| telco                      | 7.10 ms                                                | 7.80 ms: 1.10x slower                                                  |
| coverage                   | 72.7 ms                                                | 84.6 ms: 1.16x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 8.18 ms: 1.18x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.98 ms: 1.31x slower                                                  |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 83.3 ms: 3.47x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (2): regex_v8, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250401-3.14.0a6+-1a9d4a1/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.129x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.11x