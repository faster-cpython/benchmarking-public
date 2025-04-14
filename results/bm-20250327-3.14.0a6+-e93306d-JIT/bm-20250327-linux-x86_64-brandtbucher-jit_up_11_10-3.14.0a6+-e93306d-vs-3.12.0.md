# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_11_10
- machine: linux-x86_64
- commit hash: e93306d
- commit date: 2025-03-27
- overall geometric mean: 1.109x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 265 ms: 1.04x faster                                                 |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.87x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                 |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.52x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.8 ms: 1.29x faster                                                |
| nbody          | 97.0 ms                                                | 86.4 ms: 1.12x faster                                                |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.47 ms: 1.04x faster                                                |
| regex_v8       | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.86 sec: 1.25x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 80.3 ms: 1.11x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 56.8 ms: 1.09x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                                |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                                 |
| json_loads           | 28.5 us                                                | 30.0 us: 1.05x slower                                                |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                         |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.22 ms: 1.18x slower                                                |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                |
| django_template | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.87x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                 |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.52x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                                 |
| deepcopy                   | 371 us                                                 | 262 us: 1.41x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.40x faster                                                |
| richards                   | 45.8 ms                                                | 35.3 ms: 1.30x faster                                                |
| float                      | 84.7 ms                                                | 65.8 ms: 1.29x faster                                                |
| richards_super             | 51.5 ms                                                | 40.6 ms: 1.27x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.86 sec: 1.25x faster                                               |
| spectral_norm              | 115 ms                                                 | 92.6 ms: 1.24x faster                                                |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.08 ms: 1.21x faster                                                |
| raytrace                   | 312 ms                                                 | 268 ms: 1.16x faster                                                 |
| logging_format             | 7.23 us                                                | 6.22 us: 1.16x faster                                                |
| comprehensions             | 21.8 us                                                | 18.8 us: 1.16x faster                                                |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                                |
| logging_simple             | 6.46 us                                                | 5.66 us: 1.14x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 60.5 ms: 1.13x faster                                                |
| nbody                      | 97.0 ms                                                | 86.4 ms: 1.12x faster                                                |
| chaos                      | 67.0 ms                                                | 59.9 ms: 1.12x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 80.3 ms: 1.11x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 68.1 ms: 1.10x faster                                                |
| async_generators           | 463 ms                                                 | 420 ms: 1.10x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                 |
| sqlalchemy_declarative     | 147 ms                                                 | 135 ms: 1.09x faster                                                 |
| mako                       | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 56.8 ms: 1.09x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.66 ms: 1.09x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                                |
| django_template            | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                |
| sympy_str                  | 300 ms                                                 | 278 ms: 1.08x faster                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.4 ms: 1.08x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                                 |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                 |
| pyflate                    | 482 ms                                                 | 453 ms: 1.06x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 77.2 ms: 1.06x faster                                                |
| generators                 | 31.2 ms                                                | 29.5 ms: 1.06x faster                                                |
| mdp                        | 2.63 sec                                               | 2.49 sec: 1.06x faster                                               |
| go                         | 139 ms                                                 | 132 ms: 1.06x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 20.3 ms: 1.05x faster                                                |
| logging_silent             | 104 ns                                                 | 100 ns: 1.04x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.47 ms: 1.04x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.73 us: 1.04x faster                                                |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                 |
| 2to3                       | 274 ms                                                 | 265 ms: 1.04x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.03x faster                                               |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                 |
| regex_v8                   | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                |
| fannkuch                   | 417 ms                                                 | 422 ms: 1.01x slower                                                 |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                                |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.02x slower                                                 |
| nqueens                    | 83.3 ms                                                | 86.5 ms: 1.04x slower                                                |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 883 us: 1.05x slower                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.65 sec: 1.05x slower                                               |
| json_loads                 | 28.5 us                                                | 30.0 us: 1.05x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.93 ms: 1.08x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                |
| telco                      | 7.10 ms                                                | 7.95 ms: 1.12x slower                                                |
| coverage                   | 72.7 ms                                                | 85.8 ms: 1.18x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 8.22 ms: 1.18x slower                                                |
| gc_traversal               | 3.79 ms                                                | 4.61 ms: 1.21x slower                                                |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 83.4 ms: 3.47x slower                                                |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                         |

Benchmark hidden because not significant (6): pycparser, coroutines, asyncio_websockets, sympy_expand, pprint_safe_repr, pickle_pure_python
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250327-3.14.0a6+-e93306d-JIT/bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.109x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.12x