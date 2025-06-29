# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_12_11
- machine: linux-x86_64
- commit hash: af1f59b
- commit date: 2025-06-29
- overall geometric mean: 1.145x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 496 ms: 1.46x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                                |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.7 ms: 1.29x faster                                               |
| pidigits       | 187 ms                                                 | 193 ms: 1.03x slower                                                |
| nbody          | 97.0 ms                                                | 100 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.41 ms: 1.06x faster                                               |
| regex_dna      | 212 ms                                                 | 215 ms: 1.01x slower                                                |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.81 sec: 1.29x faster                                              |
| unpickle_pure_python | 230 us                                                 | 189 us: 1.22x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 79.7 ms: 1.12x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 55.4 ms: 1.11x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 99.0 ms: 1.08x faster                                               |
| json_loads           | 28.5 us                                                | 28.1 us: 1.02x faster                                               |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                               |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.95 ms: 1.00x slower                                               |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                               |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.6 ms: 1.12x faster                                               |
| django_template | 34.6 ms                                                | 32.9 ms: 1.05x faster                                               |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                              |
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                |
| richards                   | 45.8 ms                                                | 30.3 ms: 1.51x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 496 ms: 1.46x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                                |
| richards_super             | 51.5 ms                                                | 35.7 ms: 1.44x faster                                               |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                               |
| comprehensions             | 21.8 us                                                | 16.2 us: 1.34x faster                                               |
| spectral_norm              | 115 ms                                                 | 88.7 ms: 1.29x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.81 sec: 1.29x faster                                              |
| float                      | 84.7 ms                                                | 65.7 ms: 1.29x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.03 ms: 1.23x faster                                               |
| scimark_fft                | 382 ms                                                 | 311 ms: 1.23x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 189 us: 1.22x faster                                                |
| go                         | 139 ms                                                 | 115 ms: 1.21x faster                                                |
| pyflate                    | 482 ms                                                 | 403 ms: 1.20x faster                                                |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                               |
| dulwich_log                | 68.5 ms                                                | 59.3 ms: 1.15x faster                                               |
| logging_format             | 7.23 us                                                | 6.27 us: 1.15x faster                                               |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                                |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 66.0 ms: 1.14x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                |
| mako                       | 11.9 ms                                                | 10.6 ms: 1.12x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 79.7 ms: 1.12x faster                                               |
| xml_etree_process          | 61.7 ms                                                | 55.4 ms: 1.11x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 19.3 ms: 1.11x faster                                               |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                |
| pathlib                    | 19.3 ms                                                | 17.5 ms: 1.10x faster                                               |
| chaos                      | 67.0 ms                                                | 61.6 ms: 1.09x faster                                               |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 75.7 ms: 1.08x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 99.0 ms: 1.08x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 720 ms: 1.08x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.08x faster                                              |
| async_generators           | 463 ms                                                 | 430 ms: 1.08x faster                                                |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                |
| regex_effbot               | 3.61 ms                                                | 3.41 ms: 1.06x faster                                               |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                |
| django_template            | 34.6 ms                                                | 32.9 ms: 1.05x faster                                               |
| fannkuch                   | 417 ms                                                 | 397 ms: 1.05x faster                                                |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                              |
| hexiom                     | 6.41 ms                                                | 6.17 ms: 1.04x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.87 ms: 1.04x faster                                               |
| sympy_expand               | 478 ms                                                 | 465 ms: 1.03x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                              |
| generators                 | 31.2 ms                                                | 30.6 ms: 1.02x faster                                               |
| json_loads                 | 28.5 us                                                | 28.1 us: 1.02x faster                                               |
| nqueens                    | 83.3 ms                                                | 82.1 ms: 1.01x faster                                               |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                               |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                |
| json                       | 5.26 ms                                                | 5.21 ms: 1.01x faster                                               |
| python_startup_no_site     | 6.94 ms                                                | 6.95 ms: 1.00x slower                                               |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.01x slower                                                |
| pidigits                   | 187 ms                                                 | 193 ms: 1.03x slower                                                |
| nbody                      | 97.0 ms                                                | 100 ms: 1.03x slower                                                |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                               |
| coroutines                 | 23.2 ms                                                | 24.7 ms: 1.07x slower                                               |
| telco                      | 7.10 ms                                                | 7.74 ms: 1.09x slower                                               |
| coverage                   | 72.7 ms                                                | 88.1 ms: 1.21x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.76 ms: 1.26x slower                                               |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.57 ms: 1.74x slower                                               |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                        |
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250629-3.15.0a0-af1f59b-JIT/bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.145x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.15x