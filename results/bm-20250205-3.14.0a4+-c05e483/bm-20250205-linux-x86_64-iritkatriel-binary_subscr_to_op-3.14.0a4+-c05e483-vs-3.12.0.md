# Results vs. 3.12.0

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: c05e483
- commit date: 2025-02-05
- overall geometric mean: 1.117x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 252 ms: 1.09x faster                                                       |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.91x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 614 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                       |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.80x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 68.8 ms: 1.23x faster                                                      |
| nbody          | 97.0 ms                                                | 94.7 ms: 1.02x faster                                                      |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.36 ms: 1.07x faster                                                      |
| regex_dna      | 212 ms                                                 | 213 ms: 1.00x slower                                                       |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 97.5 ms: 1.09x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 83.5 ms: 1.07x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 58.1 ms: 1.06x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 312 us: 1.04x faster                                                       |
| json_loads           | 28.5 us                                                | 28.9 us: 1.02x slower                                                      |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.10 ms: 1.02x slower                                                      |
| python_startup         | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                      |
| django_template | 34.6 ms                                                | 31.5 ms: 1.10x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.91x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 614 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                       |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.80x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                       |
| deepcopy                   | 371 us                                                 | 257 us: 1.45x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 30.1 us: 1.35x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.2 us: 1.34x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                                      |
| float                      | 84.7 ms                                                | 68.8 ms: 1.23x faster                                                      |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                                      |
| async_generators           | 463 ms                                                 | 381 ms: 1.22x faster                                                       |
| go                         | 139 ms                                                 | 115 ms: 1.21x faster                                                       |
| logging_format             | 7.23 us                                                | 5.98 us: 1.21x faster                                                      |
| spectral_norm              | 115 ms                                                 | 95.5 ms: 1.20x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.42 us: 1.19x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                     |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.16 ms: 1.18x faster                                                      |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 71.1 ms: 1.15x faster                                                      |
| chaos                      | 67.0 ms                                                | 58.7 ms: 1.14x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                       |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                       |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                       |
| scimark_fft                | 382 ms                                                 | 341 ms: 1.12x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 67.1 ms: 1.12x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                                       |
| generators                 | 31.2 ms                                                | 28.1 ms: 1.11x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.23 ms: 1.11x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 703 ms: 1.10x faster                                                       |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                      |
| django_template            | 34.6 ms                                                | 31.5 ms: 1.10x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.54 ms: 1.10x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 97.5 ms: 1.09x faster                                                      |
| 2to3                       | 274 ms                                                 | 252 ms: 1.09x faster                                                       |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.3 ms: 1.08x faster                                                      |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                      |
| regex_effbot               | 3.61 ms                                                | 3.36 ms: 1.07x faster                                                      |
| sqlglot_normalize          | 110 ms                                                 | 103 ms: 1.07x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.46 sec: 1.07x faster                                                     |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 83.5 ms: 1.07x faster                                                      |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 58.1 ms: 1.06x faster                                                      |
| sympy_expand               | 478 ms                                                 | 450 ms: 1.06x faster                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 51.7 ms: 1.06x faster                                                      |
| richards                   | 45.8 ms                                                | 43.4 ms: 1.06x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                                       |
| pyflate                    | 482 ms                                                 | 460 ms: 1.05x faster                                                       |
| richards_super             | 51.5 ms                                                | 49.3 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.85 ms: 1.04x faster                                                      |
| nqueens                    | 83.3 ms                                                | 79.9 ms: 1.04x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 312 us: 1.04x faster                                                       |
| json                       | 5.26 ms                                                | 5.08 ms: 1.03x faster                                                      |
| fannkuch                   | 417 ms                                                 | 407 ms: 1.03x faster                                                       |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 66.9 ms: 1.02x faster                                                      |
| nbody                      | 97.0 ms                                                | 94.7 ms: 1.02x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                       |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                       |
| hexiom                     | 6.41 ms                                                | 6.33 ms: 1.01x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| regex_dna                  | 212 ms                                                 | 213 ms: 1.00x slower                                                       |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.02x slower                                                      |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.10 ms: 1.02x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 872 us: 1.04x slower                                                       |
| telco                      | 7.10 ms                                                | 7.76 ms: 1.09x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                      |
| coverage                   | 72.7 ms                                                | 91.8 ms: 1.26x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 5.03 ms: 1.33x slower                                                      |
| python_startup             | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.68x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 82.3 ms: 3.43x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250205-3.14.0a4+-c05e483/bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.117x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.09x