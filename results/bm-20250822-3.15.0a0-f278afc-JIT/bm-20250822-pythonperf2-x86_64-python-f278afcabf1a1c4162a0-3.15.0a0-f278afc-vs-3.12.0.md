# Results vs. 3.12.0

- fork: python
- ref: f278afcabf1a1c4162a0
- machine: linux-x86_64
- commit hash: f278afc
- commit date: 2025-08-22
- overall geometric mean: 1.039x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 287 ms: 1.01x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 618 ms: 1.69x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 627 ms: 1.68x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 324 ms: 1.68x faster                                                        |
| async_tree_none            | 452 ms                                                       | 270 ms: 1.67x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 328 ms: 1.65x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 269 ms: 1.60x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 497 ms: 1.40x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 505 ms: 1.38x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.59x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 65.0 ms: 1.18x faster                                                       |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 105 ms: 1.20x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 134 ms: 1.08x faster                                                        |
| regex_dna      | 239 ms                                                       | 223 ms: 1.07x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.72 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.96 sec: 1.10x faster                                                      |
| xml_etree_generate   | 86.1 ms                                                      | 80.3 ms: 1.07x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 195 us: 1.07x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 96.5 ms: 1.07x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 55.2 ms: 1.06x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 138 ms: 1.05x faster                                                        |
| json_dumps           | 10.2 ms                                                      | 10.2 ms: 1.00x slower                                                       |
| json_loads           | 24.4 us                                                      | 25.2 us: 1.03x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 333 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.81 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.6 ms: 1.07x faster                                                       |
| mako            | 10.0 ms                                                      | 9.85 ms: 1.02x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.29 sec: 1.99x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 618 ms: 1.69x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 627 ms: 1.68x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 324 ms: 1.68x faster                                                        |
| async_tree_none            | 452 ms                                                       | 270 ms: 1.67x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 328 ms: 1.65x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 269 ms: 1.60x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 497 ms: 1.40x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 505 ms: 1.38x faster                                                        |
| richards                   | 45.7 ms                                                      | 34.0 ms: 1.35x faster                                                       |
| deepcopy                   | 368 us                                                       | 280 us: 1.31x faster                                                        |
| richards_super             | 51.3 ms                                                      | 39.4 ms: 1.30x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 28.3 us: 1.30x faster                                                       |
| generators                 | 37.4 ms                                                      | 29.0 ms: 1.29x faster                                                       |
| comprehensions             | 21.9 us                                                      | 17.5 us: 1.26x faster                                                       |
| go                         | 150 ms                                                       | 127 ms: 1.18x faster                                                        |
| float                      | 76.6 ms                                                      | 65.0 ms: 1.18x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.42 us: 1.17x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 79.6 ms: 1.15x faster                                                       |
| logging_simple             | 6.71 us                                                      | 5.85 us: 1.15x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 16.8 ms: 1.13x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 2.89 ms: 1.12x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 59.1 ms: 1.11x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.4 ms: 1.11x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.05 us: 1.10x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 1.96 sec: 1.10x faster                                                      |
| pyflate                    | 439 ms                                                       | 402 ms: 1.09x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.52 sec: 1.09x faster                                                      |
| chaos                      | 64.0 ms                                                      | 59.2 ms: 1.08x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 748 ms: 1.08x faster                                                        |
| regex_compile              | 144 ms                                                       | 134 ms: 1.08x faster                                                        |
| django_template            | 38.2 ms                                                      | 35.6 ms: 1.07x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 80.3 ms: 1.07x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 195 us: 1.07x faster                                                        |
| regex_dna                  | 239 ms                                                       | 223 ms: 1.07x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 22.4 ms: 1.07x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 96.5 ms: 1.07x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 153 ms: 1.06x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 55.2 ms: 1.06x faster                                                       |
| meteor_contest             | 128 ms                                                       | 122 ms: 1.05x faster                                                        |
| raytrace                   | 298 ms                                                       | 283 ms: 1.05x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 94.4 ms: 1.05x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 138 ms: 1.05x faster                                                        |
| scimark_sor                | 109 ms                                                       | 104 ms: 1.04x faster                                                        |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                                        |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.3 ms: 1.03x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 78.8 ms: 1.02x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.85 ms: 1.02x faster                                                       |
| logging_silent             | 94.4 ns                                                      | 93.1 ns: 1.01x faster                                                       |
| asyncio_websockets         | 387 ms                                                       | 382 ms: 1.01x faster                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.2 ms: 1.00x slower                                                       |
| 2to3                       | 285 ms                                                       | 287 ms: 1.01x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.80 us: 1.01x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.81 ms: 1.02x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                      |
| hexiom                     | 5.96 ms                                                      | 6.13 ms: 1.03x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 92.5 ms: 1.03x slower                                                       |
| sympy_expand               | 484 ms                                                       | 500 ms: 1.03x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.2 us: 1.03x slower                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.72 ms: 1.04x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 333 us: 1.05x slower                                                        |
| fannkuch                   | 350 ms                                                       | 369 ms: 1.05x slower                                                        |
| json                       | 5.12 ms                                                      | 5.53 ms: 1.08x slower                                                       |
| async_generators           | 390 ms                                                       | 434 ms: 1.11x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 172 us: 1.13x slower                                                        |
| nbody                      | 88.0 ms                                                      | 105 ms: 1.20x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.07 ms: 1.20x slower                                                       |
| coverage                   | 66.7 ms                                                      | 81.4 ms: 1.22x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.84 ms: 1.79x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.49 ms: 1.87x slower                                                       |
| telco                      | 6.96 ms                                                      | 162 ms: 23.28x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (3): pycparser, scimark_fft, regex_v8
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250822-3.15.0a0-f278afc-JIT/bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.14x