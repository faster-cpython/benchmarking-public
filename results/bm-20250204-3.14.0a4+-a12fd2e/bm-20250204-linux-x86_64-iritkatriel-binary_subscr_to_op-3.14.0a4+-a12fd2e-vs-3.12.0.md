# Results vs. 3.12.0

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: a12fd2e
- commit date: 2025-02-04
- overall geometric mean: 1.120x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-a12fd2e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 250 ms: 1.10x faster                                                       |
| docutils       | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-a12fd2e |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 618 ms: 1.87x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                       |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.79x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.76x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-a12fd2e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.8 ms: 1.21x faster                                                      |
| nbody          | 97.0 ms                                                | 94.4 ms: 1.03x faster                                                      |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-a12fd2e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.14 ms: 1.15x faster                                                      |
| regex_dna      | 212 ms                                                 | 208 ms: 1.02x faster                                                       |
| regex_v8       | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-a12fd2e |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.14x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 96.3 ms: 1.11x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.06x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 84.0 ms: 1.06x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 59.1 ms: 1.05x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 317 us: 1.02x faster                                                       |
| json_loads           | 28.5 us                                                | 28.9 us: 1.01x slower                                                      |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-a12fd2e |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                      |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-a12fd2e |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                      |
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-a12fd2e |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 618 ms: 1.87x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                       |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.79x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.76x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                       |
| deepcopy                   | 371 us                                                 | 256 us: 1.45x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 30.7 us: 1.33x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.23x faster                                                      |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                                      |
| spectral_norm              | 115 ms                                                 | 94.4 ms: 1.22x faster                                                      |
| float                      | 84.7 ms                                                | 69.8 ms: 1.21x faster                                                      |
| async_generators           | 463 ms                                                 | 381 ms: 1.21x faster                                                       |
| go                         | 139 ms                                                 | 117 ms: 1.19x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                     |
| logging_format             | 7.23 us                                                | 6.12 us: 1.18x faster                                                      |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.49 us: 1.18x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 70.2 ms: 1.17x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.20 ms: 1.16x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.16x faster                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.3 ms: 1.15x faster                                                      |
| regex_effbot               | 3.61 ms                                                | 3.14 ms: 1.15x faster                                                      |
| chaos                      | 67.0 ms                                                | 58.4 ms: 1.15x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.14x faster                                                       |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.14x faster                                                       |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                                       |
| sympy_str                  | 300 ms                                                 | 264 ms: 1.13x faster                                                       |
| generators                 | 31.2 ms                                                | 27.6 ms: 1.13x faster                                                      |
| scimark_fft                | 382 ms                                                 | 339 ms: 1.13x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 66.8 ms: 1.13x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 96.3 ms: 1.11x faster                                                      |
| 2to3                       | 274 ms                                                 | 250 ms: 1.10x faster                                                       |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                      |
| django_template            | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.26 ms: 1.08x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 63.4 ms: 1.08x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.56 ms: 1.08x faster                                                      |
| docutils                   | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                     |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.45 sec: 1.07x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 723 ms: 1.07x faster                                                       |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                      |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.06x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.76 ms: 1.06x faster                                                      |
| sqlglot_normalize          | 110 ms                                                 | 104 ms: 1.06x faster                                                       |
| sympy_expand               | 478 ms                                                 | 450 ms: 1.06x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 84.0 ms: 1.06x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 51.9 ms: 1.06x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 59.1 ms: 1.05x faster                                                      |
| richards                   | 45.8 ms                                                | 43.9 ms: 1.04x faster                                                      |
| pyflate                    | 482 ms                                                 | 465 ms: 1.04x faster                                                       |
| nqueens                    | 83.3 ms                                                | 80.6 ms: 1.03x faster                                                      |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                      |
| nbody                      | 97.0 ms                                                | 94.4 ms: 1.03x faster                                                      |
| json                       | 5.26 ms                                                | 5.13 ms: 1.03x faster                                                      |
| richards_super             | 51.5 ms                                                | 50.2 ms: 1.03x faster                                                      |
| fannkuch                   | 417 ms                                                 | 407 ms: 1.03x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 317 us: 1.02x faster                                                       |
| regex_dna                  | 212 ms                                                 | 208 ms: 1.02x faster                                                       |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.01x faster                                                      |
| hexiom                     | 6.41 ms                                                | 6.33 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                      |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.01x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 857 us: 1.02x slower                                                       |
| logging_silent             | 104 ns                                                 | 109 ns: 1.04x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                      |
| telco                      | 7.10 ms                                                | 7.76 ms: 1.09x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.12x slower                                                      |
| coverage                   | 72.7 ms                                                | 90.1 ms: 1.24x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 4.95 ms: 1.30x slower                                                      |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.68x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 80.4 ms: 3.35x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                               |

Benchmark hidden because not significant (2): typing_runtime_protocols, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250204-3.14.0a4+-a12fd2e/bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-a12fd2e.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.120x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.09x