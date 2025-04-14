# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_12_10
- machine: linux-x86_64
- commit hash: f2d447f
- commit date: 2025-03-26
- overall geometric mean: 1.110x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_10-3.14.0a6+-f2d447f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.04x faster                                                 |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_10-3.14.0a6+-f2d447f |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 624 ms: 1.85x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                 |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_10-3.14.0a6+-f2d447f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.9 ms: 1.29x faster                                                |
| nbody          | 97.0 ms                                                | 87.7 ms: 1.11x faster                                                |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_10-3.14.0a6+-f2d447f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.13 ms: 1.16x faster                                                |
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                 |
| regex_dna      | 212 ms                                                 | 209 ms: 1.01x faster                                                 |
| regex_v8       | 23.1 ms                                                | 23.0 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.08x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_10-3.14.0a6+-f2d447f |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.87 sec: 1.25x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 56.6 ms: 1.09x faster                                                |
| unpickle_pure_python | 230 us                                                 | 212 us: 1.08x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 98.8 ms: 1.08x faster                                                |
| json_loads           | 28.5 us                                                | 30.0 us: 1.05x slower                                                |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                         |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_10-3.14.0a6+-f2d447f |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.20 ms: 1.18x slower                                                |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_10-3.14.0a6+-f2d447f |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                |
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_10-3.14.0a6+-f2d447f |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 624 ms: 1.85x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                 |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                 |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 30.1 us: 1.35x faster                                                |
| float                      | 84.7 ms                                                | 65.9 ms: 1.29x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.87 sec: 1.25x faster                                               |
| richards                   | 45.8 ms                                                | 36.9 ms: 1.24x faster                                                |
| scimark_fft                | 382 ms                                                 | 314 ms: 1.22x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.76 us: 1.21x faster                                                |
| richards_super             | 51.5 ms                                                | 42.5 ms: 1.21x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.07 ms: 1.21x faster                                                |
| spectral_norm              | 115 ms                                                 | 95.8 ms: 1.20x faster                                                |
| logging_format             | 7.23 us                                                | 6.19 us: 1.17x faster                                                |
| raytrace                   | 312 ms                                                 | 268 ms: 1.16x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.58 us: 1.16x faster                                                |
| comprehensions             | 21.8 us                                                | 18.8 us: 1.16x faster                                                |
| regex_effbot               | 3.61 ms                                                | 3.13 ms: 1.16x faster                                                |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 60.7 ms: 1.13x faster                                                |
| chaos                      | 67.0 ms                                                | 60.4 ms: 1.11x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                |
| sympy_sum                  | 169 ms                                                 | 153 ms: 1.11x faster                                                 |
| nbody                      | 97.0 ms                                                | 87.7 ms: 1.11x faster                                                |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.11x faster                                                 |
| async_generators           | 463 ms                                                 | 421 ms: 1.10x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 56.6 ms: 1.09x faster                                                |
| django_template            | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                |
| sympy_str                  | 300 ms                                                 | 276 ms: 1.09x faster                                                 |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 212 us: 1.08x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 69.5 ms: 1.08x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.3 ms: 1.08x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 98.8 ms: 1.08x faster                                                |
| generators                 | 31.2 ms                                                | 29.0 ms: 1.08x faster                                                |
| logging_silent             | 104 ns                                                 | 97.5 ns: 1.07x faster                                                |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.07x faster                                                |
| go                         | 139 ms                                                 | 132 ms: 1.06x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.79 ms: 1.06x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.70 us: 1.05x faster                                                |
| pyflate                    | 482 ms                                                 | 459 ms: 1.05x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 78.1 ms: 1.05x faster                                                |
| 2to3                       | 274 ms                                                 | 262 ms: 1.04x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.04x faster                                               |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                               |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                               |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.01x faster                                                 |
| regex_dna                  | 212 ms                                                 | 209 ms: 1.01x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 767 ms: 1.01x faster                                                 |
| sympy_expand               | 478 ms                                                 | 473 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                 |
| regex_v8                   | 23.1 ms                                                | 23.0 ms: 1.00x faster                                                |
| json                       | 5.26 ms                                                | 5.34 ms: 1.02x slower                                                |
| pprint_pformat             | 1.57 sec                                               | 1.59 sec: 1.02x slower                                               |
| fannkuch                   | 417 ms                                                 | 425 ms: 1.02x slower                                                 |
| nqueens                    | 83.3 ms                                                | 85.8 ms: 1.03x slower                                                |
| coroutines                 | 23.2 ms                                                | 24.0 ms: 1.04x slower                                                |
| bench_thread_pool          | 842 us                                                 | 881 us: 1.05x slower                                                 |
| json_loads                 | 28.5 us                                                | 30.0 us: 1.05x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.87 ms: 1.07x slower                                                |
| telco                      | 7.10 ms                                                | 7.80 ms: 1.10x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 8.20 ms: 1.18x slower                                                |
| coverage                   | 72.7 ms                                                | 87.3 ms: 1.20x slower                                                |
| gc_traversal               | 3.79 ms                                                | 4.81 ms: 1.27x slower                                                |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 83.1 ms: 3.46x slower                                                |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                         |

Benchmark hidden because not significant (2): asyncio_websockets, pickle_pure_python
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250326-3.14.0a6+-f2d447f-JIT/bm-20250326-linux-x86_64-brandtbucher-jit_up_12_10-3.14.0a6+-f2d447f.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.110x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.12x