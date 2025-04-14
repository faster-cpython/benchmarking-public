# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.112x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 264 ms: 1.04x faster                                                   |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                                   |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.48x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.1 ms: 1.30x faster                                                  |
| nbody          | 97.0 ms                                                | 88.1 ms: 1.10x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.55 ms: 1.02x faster                                                  |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.04x slower                                                  |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 79.9 ms: 1.12x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 97.3 ms: 1.10x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 56.6 ms: 1.09x faster                                                  |
| unpickle             | 15.9 us                                                | 14.6 us: 1.08x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.08x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                   |
| pickle_dict          | 35.5 us                                                | 35.9 us: 1.01x slower                                                  |
| pickle_list          | 5.08 us                                                | 5.24 us: 1.03x slower                                                  |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                                  |
| unpickle_list        | 5.29 us                                                | 5.56 us: 1.05x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                  |
| pickle               | 11.6 us                                                | 13.0 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.15 ms: 1.18x slower                                                  |
| python_startup         | 9.55 ms                                                | 13.0 ms: 1.37x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                  |
| django_template | 34.6 ms                                                | 32.2 ms: 1.08x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                                   |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.48x faster                                                   |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 28.9 us: 1.41x faster                                                  |
| float                      | 84.7 ms                                                | 65.1 ms: 1.30x faster                                                  |
| richards                   | 45.8 ms                                                | 36.4 ms: 1.26x faster                                                  |
| richards_super             | 51.5 ms                                                | 41.3 ms: 1.25x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.23x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.05 ms: 1.22x faster                                                  |
| scimark_fft                | 382 ms                                                 | 317 ms: 1.21x faster                                                   |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                  |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                   |
| raytrace                   | 312 ms                                                 | 268 ms: 1.17x faster                                                   |
| spectral_norm              | 115 ms                                                 | 98.8 ms: 1.16x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                                  |
| comprehensions             | 21.8 us                                                | 19.0 us: 1.15x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 59.9 ms: 1.14x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 79.9 ms: 1.12x faster                                                  |
| pyflate                    | 482 ms                                                 | 434 ms: 1.11x faster                                                   |
| chaos                      | 67.0 ms                                                | 60.3 ms: 1.11x faster                                                  |
| generators                 | 31.2 ms                                                | 28.2 ms: 1.11x faster                                                  |
| async_generators           | 463 ms                                                 | 418 ms: 1.11x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.10x faster                                                   |
| nbody                      | 97.0 ms                                                | 88.1 ms: 1.10x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 97.3 ms: 1.10x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.1 ms: 1.10x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 56.6 ms: 1.09x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 68.9 ms: 1.09x faster                                                  |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                                   |
| unpickle                   | 15.9 us                                                | 14.6 us: 1.08x faster                                                  |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                  |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.08x faster                                                   |
| logging_silent             | 104 ns                                                 | 97.0 ns: 1.08x faster                                                  |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.08x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.71 ms: 1.07x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.46 sec: 1.07x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.07x faster                                                  |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.06x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.70 us: 1.05x faster                                                  |
| 2to3                       | 274 ms                                                 | 264 ms: 1.04x faster                                                   |
| asyncio_tcp                | 491 ms                                                 | 477 ms: 1.03x faster                                                   |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.03x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 79.9 ms: 1.02x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.55 ms: 1.02x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 764 ms: 1.01x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                   |
| sympy_expand               | 478 ms                                                 | 475 ms: 1.01x faster                                                   |
| fannkuch                   | 417 ms                                                 | 415 ms: 1.00x faster                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                 |
| pickle_dict                | 35.5 us                                                | 35.9 us: 1.01x slower                                                  |
| nqueens                    | 83.3 ms                                                | 84.1 ms: 1.01x slower                                                  |
| coroutines                 | 23.2 ms                                                | 23.7 ms: 1.02x slower                                                  |
| pickle_list                | 5.08 us                                                | 5.24 us: 1.03x slower                                                  |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.04x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 880 us: 1.05x slower                                                   |
| unpickle_list              | 5.29 us                                                | 5.56 us: 1.05x slower                                                  |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                   |
| hexiom                     | 6.41 ms                                                | 6.90 ms: 1.08x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                  |
| pickle                     | 11.6 us                                                | 13.0 us: 1.12x slower                                                  |
| telco                      | 7.10 ms                                                | 8.06 ms: 1.13x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 8.15 ms: 1.18x slower                                                  |
| coverage                   | 72.7 ms                                                | 87.0 ms: 1.20x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.64 ms: 1.22x slower                                                  |
| unpack_sequence            | 54.0 ns                                                | 73.4 ns: 1.36x slower                                                  |
| python_startup             | 9.55 ms                                                | 13.0 ms: 1.37x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 82.5 ms: 3.44x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (3): asyncio_websockets, json, pycparser
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.112x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.12x