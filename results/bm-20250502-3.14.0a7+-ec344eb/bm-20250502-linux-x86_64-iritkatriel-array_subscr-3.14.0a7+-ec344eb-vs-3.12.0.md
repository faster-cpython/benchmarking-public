# Results vs. 3.12.0

- fork: iritkatriel
- ref: array_subscr
- machine: linux-x86_64
- commit hash: ec344eb
- commit date: 2025-05-02
- overall geometric mean: 1.117x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-ec344eb |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 253 ms: 1.08x faster                                                |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.06x faster                                              |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-ec344eb |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 594 ms: 1.95x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 307 ms: 1.87x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                                |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 499 ms: 1.45x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 504 ms: 1.44x faster                                                |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-ec344eb |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.5 ms: 1.18x faster                                               |
| nbody          | 97.0 ms                                                | 98.4 ms: 1.01x slower                                               |
| pidigits       | 187 ms                                                 | 194 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-ec344eb |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.32 ms: 1.09x faster                                               |
| regex_dna      | 212 ms                                                 | 204 ms: 1.04x faster                                                |
| regex_v8       | 23.1 ms                                                | 23.0 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-ec344eb |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.99 sec: 1.17x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 143 ms: 1.12x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.08x faster                                               |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 85.2 ms: 1.05x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 59.0 ms: 1.05x faster                                               |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                |
| json_loads           | 28.5 us                                                | 29.6 us: 1.04x slower                                               |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.12x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-ec344eb |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.91 ms: 1.00x faster                                               |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-ec344eb |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.7 ms: 1.09x faster                                               |
| mako            | 11.9 ms                                                | 11.8 ms: 1.01x faster                                               |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-ec344eb |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.21 sec: 2.17x faster                                              |
| async_tree_io              | 1.16 sec                                               | 594 ms: 1.95x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 307 ms: 1.87x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                                |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 499 ms: 1.45x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 504 ms: 1.44x faster                                                |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                               |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                               |
| go                         | 139 ms                                                 | 111 ms: 1.25x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                               |
| float                      | 84.7 ms                                                | 71.5 ms: 1.18x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.99 sec: 1.17x faster                                              |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                |
| logging_format             | 7.23 us                                                | 6.22 us: 1.16x faster                                               |
| dulwich_log                | 68.5 ms                                                | 59.3 ms: 1.16x faster                                               |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                               |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                |
| async_generators           | 463 ms                                                 | 405 ms: 1.14x faster                                                |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                               |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.12x faster                                               |
| chaos                      | 67.0 ms                                                | 59.6 ms: 1.12x faster                                               |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 143 ms: 1.12x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.38 ms: 1.10x faster                                               |
| pyflate                    | 482 ms                                                 | 440 ms: 1.10x faster                                                |
| django_template            | 34.6 ms                                                | 31.7 ms: 1.09x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.32 ms: 1.09x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.08x faster                                               |
| 2to3                       | 274 ms                                                 | 253 ms: 1.08x faster                                                |
| spectral_norm              | 115 ms                                                 | 107 ms: 1.07x faster                                                |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 76.8 ms: 1.07x faster                                               |
| generators                 | 31.2 ms                                                | 29.5 ms: 1.06x faster                                               |
| richards                   | 45.8 ms                                                | 43.4 ms: 1.06x faster                                               |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.06x faster                                              |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 738 ms: 1.05x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                              |
| xml_etree_generate         | 89.2 ms                                                | 85.2 ms: 1.05x faster                                               |
| xml_etree_process          | 61.7 ms                                                | 59.0 ms: 1.05x faster                                               |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                              |
| sympy_expand               | 478 ms                                                 | 458 ms: 1.04x faster                                                |
| regex_dna                  | 212 ms                                                 | 204 ms: 1.04x faster                                                |
| richards_super             | 51.5 ms                                                | 49.8 ms: 1.03x faster                                               |
| nqueens                    | 83.3 ms                                                | 80.7 ms: 1.03x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 72.9 ms: 1.03x faster                                               |
| fannkuch                   | 417 ms                                                 | 409 ms: 1.02x faster                                                |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                |
| hexiom                     | 6.41 ms                                                | 6.37 ms: 1.01x faster                                               |
| mako                       | 11.9 ms                                                | 11.8 ms: 1.01x faster                                               |
| regex_v8                   | 23.1 ms                                                | 23.0 ms: 1.01x faster                                               |
| python_startup_no_site     | 6.94 ms                                                | 6.91 ms: 1.00x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.85 us: 1.01x slower                                               |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.01x slower                                                |
| nbody                      | 97.0 ms                                                | 98.4 ms: 1.01x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                |
| pidigits                   | 187 ms                                                 | 194 ms: 1.04x slower                                                |
| json_loads                 | 28.5 us                                                | 29.6 us: 1.04x slower                                               |
| scimark_fft                | 382 ms                                                 | 397 ms: 1.04x slower                                                |
| bench_thread_pool          | 842 us                                                 | 889 us: 1.06x slower                                                |
| coroutines                 | 23.2 ms                                                | 25.3 ms: 1.09x slower                                               |
| telco                      | 7.10 ms                                                | 7.88 ms: 1.11x slower                                               |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.12x slower                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.90 ms: 1.17x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.62 ms: 1.22x slower                                               |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.38x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.68x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.8 ms: 3.45x slower                                               |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                        |

Benchmark hidden because not significant (2): asyncio_websockets, json
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, coverage, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250502-3.14.0a7+-ec344eb/bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-ec344eb.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.117x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.11x