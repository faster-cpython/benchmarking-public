# Results vs. 3.12.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-x86_64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.096x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                   |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 627 ms: 1.84x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                   |
| async_tree_none            | 472 ms                                                 | 271 ms: 1.74x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 339 ms: 1.70x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 500 ms: 1.45x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 77.5 ms: 1.09x faster                                                  |
| nbody          | 97.0 ms                                                | 95.5 ms: 1.02x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.31 ms: 1.09x faster                                                  |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                   |
| regex_v8       | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.16x faster                                                   |
| tomli_loads          | 2.33 sec                                               | 2.04 sec: 1.14x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 97.3 ms: 1.10x faster                                                  |
| json_loads           | 28.5 us                                                | 27.1 us: 1.05x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 86.6 ms: 1.03x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                  |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                  |
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 627 ms: 1.84x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                   |
| async_tree_none            | 472 ms                                                 | 271 ms: 1.74x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 339 ms: 1.70x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 500 ms: 1.45x faster                                                   |
| deepcopy                   | 371 us                                                 | 268 us: 1.38x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 31.0 us: 1.31x faster                                                  |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.81 us: 1.19x faster                                                  |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.18x faster                                                  |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                                  |
| go                         | 139 ms                                                 | 120 ms: 1.16x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.16x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 127 ms: 1.15x faster                                                   |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 2.04 sec: 1.14x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.25 ms: 1.14x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.4 ms: 1.14x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 72.8 ms: 1.12x faster                                                  |
| async_generators           | 463 ms                                                 | 417 ms: 1.11x faster                                                   |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                                   |
| generators                 | 31.2 ms                                                | 28.2 ms: 1.11x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 68.1 ms: 1.10x faster                                                  |
| scimark_fft                | 382 ms                                                 | 347 ms: 1.10x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 97.3 ms: 1.10x faster                                                  |
| float                      | 84.7 ms                                                | 77.5 ms: 1.09x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.31 ms: 1.09x faster                                                  |
| chaos                      | 67.0 ms                                                | 61.4 ms: 1.09x faster                                                  |
| django_template            | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                  |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.07x faster                                                  |
| spectral_norm              | 115 ms                                                 | 108 ms: 1.06x faster                                                   |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 64.7 ms: 1.06x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 734 ms: 1.06x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 104 ms: 1.06x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                  |
| json_loads                 | 28.5 us                                                | 27.1 us: 1.05x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                   |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                   |
| json                       | 5.26 ms                                                | 5.05 ms: 1.04x faster                                                  |
| nqueens                    | 83.3 ms                                                | 80.0 ms: 1.04x faster                                                  |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                  |
| fannkuch                   | 417 ms                                                 | 401 ms: 1.04x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.87 ms: 1.04x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 52.8 ms: 1.04x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.03x faster                                                 |
| pyflate                    | 482 ms                                                 | 467 ms: 1.03x faster                                                   |
| scimark_sor                | 129 ms                                                 | 125 ms: 1.03x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 86.6 ms: 1.03x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.23 ms: 1.03x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                  |
| nbody                      | 97.0 ms                                                | 95.5 ms: 1.02x faster                                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                   |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                   |
| richards_super             | 51.5 ms                                                | 52.4 ms: 1.02x slower                                                  |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 862 us: 1.02x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                   |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                  |
| telco                      | 7.10 ms                                                | 7.85 ms: 1.11x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                  |
| coverage                   | 72.7 ms                                                | 83.2 ms: 1.14x slower                                                  |
| mypy2                      | 830 ms                                                 | 953 ms: 1.15x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 4.94 ms: 1.30x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.5 ms: 3.40x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (6): richards, pycparser, sqlite_synth, scimark_lu, pickle_pure_python, coroutines
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.096x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x