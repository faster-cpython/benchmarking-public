# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_8_6
- machine: linux-x86_64
- commit hash: 008b481
- commit date: 2025-03-31
- overall geometric mean: 1.107x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 270 ms: 1.02x faster                                               |
| docutils       | 2.77 sec                                               | 2.72 sec: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                               |
| async_tree_io              | 1.16 sec                                               | 618 ms: 1.87x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.83x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                               |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                               |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 66.3 ms: 1.28x faster                                              |
| nbody          | 97.0 ms                                                | 88.6 ms: 1.10x faster                                              |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.12x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.23 ms: 1.12x faster                                              |
| regex_v8       | 23.1 ms                                                | 22.8 ms: 1.02x faster                                              |
| regex_dna      | 212 ms                                                 | 213 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.87 sec: 1.25x faster                                             |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 80.9 ms: 1.10x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 56.8 ms: 1.09x faster                                              |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.09x faster                                              |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                               |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                              |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.11x slower                                              |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                       |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.18 ms: 1.18x slower                                              |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                              |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.1 ms: 1.08x faster                                              |
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                              |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                               |
| async_tree_io              | 1.16 sec                                               | 618 ms: 1.87x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.83x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                               |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                               |
| deepcopy                   | 371 us                                                 | 265 us: 1.40x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 29.2 us: 1.40x faster                                              |
| float                      | 84.7 ms                                                | 66.3 ms: 1.28x faster                                              |
| tomli_loads                | 2.33 sec                                               | 1.87 sec: 1.25x faster                                             |
| richards                   | 45.8 ms                                                | 37.4 ms: 1.23x faster                                              |
| deltablue                  | 3.72 ms                                                | 3.05 ms: 1.22x faster                                              |
| scimark_fft                | 382 ms                                                 | 315 ms: 1.21x faster                                               |
| spectral_norm              | 115 ms                                                 | 95.5 ms: 1.20x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.79 us: 1.20x faster                                              |
| richards_super             | 51.5 ms                                                | 43.0 ms: 1.20x faster                                              |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                              |
| logging_simple             | 6.46 us                                                | 5.51 us: 1.17x faster                                              |
| comprehensions             | 21.8 us                                                | 18.6 us: 1.17x faster                                              |
| raytrace                   | 312 ms                                                 | 268 ms: 1.16x faster                                               |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                              |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                               |
| dulwich_log                | 68.5 ms                                                | 60.4 ms: 1.13x faster                                              |
| chaos                      | 67.0 ms                                                | 59.7 ms: 1.12x faster                                              |
| regex_effbot               | 3.61 ms                                                | 3.23 ms: 1.12x faster                                              |
| async_generators           | 463 ms                                                 | 420 ms: 1.10x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 80.9 ms: 1.10x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 68.5 ms: 1.10x faster                                              |
| nbody                      | 97.0 ms                                                | 88.6 ms: 1.10x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 56.8 ms: 1.09x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.09x faster                                              |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.66 ms: 1.08x faster                                              |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.08x faster                                               |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                               |
| logging_silent             | 104 ns                                                 | 96.8 ns: 1.08x faster                                              |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.08x faster                                              |
| crypto_pyaes               | 81.9 ms                                                | 76.2 ms: 1.07x faster                                              |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.4 ms: 1.07x faster                                              |
| sympy_str                  | 300 ms                                                 | 280 ms: 1.07x faster                                               |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                              |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                               |
| generators                 | 31.2 ms                                                | 29.4 ms: 1.06x faster                                              |
| pyflate                    | 482 ms                                                 | 460 ms: 1.05x faster                                               |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.05x faster                                             |
| sqlite_synth               | 2.83 us                                                | 2.72 us: 1.04x faster                                              |
| sympy_integrate            | 21.4 ms                                                | 20.5 ms: 1.04x faster                                              |
| sqlalchemy_declarative     | 147 ms                                                 | 141 ms: 1.04x faster                                               |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.04x faster                                               |
| docutils                   | 2.77 sec                                               | 2.72 sec: 1.02x faster                                             |
| regex_v8                   | 23.1 ms                                                | 22.8 ms: 1.02x faster                                              |
| 2to3                       | 274 ms                                                 | 270 ms: 1.02x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 766 ms: 1.01x faster                                               |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                               |
| regex_dna                  | 212 ms                                                 | 213 ms: 1.00x slower                                               |
| sympy_expand               | 478 ms                                                 | 480 ms: 1.00x slower                                               |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.02x slower                                               |
| nqueens                    | 83.3 ms                                                | 84.9 ms: 1.02x slower                                              |
| fannkuch                   | 417 ms                                                 | 428 ms: 1.03x slower                                               |
| pprint_pformat             | 1.57 sec                                               | 1.61 sec: 1.03x slower                                             |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                              |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                              |
| bench_thread_pool          | 842 us                                                 | 897 us: 1.07x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                               |
| hexiom                     | 6.41 ms                                                | 6.94 ms: 1.08x slower                                              |
| telco                      | 7.10 ms                                                | 7.89 ms: 1.11x slower                                              |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                              |
| python_startup_no_site     | 6.94 ms                                                | 8.18 ms: 1.18x slower                                              |
| coverage                   | 72.7 ms                                                | 86.1 ms: 1.18x slower                                              |
| gc_traversal               | 3.79 ms                                                | 5.00 ms: 1.32x slower                                              |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 2.50 ms: 1.69x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 83.8 ms: 3.49x slower                                              |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                       |

Benchmark hidden because not significant (4): pycparser, asyncio_websockets, pickle_pure_python, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250331-3.14.0a6+-008b481-JIT/bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.107x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.12x