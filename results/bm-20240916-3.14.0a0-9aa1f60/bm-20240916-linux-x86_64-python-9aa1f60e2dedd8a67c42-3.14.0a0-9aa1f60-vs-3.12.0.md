# Results vs. 3.12.0

- fork: python
- ref: 9aa1f60e2dedd8a67c42
- machine: linux-x86_64
- commit hash: 9aa1f60
- commit date: 2024-09-16
- overall geometric mean: 1.068x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                  |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.03x faster                                                |
| tornado_http   | 103 ms                                                 | 90.5 ms: 1.13x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 385 ms: 1.49x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 303 ms: 1.48x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 399 ms: 1.45x faster                                                  |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 862 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 555 ms: 1.31x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 911 ms: 1.30x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 566 ms: 1.28x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 77.0 ms: 1.10x faster                                                 |
| nbody          | 97.0 ms                                                | 88.8 ms: 1.09x faster                                                 |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                  |
| regex_v8       | 23.1 ms                                                | 22.9 ms: 1.01x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                 |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.05 sec: 1.14x faster                                                |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 309 us: 1.05x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 87.2 ms: 1.02x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                 |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                 |
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 385 ms: 1.49x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 303 ms: 1.48x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 399 ms: 1.45x faster                                                  |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                  |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 30.4 us: 1.34x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 862 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 555 ms: 1.31x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 911 ms: 1.30x faster                                                  |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 566 ms: 1.28x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                 |
| go                         | 139 ms                                                 | 118 ms: 1.18x faster                                                  |
| raytrace                   | 312 ms                                                 | 268 ms: 1.17x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                  |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 71.3 ms: 1.15x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.15x faster                                                 |
| logging_format             | 7.23 us                                                | 6.32 us: 1.14x faster                                                 |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.14x faster                                                  |
| chaos                      | 67.0 ms                                                | 58.8 ms: 1.14x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.05 sec: 1.14x faster                                                |
| tornado_http               | 103 ms                                                 | 90.5 ms: 1.13x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                                 |
| generators                 | 31.2 ms                                                | 27.8 ms: 1.13x faster                                                 |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 68.0 ms: 1.10x faster                                                 |
| float                      | 84.7 ms                                                | 77.0 ms: 1.10x faster                                                 |
| json                       | 5.26 ms                                                | 4.80 ms: 1.09x faster                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.1 ms: 1.09x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                 |
| nbody                      | 97.0 ms                                                | 88.8 ms: 1.09x faster                                                 |
| django_template            | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 719 ms: 1.08x faster                                                  |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                                |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                  |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.75 ms: 1.06x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 64.6 ms: 1.06x faster                                                 |
| async_generators           | 463 ms                                                 | 437 ms: 1.06x faster                                                  |
| sympy_expand               | 478 ms                                                 | 452 ms: 1.06x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 802 us: 1.05x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                |
| pickle_pure_python         | 324 us                                                 | 309 us: 1.05x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                  |
| scimark_fft                | 382 ms                                                 | 366 ms: 1.04x faster                                                  |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.03x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                 |
| nqueens                    | 83.3 ms                                                | 81.0 ms: 1.03x faster                                                 |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                                  |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                  |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 87.2 ms: 1.02x faster                                                 |
| fannkuch                   | 417 ms                                                 | 409 ms: 1.02x faster                                                  |
| pyflate                    | 482 ms                                                 | 475 ms: 1.02x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.33 ms: 1.01x faster                                                 |
| regex_v8                   | 23.1 ms                                                | 22.9 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                 |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.02x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                 |
| richards                   | 45.8 ms                                                | 46.8 ms: 1.02x slower                                                 |
| richards_super             | 51.5 ms                                                | 52.7 ms: 1.02x slower                                                 |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                  |
| coverage                   | 72.7 ms                                                | 83.9 ms: 1.15x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.49 ms: 1.18x slower                                                 |
| telco                      | 7.10 ms                                                | 8.67 ms: 1.22x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.64 ms: 1.79x slower                                                 |
| dask                       | 372 ms                                                 | 782 ms: 2.10x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (8): xml_etree_parse, pycparser, sqlite_synth, xml_etree_iterparse, bench_mp_pool, spectral_norm, asyncio_websockets, typing_runtime_protocols
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (25) of results/bm-20240916-3.14.0a0-9aa1f60/bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.068x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.08x