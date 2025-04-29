# Results vs. 3.12.0

- fork: python
- ref: bac4edad69bb20dd9460
- machine: linux-x86_64
- commit hash: bac4eda
- commit date: 2024-06-16
- overall geometric mean: 1.052x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 266 ms: 1.03x faster                                                  |
| docutils       | 2.77 sec                                               | 2.72 sec: 1.02x faster                                                |
| tornado_http   | 103 ms                                                 | 92.1 ms: 1.11x faster                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 333 ms: 1.35x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 431 ms: 1.33x faster                                                  |
| async_tree_none            | 472 ms                                                 | 362 ms: 1.30x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 458 ms: 1.26x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 595 ms: 1.22x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 952 ms: 1.21x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 978 ms: 1.21x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 603 ms: 1.20x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 87.0 ms: 1.12x faster                                                 |
| float          | 84.7 ms                                                | 77.7 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 132 ms: 1.13x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.50 ms: 1.03x faster                                                 |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.13 sec: 1.09x faster                                                |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.3 ms: 1.05x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 59.4 ms: 1.04x faster                                                 |
| json_loads           | 28.5 us                                                | 28.0 us: 1.02x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.01 ms: 1.01x slower                                                 |
| python_startup         | 9.55 ms                                                | 14.4 ms: 1.51x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.23x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                 |
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 333 ms: 1.35x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 431 ms: 1.33x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.31x faster                                                 |
| async_tree_none            | 472 ms                                                 | 362 ms: 1.30x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 458 ms: 1.26x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 595 ms: 1.22x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 952 ms: 1.21x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 978 ms: 1.21x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 603 ms: 1.20x faster                                                  |
| raytrace                   | 312 ms                                                 | 263 ms: 1.19x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.16x faster                                                 |
| logging_format             | 7.23 us                                                | 6.33 us: 1.14x faster                                                 |
| chaos                      | 67.0 ms                                                | 58.7 ms: 1.14x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 72.6 ms: 1.13x faster                                                 |
| regex_compile              | 148 ms                                                 | 132 ms: 1.13x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.77 us: 1.12x faster                                                 |
| nbody                      | 97.0 ms                                                | 87.0 ms: 1.12x faster                                                 |
| tornado_http               | 103 ms                                                 | 92.1 ms: 1.11x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 68.5 ms: 1.10x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.13 sec: 1.09x faster                                                |
| float                      | 84.7 ms                                                | 77.7 ms: 1.09x faster                                                 |
| sympy_str                  | 300 ms                                                 | 276 ms: 1.09x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 136 ms: 1.08x faster                                                  |
| generators                 | 31.2 ms                                                | 28.9 ms: 1.08x faster                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.3 ms: 1.08x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                  |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                 |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.07x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                  |
| async_generators           | 463 ms                                                 | 436 ms: 1.06x faster                                                  |
| nqueens                    | 83.3 ms                                                | 78.7 ms: 1.06x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 737 ms: 1.05x faster                                                  |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 65.2 ms: 1.05x faster                                                 |
| scimark_fft                | 382 ms                                                 | 365 ms: 1.05x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 85.3 ms: 1.05x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.14 ms: 1.04x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 59.4 ms: 1.04x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                |
| regex_effbot               | 3.61 ms                                                | 3.50 ms: 1.03x faster                                                 |
| 2to3                       | 274 ms                                                 | 266 ms: 1.03x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.02x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 825 us: 1.02x faster                                                  |
| sympy_expand               | 478 ms                                                 | 470 ms: 1.02x faster                                                  |
| json_loads                 | 28.5 us                                                | 28.0 us: 1.02x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.72 sec: 1.02x faster                                                |
| fannkuch                   | 417 ms                                                 | 414 ms: 1.01x faster                                                  |
| pyflate                    | 482 ms                                                 | 480 ms: 1.01x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.09 ms: 1.01x slower                                                 |
| logging_silent             | 104 ns                                                 | 105 ns: 1.01x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.01 ms: 1.01x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                 |
| go                         | 139 ms                                                 | 143 ms: 1.03x slower                                                  |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                  |
| scimark_sor                | 129 ms                                                 | 134 ms: 1.03x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 2.93 us: 1.04x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                  |
| coroutines                 | 23.2 ms                                                | 24.4 ms: 1.05x slower                                                 |
| richards                   | 45.8 ms                                                | 49.9 ms: 1.09x slower                                                 |
| richards_super             | 51.5 ms                                                | 57.0 ms: 1.11x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.49 ms: 1.18x slower                                                 |
| telco                      | 7.10 ms                                                | 8.48 ms: 1.19x slower                                                 |
| coverage                   | 72.7 ms                                                | 91.5 ms: 1.26x slower                                                 |
| python_startup             | 9.55 ms                                                | 14.4 ms: 1.51x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.66 ms: 1.80x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (7): regex_v8, bench_mp_pool, pidigits, asyncio_websockets, xml_etree_parse, xml_etree_iterparse, json
Ignored benchmarks (17) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (25) of results/bm-20240616-3.14.0a0-bac4eda/bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.052x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.09x