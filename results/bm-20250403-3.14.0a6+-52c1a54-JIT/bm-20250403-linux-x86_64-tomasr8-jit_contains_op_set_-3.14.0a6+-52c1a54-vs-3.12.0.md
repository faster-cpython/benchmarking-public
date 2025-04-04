# Results vs. 3.12.0

- fork: tomasr8
- ref: jit_contains_op_set_
- machine: linux-x86_64
- commit hash: 52c1a54
- commit date: 2025-04-03
- overall geometric mean: 1.130x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 253 ms: 1.08x faster                                                    |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                    |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 477 ms: 1.52x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 64.8 ms: 1.31x faster                                                   |
| nbody          | 97.0 ms                                                | 89.2 ms: 1.09x faster                                                   |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.13x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.36 ms: 1.07x faster                                                   |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                    |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 79.6 ms: 1.12x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 55.4 ms: 1.11x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 97.2 ms: 1.10x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                    |
| json_loads           | 28.5 us                                                | 29.6 us: 1.04x slower                                                   |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                            |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.20 ms: 1.18x slower                                                   |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                   |
| django_template | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.21 sec: 2.17x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                    |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 477 ms: 1.52x faster                                                    |
| deepcopy                   | 371 us                                                 | 250 us: 1.49x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 28.6 us: 1.42x faster                                                   |
| float                      | 84.7 ms                                                | 64.8 ms: 1.31x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                  |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.24x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.02 ms: 1.23x faster                                                   |
| richards                   | 45.8 ms                                                | 38.4 ms: 1.20x faster                                                   |
| raytrace                   | 312 ms                                                 | 261 ms: 1.19x faster                                                    |
| comprehensions             | 21.8 us                                                | 18.3 us: 1.19x faster                                                   |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                    |
| chaos                      | 67.0 ms                                                | 56.9 ms: 1.18x faster                                                   |
| go                         | 139 ms                                                 | 122 ms: 1.14x faster                                                    |
| logging_format             | 7.23 us                                                | 6.33 us: 1.14x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                    |
| richards_super             | 51.5 ms                                                | 45.3 ms: 1.14x faster                                                   |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.13x faster                                                    |
| pathlib                    | 19.3 ms                                                | 17.1 ms: 1.13x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.71 us: 1.13x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 66.4 ms: 1.13x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 60.8 ms: 1.13x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 79.6 ms: 1.12x faster                                                   |
| pyflate                    | 482 ms                                                 | 432 ms: 1.12x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 55.4 ms: 1.11x faster                                                   |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.11x faster                                                    |
| async_generators           | 463 ms                                                 | 417 ms: 1.11x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.58 ms: 1.10x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.10x faster                                                    |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 97.2 ms: 1.10x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                   |
| mako                       | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 75.2 ms: 1.09x faster                                                   |
| nbody                      | 97.0 ms                                                | 89.2 ms: 1.09x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.2 ms: 1.08x faster                                                   |
| django_template            | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                   |
| 2to3                       | 274 ms                                                 | 253 ms: 1.08x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.36 ms: 1.07x faster                                                   |
| logging_silent             | 104 ns                                                 | 97.5 ns: 1.07x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 735 ms: 1.06x faster                                                    |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.05x faster                                                   |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                    |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.03x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                    |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| fannkuch                   | 417 ms                                                 | 414 ms: 1.01x faster                                                    |
| json                       | 5.26 ms                                                | 5.31 ms: 1.01x slower                                                   |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                    |
| json_loads                 | 28.5 us                                                | 29.6 us: 1.04x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                    |
| hexiom                     | 6.41 ms                                                | 6.71 ms: 1.05x slower                                                   |
| coroutines                 | 23.2 ms                                                | 24.3 ms: 1.05x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 885 us: 1.05x slower                                                    |
| telco                      | 7.10 ms                                                | 7.82 ms: 1.10x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 8.20 ms: 1.18x slower                                                   |
| coverage                   | 72.7 ms                                                | 88.4 ms: 1.22x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 4.76 ms: 1.25x slower                                                   |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 2.44 ms: 1.65x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 82.3 ms: 3.43x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                            |

Benchmark hidden because not significant (3): nqueens, asyncio_websockets, pickle_pure_python
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-52c1a54-JIT/bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.130x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.12x