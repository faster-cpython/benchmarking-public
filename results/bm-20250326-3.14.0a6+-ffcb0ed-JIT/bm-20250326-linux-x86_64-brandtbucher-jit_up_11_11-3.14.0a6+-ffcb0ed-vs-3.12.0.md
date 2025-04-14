# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_11_11
- machine: linux-x86_64
- commit hash: ffcb0ed
- commit date: 2025-03-26
- overall geometric mean: 1.104x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 264 ms: 1.04x faster                                                 |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.83x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                 |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.76x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.50x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 501 ms: 1.45x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.8 ms: 1.29x faster                                                |
| nbody          | 97.0 ms                                                | 88.4 ms: 1.10x faster                                                |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.39 ms: 1.06x faster                                                |
| regex_v8       | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.86 sec: 1.25x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 80.4 ms: 1.11x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 56.4 ms: 1.09x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 98.6 ms: 1.08x faster                                                |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 327 us: 1.01x slower                                                 |
| json_loads           | 28.5 us                                                | 30.0 us: 1.05x slower                                                |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.20 ms: 1.18x slower                                                |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                |
| django_template | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.83x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                 |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.76x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.50x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 501 ms: 1.45x faster                                                 |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                |
| float                      | 84.7 ms                                                | 65.8 ms: 1.29x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.86 sec: 1.25x faster                                               |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.24x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.06 ms: 1.21x faster                                                |
| spectral_norm              | 115 ms                                                 | 95.2 ms: 1.21x faster                                                |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.17x faster                                                |
| logging_format             | 7.23 us                                                | 6.19 us: 1.17x faster                                                |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.67 us: 1.14x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 60.8 ms: 1.13x faster                                                |
| comprehensions             | 21.8 us                                                | 19.4 us: 1.12x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 80.4 ms: 1.11x faster                                                |
| chaos                      | 67.0 ms                                                | 60.5 ms: 1.11x faster                                                |
| async_generators           | 463 ms                                                 | 419 ms: 1.10x faster                                                 |
| richards                   | 45.8 ms                                                | 41.6 ms: 1.10x faster                                                |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                                 |
| nbody                      | 97.0 ms                                                | 88.4 ms: 1.10x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 56.4 ms: 1.09x faster                                                |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                 |
| pyflate                    | 482 ms                                                 | 441 ms: 1.09x faster                                                 |
| logging_silent             | 104 ns                                                 | 95.6 ns: 1.09x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.63 ms: 1.09x faster                                                |
| sqlalchemy_declarative     | 147 ms                                                 | 134 ms: 1.09x faster                                                 |
| richards_super             | 51.5 ms                                                | 47.2 ms: 1.09x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 69.1 ms: 1.09x faster                                                |
| generators                 | 31.2 ms                                                | 28.7 ms: 1.09x faster                                                |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 98.6 ms: 1.08x faster                                                |
| sympy_str                  | 300 ms                                                 | 277 ms: 1.08x faster                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.4 ms: 1.08x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                                 |
| go                         | 139 ms                                                 | 130 ms: 1.07x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 76.5 ms: 1.07x faster                                                |
| django_template            | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                |
| regex_effbot               | 3.61 ms                                                | 3.39 ms: 1.06x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 20.2 ms: 1.06x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.71 us: 1.04x faster                                                |
| 2to3                       | 274 ms                                                 | 264 ms: 1.04x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                               |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.03x faster                                               |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.01x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 768 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                 |
| sympy_expand               | 478 ms                                                 | 476 ms: 1.00x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 327 us: 1.01x slower                                                 |
| fannkuch                   | 417 ms                                                 | 426 ms: 1.02x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                |
| nqueens                    | 83.3 ms                                                | 86.1 ms: 1.03x slower                                                |
| coroutines                 | 23.2 ms                                                | 24.1 ms: 1.04x slower                                                |
| json_loads                 | 28.5 us                                                | 30.0 us: 1.05x slower                                                |
| bench_thread_pool          | 842 us                                                 | 886 us: 1.05x slower                                                 |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.82 ms: 1.06x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                |
| telco                      | 7.10 ms                                                | 7.93 ms: 1.12x slower                                                |
| coverage                   | 72.7 ms                                                | 85.7 ms: 1.18x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 8.20 ms: 1.18x slower                                                |
| gc_traversal               | 3.79 ms                                                | 5.01 ms: 1.32x slower                                                |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.69x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 83.2 ms: 3.46x slower                                                |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                         |

Benchmark hidden because not significant (4): asyncio_websockets, json, pycparser, pprint_pformat
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250326-3.14.0a6+-ffcb0ed-JIT/bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.104x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.11x