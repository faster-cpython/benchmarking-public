# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_warmup_2048
- machine: linux-x86_64
- commit hash: 004e970
- commit date: 2025-03-03
- overall geometric mean: 1.111x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                    |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 626 ms: 1.89x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 320 ms: 1.80x faster                                                    |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.77x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 331 ms: 1.74x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 486 ms: 1.49x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.6 ms: 1.22x faster                                                   |
| nbody          | 97.0 ms                                                | 94.1 ms: 1.03x faster                                                   |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.35 ms: 1.08x faster                                                   |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                    |
| regex_v8       | 23.1 ms                                                | 25.6 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.84 sec: 1.27x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 78.2 ms: 1.14x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 204 us: 1.13x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 99.2 ms: 1.08x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                                    |
| json_loads           | 28.5 us                                                | 29.9 us: 1.05x slower                                                   |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                   |
| python_startup         | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.19x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.16x faster                                                   |
| django_template | 34.6 ms                                                | 31.5 ms: 1.10x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 626 ms: 1.89x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 320 ms: 1.80x faster                                                    |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.77x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 331 ms: 1.74x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 486 ms: 1.49x faster                                                    |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 28.9 us: 1.41x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.63 us: 1.27x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.84 sec: 1.27x faster                                                  |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                    |
| comprehensions             | 21.8 us                                                | 17.8 us: 1.23x faster                                                   |
| float                      | 84.7 ms                                                | 69.6 ms: 1.22x faster                                                   |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                                   |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                    |
| go                         | 139 ms                                                 | 119 ms: 1.17x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.53 us: 1.17x faster                                                   |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.16x faster                                                   |
| spectral_norm              | 115 ms                                                 | 99.1 ms: 1.16x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 78.2 ms: 1.14x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 71.9 ms: 1.14x faster                                                   |
| async_generators           | 463 ms                                                 | 407 ms: 1.14x faster                                                    |
| raytrace                   | 312 ms                                                 | 275 ms: 1.14x faster                                                    |
| pyflate                    | 482 ms                                                 | 426 ms: 1.13x faster                                                    |
| pathlib                    | 19.3 ms                                                | 17.1 ms: 1.13x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.29 ms: 1.13x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 204 us: 1.13x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.48 ms: 1.13x faster                                                   |
| chaos                      | 67.0 ms                                                | 59.7 ms: 1.12x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.12x faster                                                    |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 67.9 ms: 1.11x faster                                                   |
| generators                 | 31.2 ms                                                | 28.2 ms: 1.11x faster                                                   |
| django_template            | 34.6 ms                                                | 31.5 ms: 1.10x faster                                                   |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.09x faster                                                    |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.35 ms: 1.08x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 99.2 ms: 1.08x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 20.3 ms: 1.06x faster                                                   |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                    |
| richards                   | 45.8 ms                                                | 43.5 ms: 1.05x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.05x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.71 us: 1.05x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 744 ms: 1.04x faster                                                    |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                    |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                    |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                  |
| nbody                      | 97.0 ms                                                | 94.1 ms: 1.03x faster                                                   |
| fannkuch                   | 417 ms                                                 | 405 ms: 1.03x faster                                                    |
| sqlglot_optimize           | 54.8 ms                                                | 53.3 ms: 1.03x faster                                                   |
| nqueens                    | 83.3 ms                                                | 81.1 ms: 1.03x faster                                                   |
| richards_super             | 51.5 ms                                                | 50.2 ms: 1.03x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 67.2 ms: 1.02x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                    |
| sympy_expand               | 478 ms                                                 | 471 ms: 1.01x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                                    |
| hexiom                     | 6.41 ms                                                | 6.36 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| logging_silent             | 104 ns                                                 | 104 ns: 1.00x faster                                                    |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                                    |
| json                       | 5.26 ms                                                | 5.35 ms: 1.02x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                   |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                    |
| bench_thread_pool          | 842 us                                                 | 879 us: 1.04x slower                                                    |
| coroutines                 | 23.2 ms                                                | 24.3 ms: 1.05x slower                                                   |
| json_loads                 | 28.5 us                                                | 29.9 us: 1.05x slower                                                   |
| telco                      | 7.10 ms                                                | 7.59 ms: 1.07x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 25.6 ms: 1.11x slower                                                   |
| coverage                   | 72.7 ms                                                | 84.2 ms: 1.16x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 4.77 ms: 1.26x slower                                                   |
| python_startup             | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 2.42 ms: 1.64x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 82.2 ms: 3.42x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250303-3.14.0a5+-004e970-JIT/bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.111x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x