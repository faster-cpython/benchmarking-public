# Results vs. 3.12.0

- fork: python
- ref: 1a9d4a1fb3d4beda7c7e
- machine: linux-x86_64
- commit hash: 1a9d4a1
- commit date: 2025-04-01
- overall geometric mean: 1.134x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                   |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.88x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                   |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 61.5 ms: 1.38x faster                                                  |
| nbody          | 97.0 ms                                                | 86.4 ms: 1.12x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.35 ms: 1.08x faster                                                  |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.83 sec: 1.27x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 79.4 ms: 1.12x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 209 us: 1.10x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 56.6 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 317 us: 1.02x faster                                                   |
| json_loads           | 28.5 us                                                | 29.6 us: 1.04x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.19 ms: 1.18x slower                                                  |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.9 ms: 1.10x faster                                                  |
| django_template | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.16x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.88x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                   |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                                   |
| deepcopy                   | 371 us                                                 | 252 us: 1.47x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 28.6 us: 1.42x faster                                                  |
| float                      | 84.7 ms                                                | 61.5 ms: 1.38x faster                                                  |
| richards                   | 45.8 ms                                                | 34.9 ms: 1.31x faster                                                  |
| richards_super             | 51.5 ms                                                | 39.7 ms: 1.30x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.83 sec: 1.27x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                                  |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.25x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.03 ms: 1.22x faster                                                  |
| raytrace                   | 312 ms                                                 | 259 ms: 1.21x faster                                                   |
| comprehensions             | 21.8 us                                                | 18.2 us: 1.19x faster                                                  |
| chaos                      | 67.0 ms                                                | 56.8 ms: 1.18x faster                                                  |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                   |
| logging_format             | 7.23 us                                                | 6.15 us: 1.18x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.17x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                                  |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.14x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 60.2 ms: 1.14x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 66.0 ms: 1.14x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                   |
| go                         | 139 ms                                                 | 123 ms: 1.13x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.12x faster                                                   |
| pyflate                    | 482 ms                                                 | 429 ms: 1.12x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 79.4 ms: 1.12x faster                                                  |
| nbody                      | 97.0 ms                                                | 86.4 ms: 1.12x faster                                                  |
| async_generators           | 463 ms                                                 | 414 ms: 1.12x faster                                                   |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 209 us: 1.10x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.10x faster                                                   |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 74.4 ms: 1.10x faster                                                  |
| mako                       | 11.9 ms                                                | 10.9 ms: 1.10x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.1 ms: 1.09x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 56.6 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.64 ms: 1.09x faster                                                  |
| logging_silent             | 104 ns                                                 | 95.9 ns: 1.09x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.35 ms: 1.08x faster                                                  |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                   |
| django_template            | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                  |
| generators                 | 31.2 ms                                                | 29.5 ms: 1.06x faster                                                  |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 750 ms: 1.03x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 317 us: 1.02x faster                                                   |
| sympy_expand               | 478 ms                                                 | 469 ms: 1.02x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| fannkuch                   | 417 ms                                                 | 415 ms: 1.00x faster                                                   |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.01x slower                                                  |
| nqueens                    | 83.3 ms                                                | 84.7 ms: 1.02x slower                                                  |
| json_loads                 | 28.5 us                                                | 29.6 us: 1.04x slower                                                  |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                   |
| hexiom                     | 6.41 ms                                                | 6.70 ms: 1.04x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 890 us: 1.06x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 173 us: 1.10x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                  |
| telco                      | 7.10 ms                                                | 8.02 ms: 1.13x slower                                                  |
| coverage                   | 72.7 ms                                                | 85.1 ms: 1.17x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 8.19 ms: 1.18x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.82 ms: 1.27x slower                                                  |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.50 ms: 1.69x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 82.7 ms: 3.44x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (4): pycparser, asyncio_websockets, json, regex_v8
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250401-3.14.0a6+-1a9d4a1-JIT/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.134x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.12x