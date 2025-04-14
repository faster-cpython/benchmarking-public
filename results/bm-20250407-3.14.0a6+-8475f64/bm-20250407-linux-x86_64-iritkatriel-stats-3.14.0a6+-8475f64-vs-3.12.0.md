# Results vs. 3.12.0

- fork: iritkatriel
- ref: stats
- machine: linux-x86_64
- commit hash: 8475f64
- commit date: 2025-04-07
- overall geometric mean: 1.140x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 250 ms: 1.10x faster                                         |
| docutils       | 2.77 sec                                               | 2.57 sec: 1.08x faster                                       |
| Geometric mean | (ref)                                                  | 1.09x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 609 ms: 1.94x faster                                         |
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 307 ms: 1.88x faster                                         |
| async_tree_none            | 472 ms                                                 | 255 ms: 1.85x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 245 ms: 1.84x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 476 ms: 1.53x faster                                         |
| Geometric mean             | (ref)                                                  | 1.78x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 84.7 ms                                                | 66.3 ms: 1.28x faster                                        |
| nbody          | 97.0 ms                                                | 86.4 ms: 1.12x faster                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                  | 1.13x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 124 ms: 1.19x faster                                         |
| regex_effbot   | 3.61 ms                                                | 3.45 ms: 1.05x faster                                        |
| regex_v8       | 23.1 ms                                                | 22.5 ms: 1.03x faster                                        |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.22x faster                                       |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                         |
| xml_etree_iterparse  | 107 ms                                                 | 98.6 ms: 1.08x faster                                        |
| xml_etree_generate   | 89.2 ms                                                | 83.8 ms: 1.06x faster                                        |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                         |
| xml_etree_process    | 61.7 ms                                                | 58.6 ms: 1.05x faster                                        |
| pickle_pure_python   | 324 us                                                 | 313 us: 1.03x faster                                         |
| json_loads           | 28.5 us                                                | 29.9 us: 1.05x slower                                        |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.14x slower                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.21 ms: 1.18x slower                                        |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                        |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.3 ms: 1.11x faster                                        |
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                        |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.16x faster                                       |
| async_tree_io_tg           | 1.18 sec                                               | 609 ms: 1.94x faster                                         |
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 307 ms: 1.88x faster                                         |
| async_tree_none            | 472 ms                                                 | 255 ms: 1.85x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 245 ms: 1.84x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 476 ms: 1.53x faster                                         |
| deepcopy                   | 371 us                                                 | 245 us: 1.51x faster                                         |
| deepcopy_memo              | 40.7 us                                                | 28.6 us: 1.42x faster                                        |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.31x faster                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.57 us: 1.30x faster                                        |
| float                      | 84.7 ms                                                | 66.3 ms: 1.28x faster                                        |
| go                         | 139 ms                                                 | 110 ms: 1.27x faster                                         |
| raytrace                   | 312 ms                                                 | 254 ms: 1.23x faster                                         |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.22x faster                                       |
| chaos                      | 67.0 ms                                                | 55.6 ms: 1.20x faster                                        |
| regex_compile              | 148 ms                                                 | 124 ms: 1.19x faster                                         |
| logging_format             | 7.23 us                                                | 6.07 us: 1.19x faster                                        |
| async_generators           | 463 ms                                                 | 390 ms: 1.19x faster                                         |
| spectral_norm              | 115 ms                                                 | 97.0 ms: 1.18x faster                                        |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.18x faster                                        |
| logging_simple             | 6.46 us                                                | 5.48 us: 1.18x faster                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 64.0 ms: 1.17x faster                                        |
| dulwich_log                | 68.5 ms                                                | 59.0 ms: 1.16x faster                                        |
| scimark_fft                | 382 ms                                                 | 332 ms: 1.15x faster                                         |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                         |
| crypto_pyaes               | 81.9 ms                                                | 72.0 ms: 1.14x faster                                        |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                         |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.13x faster                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.12x faster                                        |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                         |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                         |
| nbody                      | 97.0 ms                                                | 86.4 ms: 1.12x faster                                        |
| deltablue                  | 3.72 ms                                                | 3.32 ms: 1.12x faster                                        |
| django_template            | 34.6 ms                                                | 31.3 ms: 1.11x faster                                        |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                         |
| 2to3                       | 274 ms                                                 | 250 ms: 1.10x faster                                         |
| pprint_safe_repr           | 776 ms                                                 | 712 ms: 1.09x faster                                         |
| xml_etree_iterparse        | 107 ms                                                 | 98.6 ms: 1.08x faster                                        |
| pyflate                    | 482 ms                                                 | 446 ms: 1.08x faster                                         |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                        |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.08x faster                                       |
| docutils                   | 2.77 sec                                               | 2.57 sec: 1.08x faster                                       |
| logging_silent             | 104 ns                                                 | 97.2 ns: 1.07x faster                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.73 ms: 1.07x faster                                        |
| richards                   | 45.8 ms                                                | 42.9 ms: 1.07x faster                                        |
| xml_etree_generate         | 89.2 ms                                                | 83.8 ms: 1.06x faster                                        |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                         |
| richards_super             | 51.5 ms                                                | 48.5 ms: 1.06x faster                                        |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                         |
| xml_etree_process          | 61.7 ms                                                | 58.6 ms: 1.05x faster                                        |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                         |
| generators                 | 31.2 ms                                                | 29.8 ms: 1.05x faster                                        |
| regex_effbot               | 3.61 ms                                                | 3.45 ms: 1.05x faster                                        |
| nqueens                    | 83.3 ms                                                | 80.4 ms: 1.04x faster                                        |
| pickle_pure_python         | 324 us                                                 | 313 us: 1.03x faster                                         |
| hexiom                     | 6.41 ms                                                | 6.21 ms: 1.03x faster                                        |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                       |
| regex_v8                   | 23.1 ms                                                | 22.5 ms: 1.03x faster                                        |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                        |
| fannkuch                   | 417 ms                                                 | 409 ms: 1.02x faster                                         |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.01x faster                                         |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                         |
| json                       | 5.26 ms                                                | 5.36 ms: 1.02x slower                                        |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                         |
| bench_thread_pool          | 842 us                                                 | 875 us: 1.04x slower                                         |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.04x slower                                         |
| json_loads                 | 28.5 us                                                | 29.9 us: 1.05x slower                                        |
| telco                      | 7.10 ms                                                | 7.79 ms: 1.10x slower                                        |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.14x slower                                        |
| coverage                   | 72.7 ms                                                | 85.4 ms: 1.17x slower                                        |
| python_startup_no_site     | 6.94 ms                                                | 8.21 ms: 1.18x slower                                        |
| gc_traversal               | 3.79 ms                                                | 4.60 ms: 1.21x slower                                        |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                        |
| bench_mp_pool              | 24.0 ms                                                | 82.3 ms: 3.43x slower                                        |
| Geometric mean             | (ref)                                                  | 1.12x faster                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250407-3.14.0a6+-8475f64/bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.140x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.10x