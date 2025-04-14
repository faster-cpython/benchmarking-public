# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_build_and_iter
- machine: linux-x86_64
- commit hash: 488d5b8
- commit date: 2025-03-27
- overall geometric mean: 1.110x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 264 ms: 1.04x faster                                                       |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 623 ms: 1.90x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 623 ms: 1.85x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                       |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.7 ms: 1.29x faster                                                      |
| nbody          | 97.0 ms                                                | 88.4 ms: 1.10x faster                                                      |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.20 ms: 1.13x faster                                                      |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                       |
| regex_v8       | 23.1 ms                                                | 23.7 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.87 sec: 1.25x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.14x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 80.7 ms: 1.10x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 56.6 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 97.9 ms: 1.09x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                       |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                                      |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                               |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.24 ms: 1.19x slower                                                      |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                      |
| django_template | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 623 ms: 1.90x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 623 ms: 1.85x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                       |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                                       |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 29.2 us: 1.39x faster                                                      |
| float                      | 84.7 ms                                                | 65.7 ms: 1.29x faster                                                      |
| richards                   | 45.8 ms                                                | 36.2 ms: 1.27x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.87 sec: 1.25x faster                                                     |
| richards_super             | 51.5 ms                                                | 41.6 ms: 1.24x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.24x faster                                                      |
| scimark_fft                | 382 ms                                                 | 314 ms: 1.22x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.07 ms: 1.21x faster                                                      |
| spectral_norm              | 115 ms                                                 | 95.2 ms: 1.21x faster                                                      |
| comprehensions             | 21.8 us                                                | 18.8 us: 1.16x faster                                                      |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                       |
| logging_format             | 7.23 us                                                | 6.27 us: 1.15x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.15x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                                      |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.14x faster                                                       |
| pyflate                    | 482 ms                                                 | 427 ms: 1.13x faster                                                       |
| regex_effbot               | 3.61 ms                                                | 3.20 ms: 1.13x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 60.9 ms: 1.12x faster                                                      |
| async_generators           | 463 ms                                                 | 412 ms: 1.12x faster                                                       |
| chaos                      | 67.0 ms                                                | 59.8 ms: 1.12x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 80.7 ms: 1.10x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 153 ms: 1.10x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 68.3 ms: 1.10x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 134 ms: 1.10x faster                                                       |
| nbody                      | 97.0 ms                                                | 88.4 ms: 1.10x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 56.6 ms: 1.09x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 97.9 ms: 1.09x faster                                                      |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                                      |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                                       |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.67 ms: 1.08x faster                                                      |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.3 ms: 1.08x faster                                                      |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                       |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                       |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.07x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.49 sec: 1.06x faster                                                     |
| logging_silent             | 104 ns                                                 | 100 ns: 1.04x faster                                                       |
| 2to3                       | 274 ms                                                 | 264 ms: 1.04x faster                                                       |
| sqlite_synth               | 2.83 us                                                | 2.73 us: 1.04x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 79.3 ms: 1.03x faster                                                      |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                     |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                     |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                       |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| sympy_expand               | 478 ms                                                 | 476 ms: 1.00x faster                                                       |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                       |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                                      |
| fannkuch                   | 417 ms                                                 | 420 ms: 1.01x slower                                                       |
| nqueens                    | 83.3 ms                                                | 84.4 ms: 1.01x slower                                                      |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 23.7 ms: 1.03x slower                                                      |
| pprint_safe_repr           | 776 ms                                                 | 804 ms: 1.04x slower                                                       |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.64 sec: 1.04x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 882 us: 1.05x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                       |
| hexiom                     | 6.41 ms                                                | 6.88 ms: 1.07x slower                                                      |
| telco                      | 7.10 ms                                                | 7.82 ms: 1.10x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 8.24 ms: 1.19x slower                                                      |
| coverage                   | 72.7 ms                                                | 88.9 ms: 1.22x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 4.83 ms: 1.27x slower                                                      |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.68x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 83.5 ms: 3.48x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                               |

Benchmark hidden because not significant (3): scimark_lu, pickle_pure_python, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250327-3.14.0a6+-488d5b8-JIT/bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.110x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.12x