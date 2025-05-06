# Results vs. 3.12.0

- fork: iritkatriel
- ref: array_subscr
- machine: linux-x86_64
- commit hash: 454bfc5
- commit date: 2025-05-05
- overall geometric mean: 1.115x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 601 ms: 1.97x faster                                                |
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 308 ms: 1.87x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                                |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 493 ms: 1.47x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 503 ms: 1.44x faster                                                |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.9 ms: 1.29x faster                                               |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                |
| nbody          | 97.0 ms                                                | 98.1 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.08x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.35 ms: 1.08x faster                                               |
| regex_dna      | 212 ms                                                 | 208 ms: 1.02x faster                                                |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.23x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                |
| unpickle_pure_python | 230 us                                                 | 207 us: 1.11x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 80.7 ms: 1.10x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 56.2 ms: 1.10x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                               |
| json_loads           | 28.5 us                                                | 30.2 us: 1.06x slower                                               |
| json_dumps           | 10.4 ms                                                | 12.0 ms: 1.15x slower                                               |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.94 ms: 1.00x slower                                               |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                               |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                               |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 601 ms: 1.97x faster                                                |
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 308 ms: 1.87x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                                |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 493 ms: 1.47x faster                                                |
| deepcopy                   | 371 us                                                 | 255 us: 1.45x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 503 ms: 1.44x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.1 us: 1.40x faster                                               |
| richards                   | 45.8 ms                                                | 35.2 ms: 1.30x faster                                               |
| float                      | 84.7 ms                                                | 65.9 ms: 1.29x faster                                               |
| richards_super             | 51.5 ms                                                | 40.6 ms: 1.27x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.23x faster                                              |
| deltablue                  | 3.72 ms                                                | 3.07 ms: 1.21x faster                                               |
| comprehensions             | 21.8 us                                                | 18.1 us: 1.21x faster                                               |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                |
| go                         | 139 ms                                                 | 123 ms: 1.14x faster                                                |
| logging_format             | 7.23 us                                                | 6.36 us: 1.14x faster                                               |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                               |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                |
| dulwich_log                | 68.5 ms                                                | 60.6 ms: 1.13x faster                                               |
| logging_simple             | 6.46 us                                                | 5.72 us: 1.13x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 19.3 ms: 1.11x faster                                               |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 207 us: 1.11x faster                                                |
| raytrace                   | 312 ms                                                 | 282 ms: 1.11x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 80.7 ms: 1.10x faster                                               |
| pyflate                    | 482 ms                                                 | 438 ms: 1.10x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 56.2 ms: 1.10x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                               |
| chaos                      | 67.0 ms                                                | 61.6 ms: 1.09x faster                                               |
| spectral_norm              | 115 ms                                                 | 106 ms: 1.09x faster                                                |
| regex_effbot               | 3.61 ms                                                | 3.35 ms: 1.08x faster                                               |
| async_generators           | 463 ms                                                 | 431 ms: 1.07x faster                                                |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                               |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 735 ms: 1.06x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 77.9 ms: 1.05x faster                                               |
| generators                 | 31.2 ms                                                | 29.8 ms: 1.05x faster                                               |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                               |
| logging_silent             | 104 ns                                                 | 99.8 ns: 1.05x faster                                               |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                              |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                              |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.03x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.03x faster                                              |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.03x faster                                                |
| regex_dna                  | 212 ms                                                 | 208 ms: 1.02x faster                                                |
| sympy_expand               | 478 ms                                                 | 469 ms: 1.02x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.01x faster                                               |
| nqueens                    | 83.3 ms                                                | 82.1 ms: 1.01x faster                                               |
| fannkuch                   | 417 ms                                                 | 411 ms: 1.01x faster                                                |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                |
| python_startup_no_site     | 6.94 ms                                                | 6.94 ms: 1.00x slower                                               |
| nbody                      | 97.0 ms                                                | 98.1 ms: 1.01x slower                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 76.3 ms: 1.02x slower                                               |
| json                       | 5.26 ms                                                | 5.39 ms: 1.03x slower                                               |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                               |
| hexiom                     | 6.41 ms                                                | 6.70 ms: 1.05x slower                                               |
| scimark_lu                 | 118 ms                                                 | 124 ms: 1.05x slower                                                |
| json_loads                 | 28.5 us                                                | 30.2 us: 1.06x slower                                               |
| bench_thread_pool          | 842 us                                                 | 908 us: 1.08x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                                |
| scimark_fft                | 382 ms                                                 | 419 ms: 1.10x slower                                                |
| coroutines                 | 23.2 ms                                                | 25.7 ms: 1.11x slower                                               |
| telco                      | 7.10 ms                                                | 8.03 ms: 1.13x slower                                               |
| json_dumps                 | 10.4 ms                                                | 12.0 ms: 1.15x slower                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.29 ms: 1.24x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.99 ms: 1.32x slower                                               |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.69x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.8 ms: 3.45x slower                                               |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                        |

Benchmark hidden because not significant (2): pickle_pure_python, asyncio_websockets
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, coverage, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250505-3.14.0a7+-454bfc5-JIT/bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.115x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.13x