# Results vs. 3.12.0

- fork: python
- ref: ae4d27eba7c746463c62
- machine: linux-x86_64
- commit hash: ae4d27e
- commit date: 2025-07-24
- overall geometric mean: 1.036x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 286 ms: 1.00x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 618 ms: 1.69x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 327 ms: 1.66x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 636 ms: 1.66x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                        |
| async_tree_none            | 452 ms                                                       | 280 ms: 1.61x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 270 ms: 1.60x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 501 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 506 ms: 1.38x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.57x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 63.6 ms: 1.21x faster                                                       |
| pidigits       | 265 ms                                                       | 256 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 99.4 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.08x faster                                                        |
| regex_dna      | 239 ms                                                       | 227 ms: 1.05x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 24.4 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.91 sec: 1.13x faster                                                      |
| unpickle_pure_python | 210 us                                                       | 193 us: 1.09x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 80.4 ms: 1.07x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 56.0 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 99.1 ms: 1.04x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.02x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 331 us: 1.04x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.84 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.2 ms: 1.09x faster                                                       |
| mako            | 10.0 ms                                                      | 9.65 ms: 1.04x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.29 sec: 1.99x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 618 ms: 1.69x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 327 ms: 1.66x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 636 ms: 1.66x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                        |
| async_tree_none            | 452 ms                                                       | 280 ms: 1.61x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 270 ms: 1.60x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 501 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 506 ms: 1.38x faster                                                        |
| deepcopy                   | 368 us                                                       | 279 us: 1.32x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 27.9 us: 1.32x faster                                                       |
| richards                   | 45.7 ms                                                      | 35.1 ms: 1.30x faster                                                       |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.26x faster                                                       |
| richards_super             | 51.3 ms                                                      | 40.7 ms: 1.26x faster                                                       |
| generators                 | 37.4 ms                                                      | 30.1 ms: 1.24x faster                                                       |
| float                      | 76.6 ms                                                      | 63.6 ms: 1.21x faster                                                       |
| go                         | 150 ms                                                       | 129 ms: 1.16x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 80.4 ms: 1.14x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 2.84 ms: 1.14x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.61 us: 1.13x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 1.91 sec: 1.13x faster                                                      |
| deepcopy_reduce            | 3.37 us                                                      | 2.99 us: 1.13x faster                                                       |
| logging_simple             | 6.71 us                                                      | 5.96 us: 1.13x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 58.5 ms: 1.12x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 17.0 ms: 1.11x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.49 sec: 1.11x faster                                                      |
| pprint_safe_repr           | 807 ms                                                       | 736 ms: 1.10x faster                                                        |
| pyflate                    | 439 ms                                                       | 401 ms: 1.09x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 63.2 ms: 1.09x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 193 us: 1.09x faster                                                        |
| django_template            | 38.2 ms                                                      | 35.2 ms: 1.09x faster                                                       |
| regex_compile              | 144 ms                                                       | 133 ms: 1.08x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.08x faster                                                        |
| chaos                      | 64.0 ms                                                      | 59.6 ms: 1.07x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 80.4 ms: 1.07x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 22.4 ms: 1.07x faster                                                       |
| scimark_sor                | 109 ms                                                       | 102 ms: 1.06x faster                                                        |
| meteor_contest             | 128 ms                                                       | 121 ms: 1.06x faster                                                        |
| regex_dna                  | 239 ms                                                       | 227 ms: 1.05x faster                                                        |
| raytrace                   | 298 ms                                                       | 284 ms: 1.05x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 94.4 ms: 1.05x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 56.0 ms: 1.04x faster                                                       |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 77.3 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 99.1 ms: 1.04x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.65 ms: 1.04x faster                                                       |
| pidigits                   | 265 ms                                                       | 256 ms: 1.04x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.4 ms: 1.03x faster                                                       |
| logging_silent             | 94.4 ns                                                      | 92.4 ns: 1.02x faster                                                       |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                        |
| 2to3                       | 285 ms                                                       | 286 ms: 1.00x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                      |
| sqlite_synth               | 2.77 us                                                      | 2.83 us: 1.02x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.84 ms: 1.02x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.02x slower                                                       |
| sympy_expand               | 484 ms                                                       | 499 ms: 1.03x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 24.4 ms: 1.03x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 93.3 ms: 1.04x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 331 us: 1.04x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.20 ms: 1.04x slower                                                       |
| fannkuch                   | 350 ms                                                       | 366 ms: 1.05x slower                                                        |
| json                       | 5.12 ms                                                      | 5.49 ms: 1.07x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 169 us: 1.11x slower                                                        |
| nbody                      | 88.0 ms                                                      | 99.4 ms: 1.13x slower                                                       |
| async_generators           | 390 ms                                                       | 452 ms: 1.16x slower                                                        |
| coverage                   | 66.7 ms                                                      | 79.0 ms: 1.18x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.09 ms: 1.21x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.88 ms: 1.81x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.54 ms: 1.88x slower                                                       |
| telco                      | 6.96 ms                                                      | 159 ms: 22.78x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (3): scimark_fft, pycparser, regex_effbot
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250724-3.15.0a0-ae4d27e-JIT/bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.14x