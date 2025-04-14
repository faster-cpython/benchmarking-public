# Results vs. 3.12.0

- fork: python
- ref: e0bc9d2a0c448cf46df2
- machine: linux-x86_64
- commit hash: e0bc9d2
- commit date: 2025-03-11
- overall geometric mean: 1.119x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.05x faster                                                   |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                                   |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 319 ms: 1.81x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.80x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 64.6 ms: 1.31x faster                                                  |
| nbody          | 97.0 ms                                                | 87.5 ms: 1.11x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.50 ms: 1.03x faster                                                  |
| regex_v8       | 23.1 ms                                                | 23.5 ms: 1.02x slower                                                  |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.83 sec: 1.27x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 79.0 ms: 1.13x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 55.2 ms: 1.12x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 97.6 ms: 1.09x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 212 us: 1.09x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.02x faster                                                   |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.21 ms: 1.18x slower                                                  |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.2 ms: 1.11x faster                                                  |
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                                   |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 319 ms: 1.81x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.80x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                                   |
| deepcopy                   | 371 us                                                 | 256 us: 1.45x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                                  |
| float                      | 84.7 ms                                                | 64.6 ms: 1.31x faster                                                  |
| richards                   | 45.8 ms                                                | 35.5 ms: 1.29x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.83 sec: 1.27x faster                                                 |
| richards_super             | 51.5 ms                                                | 40.8 ms: 1.26x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                                  |
| scimark_fft                | 382 ms                                                 | 308 ms: 1.24x faster                                                   |
| spectral_norm              | 115 ms                                                 | 93.2 ms: 1.23x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.02 ms: 1.23x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.18x faster                                                  |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                   |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                   |
| logging_format             | 7.23 us                                                | 6.17 us: 1.17x faster                                                  |
| comprehensions             | 21.8 us                                                | 18.8 us: 1.16x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.58 us: 1.16x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                   |
| chaos                      | 67.0 ms                                                | 58.9 ms: 1.14x faster                                                  |
| generators                 | 31.2 ms                                                | 27.5 ms: 1.13x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 60.7 ms: 1.13x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 79.0 ms: 1.13x faster                                                  |
| async_generators           | 463 ms                                                 | 411 ms: 1.13x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 67.2 ms: 1.12x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 55.2 ms: 1.12x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                                   |
| django_template            | 34.6 ms                                                | 31.2 ms: 1.11x faster                                                  |
| nbody                      | 97.0 ms                                                | 87.5 ms: 1.11x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                                  |
| logging_silent             | 104 ns                                                 | 94.7 ns: 1.10x faster                                                  |
| go                         | 139 ms                                                 | 127 ms: 1.10x faster                                                   |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 97.6 ms: 1.09x faster                                                  |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 212 us: 1.09x faster                                                   |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                  |
| pyflate                    | 482 ms                                                 | 447 ms: 1.08x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.70 ms: 1.08x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.46 sec: 1.07x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 20.2 ms: 1.06x faster                                                  |
| 2to3                       | 274 ms                                                 | 260 ms: 1.05x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.72 us: 1.04x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 745 ms: 1.04x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 79.3 ms: 1.03x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.50 ms: 1.03x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                 |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                                   |
| sympy_expand               | 478 ms                                                 | 469 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.02x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| fannkuch                   | 417 ms                                                 | 421 ms: 1.01x slower                                                   |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                                  |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.02x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 23.5 ms: 1.02x slower                                                  |
| hexiom                     | 6.41 ms                                                | 6.64 ms: 1.04x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 876 us: 1.04x slower                                                   |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                   |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                  |
| telco                      | 7.10 ms                                                | 7.92 ms: 1.12x slower                                                  |
| coverage                   | 72.7 ms                                                | 85.4 ms: 1.17x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 8.21 ms: 1.18x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 5.05 ms: 1.33x slower                                                  |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.69x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 83.2 ms: 3.47x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, nqueens
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250311-3.14.0a5+-e0bc9d2-JIT/bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.119x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x