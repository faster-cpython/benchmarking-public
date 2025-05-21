# Results vs. 3.12.0

- fork: brandtbucher
- ref: cached_attributes
- machine: linux-x86_64
- commit hash: 0e20c44
- commit date: 2025-05-21
- overall geometric mean: 1.087x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                                     |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 595 ms: 1.94x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                                     |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.48x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 64.2 ms: 1.32x faster                                                    |
| nbody          | 97.0 ms                                                | 92.9 ms: 1.04x faster                                                    |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                  | 1.11x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.08 ms: 1.17x faster                                                    |
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                     |
| regex_dna      | 212 ms                                                 | 203 ms: 1.05x faster                                                     |
| regex_v8       | 23.1 ms                                                | 22.3 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.10x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 203 us: 1.13x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 97.4 ms: 1.10x faster                                                    |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                                    |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                             |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.94 ms: 1.00x slower                                                    |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.7 ms: 1.11x faster                                                    |
| django_template | 34.6 ms                                                | 32.5 ms: 1.07x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.12x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 595 ms: 1.94x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                                     |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.48x faster                                                     |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                     |
| richards                   | 45.8 ms                                                | 33.3 ms: 1.38x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 29.9 us: 1.36x faster                                                    |
| richards_super             | 51.5 ms                                                | 38.3 ms: 1.35x faster                                                    |
| float                      | 84.7 ms                                                | 64.2 ms: 1.32x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                                    |
| comprehensions             | 21.8 us                                                | 18.0 us: 1.21x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.08 ms: 1.21x faster                                                    |
| spectral_norm              | 115 ms                                                 | 97.9 ms: 1.17x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.08 ms: 1.17x faster                                                    |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                     |
| scimark_fft                | 382 ms                                                 | 332 ms: 1.15x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 203 us: 1.13x faster                                                     |
| pathlib                    | 19.3 ms                                                | 17.1 ms: 1.13x faster                                                    |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 61.2 ms: 1.12x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 67.2 ms: 1.12x faster                                                    |
| mako                       | 11.9 ms                                                | 10.7 ms: 1.11x faster                                                    |
| go                         | 139 ms                                                 | 125 ms: 1.11x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.10x faster                                                    |
| chaos                      | 67.0 ms                                                | 60.7 ms: 1.10x faster                                                    |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 97.4 ms: 1.10x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 75.3 ms: 1.09x faster                                                    |
| async_generators           | 463 ms                                                 | 428 ms: 1.08x faster                                                     |
| pyflate                    | 482 ms                                                 | 448 ms: 1.08x faster                                                     |
| django_template            | 34.6 ms                                                | 32.5 ms: 1.07x faster                                                    |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.06x faster                                                     |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                   |
| regex_dna                  | 212 ms                                                 | 203 ms: 1.05x faster                                                     |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                                     |
| nbody                      | 97.0 ms                                                | 92.9 ms: 1.04x faster                                                    |
| regex_v8                   | 23.1 ms                                                | 22.3 ms: 1.04x faster                                                    |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                   |
| logging_simple             | 6.46 us                                                | 6.28 us: 1.03x faster                                                    |
| logging_format             | 7.23 us                                                | 7.08 us: 1.02x faster                                                    |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                                     |
| generators                 | 31.2 ms                                                | 30.8 ms: 1.01x faster                                                    |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                     |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                    |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                     |
| python_startup_no_site     | 6.94 ms                                                | 6.94 ms: 1.00x slower                                                    |
| fannkuch                   | 417 ms                                                 | 420 ms: 1.01x slower                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.16 ms: 1.02x slower                                                    |
| json                       | 5.26 ms                                                | 5.37 ms: 1.02x slower                                                    |
| hexiom                     | 6.41 ms                                                | 6.60 ms: 1.03x slower                                                    |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                                    |
| coroutines                 | 23.2 ms                                                | 24.2 ms: 1.05x slower                                                    |
| pprint_safe_repr           | 776 ms                                                 | 812 ms: 1.05x slower                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.66 sec: 1.06x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                    |
| bench_thread_pool          | 842 us                                                 | 902 us: 1.07x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 173 us: 1.09x slower                                                     |
| telco                      | 7.10 ms                                                | 7.85 ms: 1.11x slower                                                    |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 4.93 ms: 1.30x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 2.57 ms: 1.74x slower                                                    |
| dask                       | 372 ms                                                 | 924 ms: 2.49x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 93.0 ms: 3.87x slower                                                    |
| logging_silent             | 104 ns                                                 | 469 ns: 4.49x slower                                                     |
| coverage                   | 72.7 ms                                                | 427 ms: 5.88x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (3): pickle_pure_python, asyncio_websockets, nqueens
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (24) of results/bm-20250521-3.15.0a0-0e20c44-JIT/bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.087x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.14x