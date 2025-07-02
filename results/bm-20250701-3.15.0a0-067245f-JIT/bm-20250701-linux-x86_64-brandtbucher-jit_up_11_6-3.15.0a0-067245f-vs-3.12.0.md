# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_11_6
- machine: linux-x86_64
- commit hash: 067245f
- commit date: 2025-07-01
- overall geometric mean: 1.143x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                               |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.05x faster                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 639 ms: 1.85x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.84x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                               |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.80x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                               |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.6 ms: 1.29x faster                                              |
| nbody          | 97.0 ms                                                | 93.6 ms: 1.04x faster                                              |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.10x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.43 ms: 1.05x faster                                              |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                               |
| regex_v8       | 23.1 ms                                                | 23.8 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.82 sec: 1.28x faster                                             |
| unpickle_pure_python | 230 us                                                 | 190 us: 1.21x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.13x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 80.2 ms: 1.11x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 55.8 ms: 1.11x faster                                              |
| xml_etree_iterparse  | 107 ms                                                 | 99.3 ms: 1.08x faster                                              |
| json_loads           | 28.5 us                                                | 28.0 us: 1.02x faster                                              |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                              |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                       |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.95 ms: 1.00x slower                                              |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                              |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.4 ms: 1.14x faster                                              |
| django_template | 34.6 ms                                                | 32.4 ms: 1.07x faster                                              |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                             |
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 639 ms: 1.85x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.84x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                               |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.80x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                               |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.39x faster                                              |
| richards                   | 45.8 ms                                                | 33.7 ms: 1.36x faster                                              |
| comprehensions             | 21.8 us                                                | 16.3 us: 1.34x faster                                              |
| richards_super             | 51.5 ms                                                | 38.9 ms: 1.32x faster                                              |
| float                      | 84.7 ms                                                | 65.6 ms: 1.29x faster                                              |
| tomli_loads                | 2.33 sec                                               | 1.82 sec: 1.28x faster                                             |
| spectral_norm              | 115 ms                                                 | 90.0 ms: 1.28x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                              |
| go                         | 139 ms                                                 | 114 ms: 1.23x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.04 ms: 1.22x faster                                              |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 190 us: 1.21x faster                                               |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                               |
| logging_simple             | 6.46 us                                                | 5.53 us: 1.17x faster                                              |
| logging_format             | 7.23 us                                                | 6.21 us: 1.16x faster                                              |
| pyflate                    | 482 ms                                                 | 415 ms: 1.16x faster                                               |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 65.0 ms: 1.16x faster                                              |
| dulwich_log                | 68.5 ms                                                | 60.0 ms: 1.14x faster                                              |
| mako                       | 11.9 ms                                                | 10.4 ms: 1.14x faster                                              |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.13x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 72.8 ms: 1.12x faster                                              |
| pprint_safe_repr           | 776 ms                                                 | 691 ms: 1.12x faster                                               |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                               |
| pathlib                    | 19.3 ms                                                | 17.2 ms: 1.12x faster                                              |
| xml_etree_generate         | 89.2 ms                                                | 80.2 ms: 1.11x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 55.8 ms: 1.11x faster                                              |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                              |
| pprint_pformat             | 1.57 sec                                               | 1.43 sec: 1.10x faster                                             |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.10x faster                                               |
| async_generators           | 463 ms                                                 | 424 ms: 1.09x faster                                               |
| chaos                      | 67.0 ms                                                | 61.5 ms: 1.09x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 99.3 ms: 1.08x faster                                              |
| django_template            | 34.6 ms                                                | 32.4 ms: 1.07x faster                                              |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.43 ms: 1.05x faster                                              |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                               |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.05x faster                                             |
| fannkuch                   | 417 ms                                                 | 401 ms: 1.04x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.87 ms: 1.04x faster                                              |
| nbody                      | 97.0 ms                                                | 93.6 ms: 1.04x faster                                              |
| generators                 | 31.2 ms                                                | 30.2 ms: 1.03x faster                                              |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                             |
| hexiom                     | 6.41 ms                                                | 6.25 ms: 1.03x faster                                              |
| sympy_expand               | 478 ms                                                 | 467 ms: 1.02x faster                                               |
| json_loads                 | 28.5 us                                                | 28.0 us: 1.02x faster                                              |
| json                       | 5.26 ms                                                | 5.17 ms: 1.02x faster                                              |
| nqueens                    | 83.3 ms                                                | 82.4 ms: 1.01x faster                                              |
| python_startup_no_site     | 6.94 ms                                                | 6.95 ms: 1.00x slower                                              |
| logging_silent             | 104 ns                                                 | 105 ns: 1.00x slower                                               |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                               |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.02x slower                                               |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                               |
| regex_v8                   | 23.1 ms                                                | 23.8 ms: 1.03x slower                                              |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                              |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                               |
| telco                      | 7.10 ms                                                | 7.75 ms: 1.09x slower                                              |
| coroutines                 | 23.2 ms                                                | 25.4 ms: 1.10x slower                                              |
| coverage                   | 72.7 ms                                                | 87.4 ms: 1.20x slower                                              |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                              |
| gc_traversal               | 3.79 ms                                                | 4.87 ms: 1.28x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 2.57 ms: 1.74x slower                                              |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                       |

Benchmark hidden because not significant (3): sqlite_synth, pickle_pure_python, asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250701-3.15.0a0-067245f-JIT/bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.143x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.15x