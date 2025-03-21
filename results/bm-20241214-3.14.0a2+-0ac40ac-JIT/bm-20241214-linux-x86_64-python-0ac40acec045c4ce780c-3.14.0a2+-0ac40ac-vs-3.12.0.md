# Results vs. 3.12.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-x86_64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.102x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                   |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 627 ms: 1.88x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 619 ms: 1.87x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                   |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 336 ms: 1.72x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.6 ms: 1.17x faster                                                  |
| float          | 84.7 ms                                                | 73.3 ms: 1.16x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.24 ms: 1.11x faster                                                  |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                   |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 193 us: 1.19x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 137 ms: 1.16x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 78.3 ms: 1.14x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 94.5 ms: 1.13x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 55.7 ms: 1.11x faster                                                  |
| json_loads           | 28.5 us                                                | 26.0 us: 1.09x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                                   |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.3 ms: 1.15x faster                                                  |
| django_template | 34.6 ms                                                | 33.9 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 627 ms: 1.88x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 619 ms: 1.87x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                   |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 336 ms: 1.72x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                   |
| deepcopy                   | 371 us                                                 | 270 us: 1.37x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.37x faster                                                  |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                 |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.76 us: 1.21x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 62.0 ms: 1.21x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 68.0 ms: 1.20x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 193 us: 1.19x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                  |
| nbody                      | 97.0 ms                                                | 82.6 ms: 1.17x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 137 ms: 1.16x faster                                                   |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                   |
| float                      | 84.7 ms                                                | 73.3 ms: 1.16x faster                                                  |
| mako                       | 11.9 ms                                                | 10.3 ms: 1.15x faster                                                  |
| logging_format             | 7.23 us                                                | 6.27 us: 1.15x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 78.3 ms: 1.14x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.13x faster                                                   |
| scimark_sor                | 129 ms                                                 | 114 ms: 1.13x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.71 us: 1.13x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 94.5 ms: 1.13x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.29 ms: 1.13x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.7 ms: 1.12x faster                                                  |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.24 ms: 1.11x faster                                                  |
| go                         | 139 ms                                                 | 125 ms: 1.11x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 55.7 ms: 1.11x faster                                                  |
| raytrace                   | 312 ms                                                 | 284 ms: 1.10x faster                                                   |
| json_loads                 | 28.5 us                                                | 26.0 us: 1.09x faster                                                  |
| json                       | 5.26 ms                                                | 4.81 ms: 1.09x faster                                                  |
| chaos                      | 67.0 ms                                                | 61.5 ms: 1.09x faster                                                  |
| fannkuch                   | 417 ms                                                 | 385 ms: 1.08x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.08x faster                                                   |
| pyflate                    | 482 ms                                                 | 452 ms: 1.07x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.74 ms: 1.07x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                  |
| sympy_str                  | 300 ms                                                 | 283 ms: 1.06x faster                                                   |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.05x faster                                                  |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                   |
| async_generators           | 463 ms                                                 | 446 ms: 1.04x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 20.8 ms: 1.03x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 752 ms: 1.03x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                 |
| richards                   | 45.8 ms                                                | 44.7 ms: 1.03x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 66.9 ms: 1.02x faster                                                  |
| django_template            | 34.6 ms                                                | 33.9 ms: 1.02x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                  |
| mdp                        | 2.63 sec                                               | 2.69 sec: 1.02x slower                                                 |
| logging_silent             | 104 ns                                                 | 107 ns: 1.03x slower                                                   |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 887 us: 1.05x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                  |
| telco                      | 7.10 ms                                                | 7.59 ms: 1.07x slower                                                  |
| nqueens                    | 83.3 ms                                                | 89.1 ms: 1.07x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                  |
| hexiom                     | 6.41 ms                                                | 7.03 ms: 1.10x slower                                                  |
| generators                 | 31.2 ms                                                | 34.6 ms: 1.11x slower                                                  |
| coverage                   | 72.7 ms                                                | 84.1 ms: 1.16x slower                                                  |
| mypy2                      | 830 ms                                                 | 965 ms: 1.16x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 4.95 ms: 1.31x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.38x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (6): scimark_lu, richards_super, sqlglot_optimize, coroutines, sympy_expand, pycparser
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.102x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.11x