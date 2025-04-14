# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: lto_fix
- machine: linux-x86_64
- commit hash: 8891cd2
- commit date: 2025-04-07
- overall geometric mean: 1.062x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 274 ms: 1.04x faster                                                      |
| docutils       | 2.87 sec                                                     | 2.85 sec: 1.01x faster                                                    |
| Geometric mean | (ref)                                                        | 1.02x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 631 ms: 1.67x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 629 ms: 1.66x faster                                                      |
| async_tree_memoization     | 544 ms                                                       | 332 ms: 1.64x faster                                                      |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                      |
| async_tree_none            | 452 ms                                                       | 285 ms: 1.58x faster                                                      |
| async_tree_none_tg         | 431 ms                                                       | 273 ms: 1.58x faster                                                      |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 499 ms: 1.40x faster                                                      |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 504 ms: 1.38x faster                                                      |
| Geometric mean             | (ref)                                                        | 1.56x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 68.1 ms: 1.13x faster                                                     |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                      |
| nbody          | 88.0 ms                                                      | 93.4 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                        | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.12 ms: 1.15x faster                                                     |
| regex_compile  | 144 ms                                                       | 133 ms: 1.08x faster                                                      |
| regex_dna      | 239 ms                                                       | 238 ms: 1.00x faster                                                      |
| regex_v8       | 23.6 ms                                                      | 24.4 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                        | 1.05x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 2.06 sec: 1.05x faster                                                    |
| xml_etree_iterparse  | 103 ms                                                       | 98.4 ms: 1.05x faster                                                     |
| xml_etree_parse      | 144 ms                                                       | 139 ms: 1.04x faster                                                      |
| xml_etree_generate   | 86.1 ms                                                      | 84.1 ms: 1.02x faster                                                     |
| unpickle_pure_python | 210 us                                                       | 210 us: 1.00x slower                                                      |
| pickle_pure_python   | 318 us                                                       | 328 us: 1.03x slower                                                      |
| json_loads           | 24.4 us                                                      | 26.7 us: 1.10x slower                                                     |
| json_dumps           | 10.2 ms                                                      | 11.3 ms: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                              |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                     |
| python_startup         | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.8 ms: 1.07x faster                                                     |
| mako            | 10.0 ms                                                      | 11.1 ms: 1.11x slower                                                     |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.30 sec: 1.98x faster                                                    |
| async_tree_io_tg           | 1.05 sec                                                     | 631 ms: 1.67x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 629 ms: 1.66x faster                                                      |
| async_tree_memoization     | 544 ms                                                       | 332 ms: 1.64x faster                                                      |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                      |
| async_tree_none            | 452 ms                                                       | 285 ms: 1.58x faster                                                      |
| async_tree_none_tg         | 431 ms                                                       | 273 ms: 1.58x faster                                                      |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 499 ms: 1.40x faster                                                      |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 504 ms: 1.38x faster                                                      |
| deepcopy                   | 368 us                                                       | 274 us: 1.35x faster                                                      |
| deepcopy_memo              | 36.8 us                                                      | 27.9 us: 1.32x faster                                                     |
| generators                 | 37.4 ms                                                      | 28.9 ms: 1.30x faster                                                     |
| comprehensions             | 21.9 us                                                      | 17.7 us: 1.24x faster                                                     |
| go                         | 150 ms                                                       | 126 ms: 1.18x faster                                                      |
| scimark_monte_carlo        | 69.0 ms                                                      | 58.3 ms: 1.18x faster                                                     |
| deepcopy_reduce            | 3.37 us                                                      | 2.86 us: 1.18x faster                                                     |
| regex_effbot               | 3.57 ms                                                      | 3.12 ms: 1.15x faster                                                     |
| float                      | 76.6 ms                                                      | 68.1 ms: 1.13x faster                                                     |
| pathlib                    | 18.9 ms                                                      | 16.9 ms: 1.12x faster                                                     |
| raytrace                   | 298 ms                                                       | 268 ms: 1.11x faster                                                      |
| logging_format             | 7.48 us                                                      | 6.81 us: 1.10x faster                                                     |
| chaos                      | 64.0 ms                                                      | 59.0 ms: 1.08x faster                                                     |
| sqlalchemy_declarative     | 159 ms                                                       | 147 ms: 1.08x faster                                                      |
| sympy_integrate            | 23.9 ms                                                      | 22.1 ms: 1.08x faster                                                     |
| regex_compile              | 144 ms                                                       | 133 ms: 1.08x faster                                                      |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.08x faster                                                      |
| logging_simple             | 6.71 us                                                      | 6.28 us: 1.07x faster                                                     |
| django_template            | 38.2 ms                                                      | 35.8 ms: 1.07x faster                                                     |
| coroutines                 | 23.0 ms                                                      | 21.6 ms: 1.06x faster                                                     |
| sympy_str                  | 302 ms                                                       | 286 ms: 1.06x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.8 ms: 1.05x faster                                                     |
| dulwich_log                | 65.4 ms                                                      | 62.0 ms: 1.05x faster                                                     |
| tomli_loads                | 2.16 sec                                                     | 2.06 sec: 1.05x faster                                                    |
| pprint_pformat             | 1.65 sec                                                     | 1.58 sec: 1.05x faster                                                    |
| xml_etree_iterparse        | 103 ms                                                       | 98.4 ms: 1.05x faster                                                     |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                      |
| pprint_safe_repr           | 807 ms                                                       | 773 ms: 1.04x faster                                                      |
| scimark_sor                | 109 ms                                                       | 104 ms: 1.04x faster                                                      |
| pyflate                    | 439 ms                                                       | 421 ms: 1.04x faster                                                      |
| 2to3                       | 285 ms                                                       | 274 ms: 1.04x faster                                                      |
| scimark_lu                 | 98.8 ms                                                      | 94.9 ms: 1.04x faster                                                     |
| xml_etree_parse            | 144 ms                                                       | 139 ms: 1.04x faster                                                      |
| meteor_contest             | 128 ms                                                       | 124 ms: 1.03x faster                                                      |
| logging_silent             | 94.4 ns                                                      | 92.0 ns: 1.03x faster                                                     |
| xml_etree_generate         | 86.1 ms                                                      | 84.1 ms: 1.02x faster                                                     |
| spectral_norm              | 91.6 ms                                                      | 89.5 ms: 1.02x faster                                                     |
| deltablue                  | 3.24 ms                                                      | 3.19 ms: 1.01x faster                                                     |
| crypto_pyaes               | 80.3 ms                                                      | 79.4 ms: 1.01x faster                                                     |
| docutils                   | 2.87 sec                                                     | 2.85 sec: 1.01x faster                                                    |
| regex_dna                  | 239 ms                                                       | 238 ms: 1.00x faster                                                      |
| unpickle_pure_python       | 210 us                                                       | 210 us: 1.00x slower                                                      |
| sqlite_synth               | 2.77 us                                                      | 2.83 us: 1.02x slower                                                     |
| bench_thread_pool          | 950 us                                                       | 974 us: 1.03x slower                                                      |
| regex_v8                   | 23.6 ms                                                      | 24.4 ms: 1.03x slower                                                     |
| pickle_pure_python         | 318 us                                                       | 328 us: 1.03x slower                                                      |
| fannkuch                   | 350 ms                                                       | 363 ms: 1.04x slower                                                      |
| async_generators           | 390 ms                                                       | 407 ms: 1.04x slower                                                      |
| nqueens                    | 89.9 ms                                                      | 94.1 ms: 1.05x slower                                                     |
| hexiom                     | 5.96 ms                                                      | 6.27 ms: 1.05x slower                                                     |
| nbody                      | 88.0 ms                                                      | 93.4 ms: 1.06x slower                                                     |
| json                       | 5.12 ms                                                      | 5.44 ms: 1.06x slower                                                     |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.59 ms: 1.09x slower                                                     |
| json_loads                 | 24.4 us                                                      | 26.7 us: 1.10x slower                                                     |
| json_dumps                 | 10.2 ms                                                      | 11.3 ms: 1.10x slower                                                     |
| telco                      | 6.96 ms                                                      | 7.72 ms: 1.11x slower                                                     |
| mako                       | 10.0 ms                                                      | 11.1 ms: 1.11x slower                                                     |
| typing_runtime_protocols   | 152 us                                                       | 170 us: 1.12x slower                                                      |
| python_startup_no_site     | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                     |
| coverage                   | 66.7 ms                                                      | 81.8 ms: 1.23x slower                                                     |
| python_startup             | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                     |
| create_gc_cycles           | 1.59 ms                                                      | 2.80 ms: 1.76x slower                                                     |
| gc_traversal               | 3.48 ms                                                      | 6.58 ms: 1.89x slower                                                     |
| bench_mp_pool              | 4.76 ms                                                      | 1.09 sec: 228.30x slower                                                  |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                              |

Benchmark hidden because not significant (7): richards, scimark_fft, xml_etree_process, sympy_expand, richards_super, pycparser, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250407-3.14.0a6+-8891cd2/bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.062x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x