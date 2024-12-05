# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_cold_18
- machine: linux-x86_64
- commit hash: 1cd9228
- commit date: 2024-12-04
- overall geometric mean: 1.103x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.05x faster                                                   |
| docutils       | 2.77 sec                                               | 2.72 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 628 ms: 1.88x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 626 ms: 1.85x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                   |
| async_tree_none            | 472 ms                                                 | 271 ms: 1.74x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 341 ms: 1.69x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.3 ms: 1.19x faster                                                  |
| float          | 84.7 ms                                                | 75.5 ms: 1.12x faster                                                  |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.26 ms: 1.11x faster                                                  |
| regex_dna      | 212 ms                                                 | 215 ms: 1.02x slower                                                   |
| regex_v8       | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 197 us: 1.17x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 137 ms: 1.17x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 78.0 ms: 1.14x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 95.0 ms: 1.12x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 55.2 ms: 1.12x faster                                                  |
| json_loads           | 28.5 us                                                | 26.2 us: 1.09x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                   |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                  |
| django_template | 34.6 ms                                                | 34.0 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 628 ms: 1.88x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 626 ms: 1.85x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                   |
| async_tree_none            | 472 ms                                                 | 271 ms: 1.74x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 341 ms: 1.69x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                   |
| deepcopy                   | 371 us                                                 | 266 us: 1.40x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                  |
| comprehensions             | 21.8 us                                                | 17.4 us: 1.25x faster                                                  |
| richards                   | 45.8 ms                                                | 36.6 ms: 1.25x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 68.4 ms: 1.20x faster                                                  |
| richards_super             | 51.5 ms                                                | 43.1 ms: 1.20x faster                                                  |
| nbody                      | 97.0 ms                                                | 81.3 ms: 1.19x faster                                                  |
| scimark_fft                | 382 ms                                                 | 321 ms: 1.19x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                  |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.18 ms: 1.17x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 197 us: 1.17x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 137 ms: 1.17x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 64.9 ms: 1.16x faster                                                  |
| logging_format             | 7.23 us                                                | 6.26 us: 1.16x faster                                                  |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 78.0 ms: 1.14x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.72 us: 1.13x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 95.0 ms: 1.12x faster                                                  |
| float                      | 84.7 ms                                                | 75.5 ms: 1.12x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 55.2 ms: 1.12x faster                                                  |
| chaos                      | 67.0 ms                                                | 59.9 ms: 1.12x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.7 ms: 1.12x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.26 ms: 1.11x faster                                                  |
| json                       | 5.26 ms                                                | 4.76 ms: 1.10x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 711 ms: 1.09x faster                                                   |
| json_loads                 | 28.5 us                                                | 26.2 us: 1.09x faster                                                  |
| fannkuch                   | 417 ms                                                 | 384 ms: 1.09x faster                                                   |
| raytrace                   | 312 ms                                                 | 288 ms: 1.09x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.08x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.08x faster                                                 |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                   |
| pyflate                    | 482 ms                                                 | 450 ms: 1.07x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.72 ms: 1.07x faster                                                  |
| sympy_str                  | 300 ms                                                 | 284 ms: 1.06x faster                                                   |
| 2to3                       | 274 ms                                                 | 260 ms: 1.05x faster                                                   |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 20.7 ms: 1.03x faster                                                  |
| go                         | 139 ms                                                 | 135 ms: 1.03x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.02x faster                                                  |
| django_template            | 34.6 ms                                                | 34.0 ms: 1.02x faster                                                  |
| logging_silent             | 104 ns                                                 | 103 ns: 1.02x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                   |
| async_generators           | 463 ms                                                 | 456 ms: 1.02x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.72 sec: 1.02x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 67.7 ms: 1.01x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 55.6 ms: 1.01x slower                                                  |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.02x slower                                                   |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                  |
| sympy_expand               | 478 ms                                                 | 490 ms: 1.02x slower                                                   |
| mdp                        | 2.63 sec                                               | 2.70 sec: 1.03x slower                                                 |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 874 us: 1.04x slower                                                   |
| telco                      | 7.10 ms                                                | 7.63 ms: 1.07x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                  |
| nqueens                    | 83.3 ms                                                | 90.6 ms: 1.09x slower                                                  |
| hexiom                     | 6.41 ms                                                | 7.04 ms: 1.10x slower                                                  |
| coverage                   | 72.7 ms                                                | 84.3 ms: 1.16x slower                                                  |
| generators                 | 31.2 ms                                                | 36.6 ms: 1.17x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.96 ms: 1.31x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.68x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.5 ms: 3.39x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (3): sqlglot_normalize, spectral_norm, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241204-3.14.0a2+-1cd9228-JIT/bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.103x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.10x