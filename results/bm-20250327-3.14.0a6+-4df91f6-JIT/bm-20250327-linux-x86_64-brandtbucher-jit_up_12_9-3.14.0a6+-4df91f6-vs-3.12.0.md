# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_12_9
- machine: linux-x86_64
- commit hash: 4df91f6
- commit date: 2025-03-27
- overall geometric mean: 1.108x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 265 ms: 1.03x faster                                                |
| docutils       | 2.77 sec                                               | 2.72 sec: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 618 ms: 1.91x faster                                                |
| async_tree_io              | 1.16 sec                                               | 622 ms: 1.86x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.83x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 475 ms: 1.53x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                                |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.1 ms: 1.30x faster                                               |
| nbody          | 97.0 ms                                                | 86.8 ms: 1.12x faster                                               |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.14x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.51 ms: 1.03x faster                                               |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.87 sec: 1.25x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.14x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 81.0 ms: 1.10x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 97.5 ms: 1.09x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 57.1 ms: 1.08x faster                                               |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.08x faster                                                |
| pickle_pure_python   | 324 us                                                 | 330 us: 1.02x slower                                                |
| json_loads           | 28.5 us                                                | 30.0 us: 1.05x slower                                               |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.11x slower                                               |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.19 ms: 1.18x slower                                               |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                               |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.0 ms: 1.08x faster                                               |
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                               |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 618 ms: 1.91x faster                                                |
| async_tree_io              | 1.16 sec                                               | 622 ms: 1.86x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.83x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 475 ms: 1.53x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                                |
| deepcopy                   | 371 us                                                 | 260 us: 1.42x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.40x faster                                               |
| float                      | 84.7 ms                                                | 65.1 ms: 1.30x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.87 sec: 1.25x faster                                              |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                |
| richards_super             | 51.5 ms                                                | 41.9 ms: 1.23x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.22x faster                                               |
| richards                   | 45.8 ms                                                | 37.5 ms: 1.22x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.06 ms: 1.21x faster                                               |
| spectral_norm              | 115 ms                                                 | 95.5 ms: 1.20x faster                                               |
| raytrace                   | 312 ms                                                 | 268 ms: 1.17x faster                                                |
| comprehensions             | 21.8 us                                                | 18.7 us: 1.16x faster                                               |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                               |
| logging_format             | 7.23 us                                                | 6.25 us: 1.16x faster                                               |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.14x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.14x faster                                                |
| dulwich_log                | 68.5 ms                                                | 60.7 ms: 1.13x faster                                               |
| nbody                      | 97.0 ms                                                | 86.8 ms: 1.12x faster                                               |
| chaos                      | 67.0 ms                                                | 60.1 ms: 1.11x faster                                               |
| async_generators           | 463 ms                                                 | 417 ms: 1.11x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 81.0 ms: 1.10x faster                                               |
| sqlalchemy_declarative     | 147 ms                                                 | 134 ms: 1.10x faster                                                |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 97.5 ms: 1.09x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 68.8 ms: 1.09x faster                                               |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                               |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                |
| sympy_str                  | 300 ms                                                 | 276 ms: 1.08x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 57.1 ms: 1.08x faster                                               |
| django_template            | 34.6 ms                                                | 32.0 ms: 1.08x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.68 ms: 1.08x faster                                               |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.4 ms: 1.08x faster                                               |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                               |
| pyflate                    | 482 ms                                                 | 448 ms: 1.08x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.08x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.06x faster                                               |
| logging_silent             | 104 ns                                                 | 99.5 ns: 1.05x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.70 us: 1.05x faster                                               |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                              |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 79.0 ms: 1.04x faster                                               |
| 2to3                       | 274 ms                                                 | 265 ms: 1.03x faster                                                |
| regex_effbot               | 3.61 ms                                                | 3.51 ms: 1.03x faster                                               |
| docutils                   | 2.77 sec                                               | 2.72 sec: 1.02x faster                                              |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                |
| sympy_expand               | 478 ms                                                 | 474 ms: 1.01x faster                                                |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.00x faster                                                |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                |
| fannkuch                   | 417 ms                                                 | 422 ms: 1.01x slower                                                |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                               |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                              |
| pickle_pure_python         | 324 us                                                 | 330 us: 1.02x slower                                                |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                |
| nqueens                    | 83.3 ms                                                | 87.1 ms: 1.05x slower                                               |
| bench_thread_pool          | 842 us                                                 | 883 us: 1.05x slower                                                |
| json_loads                 | 28.5 us                                                | 30.0 us: 1.05x slower                                               |
| coroutines                 | 23.2 ms                                                | 24.6 ms: 1.06x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.83 ms: 1.06x slower                                               |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                               |
| telco                      | 7.10 ms                                                | 7.95 ms: 1.12x slower                                               |
| coverage                   | 72.7 ms                                                | 85.0 ms: 1.17x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 8.19 ms: 1.18x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.81 ms: 1.27x slower                                               |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.8 ms: 3.45x slower                                               |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                        |

Benchmark hidden because not significant (3): pprint_safe_repr, regex_v8, pprint_pformat
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250327-3.14.0a6+-4df91f6-JIT/bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x