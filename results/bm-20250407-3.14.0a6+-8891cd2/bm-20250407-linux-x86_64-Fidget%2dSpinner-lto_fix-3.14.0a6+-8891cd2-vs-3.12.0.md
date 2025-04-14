# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: lto_fix
- machine: linux-x86_64
- commit hash: 8891cd2
- commit date: 2025-04-07
- overall geometric mean: 1.137x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 250 ms: 1.10x faster                                                |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                              |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 609 ms: 1.94x faster                                                |
| async_tree_io              | 1.16 sec                                               | 606 ms: 1.91x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                                |
| async_tree_none            | 472 ms                                                 | 255 ms: 1.85x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 246 ms: 1.82x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 484 ms: 1.50x faster                                                |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 67.3 ms: 1.26x faster                                               |
| nbody          | 97.0 ms                                                | 91.0 ms: 1.07x faster                                               |
| pidigits       | 187 ms                                                 | 194 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 124 ms: 1.20x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.04 ms: 1.19x faster                                               |
| regex_dna      | 212 ms                                                 | 205 ms: 1.04x faster                                                |
| regex_v8       | 23.1 ms                                                | 22.7 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.11x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 97.8 ms: 1.09x faster                                               |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 84.2 ms: 1.06x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 58.5 ms: 1.06x faster                                               |
| pickle_pure_python   | 324 us                                                 | 314 us: 1.03x faster                                                |
| json_loads           | 28.5 us                                                | 29.0 us: 1.02x slower                                               |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                               |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.20 ms: 1.18x slower                                               |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.5 ms: 1.10x faster                                               |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                               |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.16x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 609 ms: 1.94x faster                                                |
| async_tree_io              | 1.16 sec                                               | 606 ms: 1.91x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                                |
| async_tree_none            | 472 ms                                                 | 255 ms: 1.85x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 246 ms: 1.82x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 484 ms: 1.50x faster                                                |
| deepcopy                   | 371 us                                                 | 251 us: 1.48x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 28.2 us: 1.44x faster                                               |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                               |
| go                         | 139 ms                                                 | 109 ms: 1.28x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                               |
| float                      | 84.7 ms                                                | 67.3 ms: 1.26x faster                                               |
| raytrace                   | 312 ms                                                 | 259 ms: 1.20x faster                                                |
| logging_format             | 7.23 us                                                | 6.03 us: 1.20x faster                                               |
| regex_compile              | 148 ms                                                 | 124 ms: 1.20x faster                                                |
| chaos                      | 67.0 ms                                                | 56.2 ms: 1.19x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.04 ms: 1.19x faster                                               |
| logging_simple             | 6.46 us                                                | 5.46 us: 1.18x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                              |
| async_generators           | 463 ms                                                 | 392 ms: 1.18x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.18x faster                                               |
| dulwich_log                | 68.5 ms                                                | 59.3 ms: 1.16x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 65.1 ms: 1.15x faster                                               |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 72.7 ms: 1.13x faster                                               |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.7 ms: 1.12x faster                                               |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.12x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 19.2 ms: 1.12x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.33 ms: 1.11x faster                                               |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                                |
| scimark_fft                | 382 ms                                                 | 346 ms: 1.10x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 704 ms: 1.10x faster                                                |
| pyflate                    | 482 ms                                                 | 439 ms: 1.10x faster                                                |
| django_template            | 34.6 ms                                                | 31.5 ms: 1.10x faster                                               |
| 2to3                       | 274 ms                                                 | 250 ms: 1.10x faster                                                |
| logging_silent             | 104 ns                                                 | 95.5 ns: 1.09x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 97.8 ms: 1.09x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                              |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                              |
| generators                 | 31.2 ms                                                | 29.2 ms: 1.07x faster                                               |
| nbody                      | 97.0 ms                                                | 91.0 ms: 1.07x faster                                               |
| richards                   | 45.8 ms                                                | 43.1 ms: 1.06x faster                                               |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 84.2 ms: 1.06x faster                                               |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 58.5 ms: 1.06x faster                                               |
| sympy_expand               | 478 ms                                                 | 454 ms: 1.05x faster                                                |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.86 ms: 1.04x faster                                               |
| richards_super             | 51.5 ms                                                | 49.5 ms: 1.04x faster                                               |
| regex_dna                  | 212 ms                                                 | 205 ms: 1.04x faster                                                |
| pickle_pure_python         | 324 us                                                 | 314 us: 1.03x faster                                                |
| fannkuch                   | 417 ms                                                 | 406 ms: 1.03x faster                                                |
| hexiom                     | 6.41 ms                                                | 6.24 ms: 1.03x faster                                               |
| nqueens                    | 83.3 ms                                                | 81.3 ms: 1.02x faster                                               |
| regex_v8                   | 23.1 ms                                                | 22.7 ms: 1.02x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                               |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                |
| json                       | 5.26 ms                                                | 5.21 ms: 1.01x faster                                               |
| json_loads                 | 28.5 us                                                | 29.0 us: 1.02x slower                                               |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                               |
| pidigits                   | 187 ms                                                 | 194 ms: 1.04x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                |
| bench_thread_pool          | 842 us                                                 | 877 us: 1.04x slower                                                |
| telco                      | 7.10 ms                                                | 7.68 ms: 1.08x slower                                               |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                               |
| coverage                   | 72.7 ms                                                | 85.8 ms: 1.18x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 8.20 ms: 1.18x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.79 ms: 1.26x slower                                               |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.1 ms: 3.42x slower                                               |
| Geometric mean             | (ref)                                                  | 1.12x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250407-3.14.0a6+-8891cd2/bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.137x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.10x