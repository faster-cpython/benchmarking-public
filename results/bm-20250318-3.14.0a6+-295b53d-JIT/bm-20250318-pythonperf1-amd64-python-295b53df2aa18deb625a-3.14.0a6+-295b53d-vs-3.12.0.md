# Results vs. 3.12.0

- fork: python
- ref: 295b53df2aa18deb625a
- machine: windows-amd64
- commit hash: 295b53d
- commit date: 2025-03-18
- overall geometric mean: 1.055x faster
- HPT reliability: 82.85%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.75 sec: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 411 ms: 1.88x faster                                                        |
| async_tree_io              | 731 ms                                                      | 418 ms: 1.75x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 175 ms: 1.63x faster                                                        |
| async_tree_none            | 291 ms                                                      | 186 ms: 1.56x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 221 ms: 1.53x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 338 ms: 1.48x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 341 ms: 1.44x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.62x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 58.6 ms: 1.23x faster                                                       |
| float          | 56.8 ms                                                     | 47.3 ms: 1.20x faster                                                       |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.45 ms: 1.11x faster                                                       |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 86.2 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.22 sec: 1.12x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 87.6 ms: 1.06x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 126 us: 1.06x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 53.0 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 38.9 ms: 1.03x slower                                                       |
| json_loads           | 13.9 us                                                     | 15.3 us: 1.10x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 222 us: 1.13x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.98 ms: 1.22x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.6 ms: 1.27x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.81 ms: 1.22x faster                                                       |
| django_template | 22.9 ms                                                     | 26.2 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.03x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.7 ms: 2.46x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 411 ms: 1.88x faster                                                        |
| async_tree_io              | 731 ms                                                      | 418 ms: 1.75x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 175 ms: 1.63x faster                                                        |
| async_tree_none            | 291 ms                                                      | 186 ms: 1.56x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 221 ms: 1.53x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 338 ms: 1.48x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 341 ms: 1.44x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 18.0 us: 1.32x faster                                                       |
| deepcopy                   | 238 us                                                      | 193 us: 1.24x faster                                                        |
| nbody                      | 71.9 ms                                                     | 58.6 ms: 1.23x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.81 ms: 1.22x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.7 us: 1.21x faster                                                       |
| float                      | 56.8 ms                                                     | 47.3 ms: 1.20x faster                                                       |
| scimark_fft                | 184 ms                                                      | 158 ms: 1.17x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.53 us: 1.15x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 58.8 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.27 ms: 1.12x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.22 sec: 1.12x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.45 ms: 1.11x faster                                                       |
| generators                 | 22.5 ms                                                     | 20.6 ms: 1.10x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 87.6 ms: 1.06x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 126 us: 1.06x faster                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 53.0 ms: 1.05x faster                                                       |
| pyflate                    | 295 ms                                                      | 283 ms: 1.04x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| go                         | 91.6 ms                                                     | 88.7 ms: 1.03x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.03 us: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| nqueens                    | 62.8 ms                                                     | 61.6 ms: 1.02x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 59.5 ns: 1.02x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 43.5 ms: 1.02x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 86.2 ms: 1.02x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.1 ms: 1.01x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 519 ms: 1.01x slower                                                        |
| meteor_contest             | 74.6 ms                                                     | 75.9 ms: 1.02x slower                                                       |
| chaos                      | 43.3 ms                                                     | 44.1 ms: 1.02x slower                                                       |
| bench_thread_pool          | 857 us                                                      | 874 us: 1.02x slower                                                        |
| sympy_str                  | 175 ms                                                      | 180 ms: 1.03x slower                                                        |
| async_generators           | 239 ms                                                      | 246 ms: 1.03x slower                                                        |
| richards_super             | 32.1 ms                                                     | 33.0 ms: 1.03x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 38.9 ms: 1.03x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 50.1 ms: 1.03x slower                                                       |
| richards                   | 28.4 ms                                                     | 29.4 ms: 1.04x slower                                                       |
| json                       | 3.05 ms                                                     | 3.16 ms: 1.04x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 81.8 ms: 1.04x slower                                                       |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.10 sec: 1.05x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.75 sec: 1.06x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.63 us: 1.06x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 62.3 ms: 1.06x slower                                                       |
| logging_format             | 6.72 us                                                     | 7.17 us: 1.07x slower                                                       |
| pycparser                  | 699 ms                                                      | 750 ms: 1.07x slower                                                        |
| json_loads                 | 13.9 us                                                     | 15.3 us: 1.10x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.53 ms: 1.11x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.58 ms: 1.11x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.40 ms: 1.11x slower                                                       |
| sympy_expand               | 284 ms                                                      | 315 ms: 1.11x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 222 us: 1.13x slower                                                        |
| django_template            | 22.9 ms                                                     | 26.2 ms: 1.14x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.58 sec: 1.16x slower                                                      |
| coverage                   | 40.8 ms                                                     | 47.4 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.98 ms: 1.22x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.6 ms: 1.27x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 89.1 ms: 1.29x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.04 ms: 1.34x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.25 ms: 1.67x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (4): fannkuch, regex_v8, sympy_sum, raytrace
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250318-3.14.0a6+-295b53d-JIT/bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 82.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown