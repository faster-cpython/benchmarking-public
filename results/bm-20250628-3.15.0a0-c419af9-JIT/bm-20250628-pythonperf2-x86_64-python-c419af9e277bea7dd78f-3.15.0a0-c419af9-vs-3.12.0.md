# Results vs. 3.12.0

- fork: python
- ref: c419af9e277bea7dd78f
- machine: linux-x86_64
- commit hash: c419af9
- commit date: 2025-06-28
- overall geometric mean: 1.078x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 286 ms: 1.00x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 623 ms: 1.69x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 626 ms: 1.66x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 328 ms: 1.65x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 330 ms: 1.65x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 270 ms: 1.59x faster                                                        |
| async_tree_none            | 452 ms                                                       | 284 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 503 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 506 ms: 1.38x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.57x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 64.7 ms: 1.18x faster                                                       |
| pidigits       | 265 ms                                                       | 257 ms: 1.03x faster                                                        |
| nbody          | 88.0 ms                                                      | 99.6 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| regex_dna      | 239 ms                                                       | 223 ms: 1.07x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                                       |
| regex_effbot   | 3.57 ms                                                      | 3.55 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.94 sec: 1.11x faster                                                      |
| unpickle_pure_python | 210 us                                                       | 194 us: 1.08x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 133 ms: 1.08x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 80.2 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 95.8 ms: 1.07x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 56.8 ms: 1.03x faster                                                       |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.03x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 340 us: 1.07x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.3 ms: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.82 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.6 ms: 1.07x faster                                                       |
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.30 sec: 1.98x faster                                                      |
| async_tree_io_tg           | 1.05 sec                                                     | 623 ms: 1.69x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 626 ms: 1.66x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 328 ms: 1.65x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 330 ms: 1.65x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 270 ms: 1.59x faster                                                        |
| async_tree_none            | 452 ms                                                       | 284 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 503 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 506 ms: 1.38x faster                                                        |
| deepcopy                   | 368 us                                                       | 275 us: 1.34x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 28.0 us: 1.31x faster                                                       |
| richards                   | 45.7 ms                                                      | 35.1 ms: 1.30x faster                                                       |
| generators                 | 37.4 ms                                                      | 29.6 ms: 1.26x faster                                                       |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                       |
| richards_super             | 51.3 ms                                                      | 42.1 ms: 1.22x faster                                                       |
| float                      | 76.6 ms                                                      | 64.7 ms: 1.18x faster                                                       |
| go                         | 150 ms                                                       | 129 ms: 1.16x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.52 us: 1.15x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.95 us: 1.14x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 81.1 ms: 1.13x faster                                                       |
| logging_simple             | 6.71 us                                                      | 5.96 us: 1.13x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 2.89 ms: 1.12x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 17.0 ms: 1.11x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 1.94 sec: 1.11x faster                                                      |
| dulwich_log                | 65.4 ms                                                      | 59.4 ms: 1.10x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 63.0 ms: 1.09x faster                                                       |
| regex_compile              | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| unpickle_pure_python       | 210 us                                                       | 194 us: 1.08x faster                                                        |
| pyflate                    | 439 ms                                                       | 407 ms: 1.08x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 133 ms: 1.08x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 80.2 ms: 1.07x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 95.8 ms: 1.07x faster                                                       |
| django_template            | 38.2 ms                                                      | 35.6 ms: 1.07x faster                                                       |
| regex_dna                  | 239 ms                                                       | 223 ms: 1.07x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 22.4 ms: 1.07x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.55 sec: 1.07x faster                                                      |
| chaos                      | 64.0 ms                                                      | 60.2 ms: 1.06x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 764 ms: 1.06x faster                                                        |
| scimark_sor                | 109 ms                                                       | 103 ms: 1.06x faster                                                        |
| meteor_contest             | 128 ms                                                       | 122 ms: 1.05x faster                                                        |
| raytrace                   | 298 ms                                                       | 284 ms: 1.05x faster                                                        |
| sympy_str                  | 302 ms                                                       | 292 ms: 1.04x faster                                                        |
| pidigits                   | 265 ms                                                       | 257 ms: 1.03x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 78.1 ms: 1.03x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 56.8 ms: 1.03x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.4 ms: 1.03x faster                                                       |
| regex_v8                   | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 96.9 ms: 1.02x faster                                                       |
| logging_silent             | 94.4 ns                                                      | 93.2 ns: 1.01x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.55 ms: 1.01x faster                                                       |
| 2to3                       | 285 ms                                                       | 286 ms: 1.00x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| sqlite_synth               | 2.77 us                                                      | 2.83 us: 1.02x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.82 ms: 1.02x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.12 ms: 1.03x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.03x slower                                                       |
| json                       | 5.12 ms                                                      | 5.27 ms: 1.03x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 92.7 ms: 1.03x slower                                                       |
| sympy_expand               | 484 ms                                                       | 500 ms: 1.03x slower                                                        |
| fannkuch                   | 350 ms                                                       | 372 ms: 1.06x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 340 us: 1.07x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.3 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 168 us: 1.11x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.79 ms: 1.12x slower                                                       |
| nbody                      | 88.0 ms                                                      | 99.6 ms: 1.13x slower                                                       |
| async_generators           | 390 ms                                                       | 443 ms: 1.14x slower                                                        |
| coverage                   | 66.7 ms                                                      | 78.5 ms: 1.18x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.01 ms: 1.19x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.82 ms: 1.77x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.42 ms: 1.85x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.08x faster                                                                |

Benchmark hidden because not significant (3): asyncio_websockets, scimark_fft, pycparser
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250628-3.15.0a0-c419af9-JIT/bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.078x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.14x