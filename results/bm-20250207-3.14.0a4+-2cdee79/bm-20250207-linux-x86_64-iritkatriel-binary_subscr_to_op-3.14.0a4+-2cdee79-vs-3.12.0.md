# Results vs. 3.12.0

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: 2cdee79
- commit date: 2025-02-07
- overall geometric mean: 1.117x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 252 ms: 1.09x faster                                                       |
| docutils       | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 621 ms: 1.86x faster                                                       |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.78x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.75x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 493 ms: 1.47x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 501 ms: 1.45x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.0 ms: 1.21x faster                                                      |
| nbody          | 97.0 ms                                                | 91.9 ms: 1.06x faster                                                      |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.25 ms: 1.11x faster                                                      |
| regex_dna      | 212 ms                                                 | 215 ms: 1.02x slower                                                       |
| regex_v8       | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 97.1 ms: 1.10x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 83.2 ms: 1.07x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 58.1 ms: 1.06x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                       |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                                      |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                      |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.2 ms: 1.08x faster                                                      |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 621 ms: 1.86x faster                                                       |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.78x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.75x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 493 ms: 1.47x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 501 ms: 1.45x faster                                                       |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                       |
| comprehensions             | 21.8 us                                                | 16.2 us: 1.35x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 30.7 us: 1.33x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                      |
| pathlib                    | 19.3 ms                                                | 15.6 ms: 1.24x faster                                                      |
| float                      | 84.7 ms                                                | 70.0 ms: 1.21x faster                                                      |
| async_generators           | 463 ms                                                 | 384 ms: 1.21x faster                                                       |
| spectral_norm              | 115 ms                                                 | 96.0 ms: 1.20x faster                                                      |
| logging_format             | 7.23 us                                                | 6.07 us: 1.19x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                                     |
| go                         | 139 ms                                                 | 118 ms: 1.18x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.50 us: 1.17x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.17 ms: 1.17x faster                                                      |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 70.8 ms: 1.16x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.15x faster                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.2 ms: 1.15x faster                                                      |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                       |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.15x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                       |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                                      |
| scimark_fft                | 382 ms                                                 | 337 ms: 1.13x faster                                                       |
| generators                 | 31.2 ms                                                | 27.6 ms: 1.13x faster                                                      |
| sympy_str                  | 300 ms                                                 | 266 ms: 1.13x faster                                                       |
| regex_effbot               | 3.61 ms                                                | 3.25 ms: 1.11x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 67.9 ms: 1.11x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 97.1 ms: 1.10x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.25 ms: 1.09x faster                                                      |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                                      |
| 2to3                       | 274 ms                                                 | 252 ms: 1.09x faster                                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.55 ms: 1.08x faster                                                      |
| pyflate                    | 482 ms                                                 | 446 ms: 1.08x faster                                                       |
| docutils                   | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                     |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.08x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 63.8 ms: 1.07x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 722 ms: 1.07x faster                                                       |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 83.2 ms: 1.07x faster                                                      |
| sqlglot_normalize          | 110 ms                                                 | 103 ms: 1.07x faster                                                       |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.47 sec: 1.07x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 58.1 ms: 1.06x faster                                                      |
| sympy_expand               | 478 ms                                                 | 451 ms: 1.06x faster                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 51.8 ms: 1.06x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                     |
| nbody                      | 97.0 ms                                                | 91.9 ms: 1.06x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.81 ms: 1.05x faster                                                      |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                     |
| nqueens                    | 83.3 ms                                                | 80.1 ms: 1.04x faster                                                      |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                      |
| fannkuch                   | 417 ms                                                 | 405 ms: 1.03x faster                                                       |
| json                       | 5.26 ms                                                | 5.12 ms: 1.03x faster                                                      |
| richards                   | 45.8 ms                                                | 44.6 ms: 1.03x faster                                                      |
| hexiom                     | 6.41 ms                                                | 6.26 ms: 1.02x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                       |
| typing_runtime_protocols   | 158 us                                                 | 156 us: 1.01x faster                                                       |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| coroutines                 | 23.2 ms                                                | 23.1 ms: 1.00x faster                                                      |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                      |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                                       |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.02x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 860 us: 1.02x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                      |
| telco                      | 7.10 ms                                                | 7.81 ms: 1.10x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 4.80 ms: 1.26x slower                                                      |
| coverage                   | 72.7 ms                                                | 92.4 ms: 1.27x slower                                                      |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.66x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 80.5 ms: 3.35x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                               |

Benchmark hidden because not significant (2): richards_super, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250207-3.14.0a4+-2cdee79/bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.117x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.09x