# Results vs. 3.12.0

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: 875bc77
- commit date: 2025-02-04
- overall geometric mean: 1.122x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 250 ms: 1.10x faster                                                       |
| docutils       | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 624 ms: 1.90x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 624 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 327 ms: 1.77x faster                                                       |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 258 ms: 1.74x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 492 ms: 1.47x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.44x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 68.5 ms: 1.24x faster                                                      |
| nbody          | 97.0 ms                                                | 92.1 ms: 1.05x faster                                                      |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 124 ms: 1.19x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.27 ms: 1.10x faster                                                      |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                       |
| regex_v8       | 23.1 ms                                                | 25.6 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 96.9 ms: 1.10x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 82.6 ms: 1.08x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.08x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 58.1 ms: 1.06x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 312 us: 1.04x faster                                                       |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                                      |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                      |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                      |
| mako            | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 624 ms: 1.90x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 624 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 327 ms: 1.77x faster                                                       |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 258 ms: 1.74x faster                                                       |
| deepcopy                   | 371 us                                                 | 250 us: 1.49x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 492 ms: 1.47x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.44x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.2 us: 1.34x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                      |
| float                      | 84.7 ms                                                | 68.5 ms: 1.24x faster                                                      |
| pathlib                    | 19.3 ms                                                | 15.7 ms: 1.23x faster                                                      |
| async_generators           | 463 ms                                                 | 380 ms: 1.22x faster                                                       |
| go                         | 139 ms                                                 | 115 ms: 1.21x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                     |
| regex_compile              | 148 ms                                                 | 124 ms: 1.19x faster                                                       |
| spectral_norm              | 115 ms                                                 | 97.0 ms: 1.18x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.15 ms: 1.18x faster                                                      |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.51 us: 1.17x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 69.9 ms: 1.17x faster                                                      |
| raytrace                   | 312 ms                                                 | 268 ms: 1.17x faster                                                       |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.16x faster                                                       |
| chaos                      | 67.0 ms                                                | 57.9 ms: 1.16x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.2 ms: 1.15x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                       |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.15x faster                                                       |
| sympy_str                  | 300 ms                                                 | 264 ms: 1.14x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 66.2 ms: 1.13x faster                                                      |
| scimark_fft                | 382 ms                                                 | 340 ms: 1.12x faster                                                       |
| generators                 | 31.2 ms                                                | 27.8 ms: 1.12x faster                                                      |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.10x faster                                                      |
| regex_effbot               | 3.61 ms                                                | 3.27 ms: 1.10x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 96.9 ms: 1.10x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.24 ms: 1.10x faster                                                      |
| django_template            | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 707 ms: 1.10x faster                                                       |
| 2to3                       | 274 ms                                                 | 250 ms: 1.10x faster                                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.54 ms: 1.09x faster                                                      |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 82.6 ms: 1.08x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.08x faster                                                       |
| docutils                   | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                     |
| sqlglot_normalize          | 110 ms                                                 | 103 ms: 1.07x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 63.8 ms: 1.07x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.45 sec: 1.07x faster                                                     |
| sympy_expand               | 478 ms                                                 | 447 ms: 1.07x faster                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 51.4 ms: 1.07x faster                                                      |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 58.1 ms: 1.06x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.76 ms: 1.06x faster                                                      |
| hexiom                     | 6.41 ms                                                | 6.05 ms: 1.06x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                     |
| fannkuch                   | 417 ms                                                 | 394 ms: 1.06x faster                                                       |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                      |
| nqueens                    | 83.3 ms                                                | 78.9 ms: 1.06x faster                                                      |
| nbody                      | 97.0 ms                                                | 92.1 ms: 1.05x faster                                                      |
| pyflate                    | 482 ms                                                 | 460 ms: 1.05x faster                                                       |
| richards                   | 45.8 ms                                                | 44.1 ms: 1.04x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 312 us: 1.04x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                       |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                                       |
| json                       | 5.26 ms                                                | 5.13 ms: 1.03x faster                                                      |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                      |
| richards_super             | 51.5 ms                                                | 50.5 ms: 1.02x faster                                                      |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 855 us: 1.02x slower                                                       |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.02x slower                                                      |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 25.6 ms: 1.11x slower                                                      |
| telco                      | 7.10 ms                                                | 7.98 ms: 1.12x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.13x slower                                                      |
| coverage                   | 72.7 ms                                                | 89.7 ms: 1.23x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 5.03 ms: 1.32x slower                                                      |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.68x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 80.5 ms: 3.35x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                               |

Benchmark hidden because not significant (2): typing_runtime_protocols, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250204-3.14.0a4+-875bc77/bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.122x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.09x