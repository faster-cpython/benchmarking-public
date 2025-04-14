# Results vs. 3.12.0

- fork: mdboom
- ref: specialize_compact_i
- machine: linux-x86_64
- commit hash: f366df0
- commit date: 2025-01-29
- overall geometric mean: 1.115x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 253 ms: 1.09x faster                                                   |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 609 ms: 1.94x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.87x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 321 ms: 1.80x faster                                                   |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.9 ms: 1.19x faster                                                  |
| nbody          | 97.0 ms                                                | 93.2 ms: 1.04x faster                                                  |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.18x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.34 ms: 1.08x faster                                                  |
| regex_dna      | 212 ms                                                 | 209 ms: 1.01x faster                                                   |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 97.4 ms: 1.10x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 83.9 ms: 1.06x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 58.4 ms: 1.06x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                   |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                  |
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 609 ms: 1.94x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.87x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 321 ms: 1.80x faster                                                   |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                   |
| deepcopy                   | 371 us                                                 | 255 us: 1.45x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 30.8 us: 1.32x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.24x faster                                                  |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.23x faster                                                  |
| async_generators           | 463 ms                                                 | 384 ms: 1.20x faster                                                   |
| spectral_norm              | 115 ms                                                 | 95.9 ms: 1.20x faster                                                  |
| logging_format             | 7.23 us                                                | 6.04 us: 1.20x faster                                                  |
| float                      | 84.7 ms                                                | 70.9 ms: 1.19x faster                                                  |
| go                         | 139 ms                                                 | 117 ms: 1.19x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.45 us: 1.19x faster                                                  |
| regex_compile              | 148 ms                                                 | 125 ms: 1.18x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 69.9 ms: 1.17x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.16x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.15x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.4 ms: 1.14x faster                                                  |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                   |
| scimark_fft                | 382 ms                                                 | 335 ms: 1.14x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                   |
| chaos                      | 67.0 ms                                                | 59.0 ms: 1.13x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 66.3 ms: 1.13x faster                                                  |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                                   |
| generators                 | 31.2 ms                                                | 28.3 ms: 1.10x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 97.4 ms: 1.10x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.62 ms: 1.09x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                  |
| 2to3                       | 274 ms                                                 | 253 ms: 1.09x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.34 ms: 1.08x faster                                                  |
| django_template            | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                  |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.45 sec: 1.07x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 63.9 ms: 1.07x faster                                                  |
| pyflate                    | 482 ms                                                 | 450 ms: 1.07x faster                                                   |
| sqlglot_normalize          | 110 ms                                                 | 103 ms: 1.07x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                                  |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                   |
| sympy_expand               | 478 ms                                                 | 449 ms: 1.06x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 83.9 ms: 1.06x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 731 ms: 1.06x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 58.4 ms: 1.06x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 52.0 ms: 1.05x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                 |
| fannkuch                   | 417 ms                                                 | 401 ms: 1.04x faster                                                   |
| nbody                      | 97.0 ms                                                | 93.2 ms: 1.04x faster                                                  |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                  |
| richards                   | 45.8 ms                                                | 44.2 ms: 1.04x faster                                                  |
| nqueens                    | 83.3 ms                                                | 80.5 ms: 1.03x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                  |
| json                       | 5.26 ms                                                | 5.14 ms: 1.02x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.29 ms: 1.02x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                   |
| richards_super             | 51.5 ms                                                | 50.8 ms: 1.02x faster                                                  |
| regex_dna                  | 212 ms                                                 | 209 ms: 1.01x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                 |
| typing_runtime_protocols   | 158 us                                                 | 156 us: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 858 us: 1.02x slower                                                   |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                  |
| logging_silent             | 104 ns                                                 | 113 ns: 1.08x slower                                                   |
| telco                      | 7.10 ms                                                | 7.78 ms: 1.10x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.13x slower                                                  |
| coverage                   | 72.7 ms                                                | 90.7 ms: 1.25x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 5.03 ms: 1.33x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.68x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250129-3.14.0a4+-f366df0/bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.115x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.09x