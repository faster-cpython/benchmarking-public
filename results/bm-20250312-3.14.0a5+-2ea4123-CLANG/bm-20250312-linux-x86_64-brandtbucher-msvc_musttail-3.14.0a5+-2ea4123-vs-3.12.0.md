# Results vs. 3.12.0

- fork: brandtbucher
- ref: msvc_musttail
- machine: linux-x86_64
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.145x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 251 ms: 1.09x faster                                                  |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 606 ms: 1.95x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 596 ms: 1.94x faster                                                  |
| async_tree_none            | 472 ms                                                 | 249 ms: 1.89x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 306 ms: 1.89x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 307 ms: 1.87x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 242 ms: 1.86x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 504 ms: 1.44x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 517 ms: 1.40x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 66.8 ms: 1.27x faster                                                 |
| nbody          | 97.0 ms                                                | 86.4 ms: 1.12x faster                                                 |
| pidigits       | 187 ms                                                 | 219 ms: 1.17x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.28 ms: 1.10x faster                                                 |
| regex_dna      | 212 ms                                                 | 196 ms: 1.08x faster                                                  |
| regex_v8       | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 306 us: 1.06x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 103 ms: 1.04x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 86.8 ms: 1.03x faster                                                 |
| json_loads           | 28.5 us                                                | 28.9 us: 1.01x slower                                                 |
| xml_etree_parse      | 159 ms                                                 | 163 ms: 1.02x slower                                                  |
| json_dumps           | 10.4 ms                                                | 12.5 ms: 1.20x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                 |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 30.6 ms: 1.13x faster                                                 |
| mako            | 11.9 ms                                                | 11.6 ms: 1.03x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 606 ms: 1.95x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 596 ms: 1.94x faster                                                  |
| async_tree_none            | 472 ms                                                 | 249 ms: 1.89x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 306 ms: 1.89x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 307 ms: 1.87x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 242 ms: 1.86x faster                                                  |
| deepcopy                   | 371 us                                                 | 244 us: 1.52x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 504 ms: 1.44x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 517 ms: 1.40x faster                                                  |
| comprehensions             | 21.8 us                                                | 15.5 us: 1.40x faster                                                 |
| spectral_norm              | 115 ms                                                 | 82.5 ms: 1.39x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.39x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.53 us: 1.32x faster                                                 |
| scimark_fft                | 382 ms                                                 | 289 ms: 1.32x faster                                                  |
| pathlib                    | 19.3 ms                                                | 14.9 ms: 1.30x faster                                                 |
| float                      | 84.7 ms                                                | 66.8 ms: 1.27x faster                                                 |
| async_generators           | 463 ms                                                 | 368 ms: 1.26x faster                                                  |
| chaos                      | 67.0 ms                                                | 53.3 ms: 1.26x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 60.1 ms: 1.25x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                |
| go                         | 139 ms                                                 | 113 ms: 1.24x faster                                                  |
| logging_format             | 7.23 us                                                | 5.86 us: 1.23x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.01 ms: 1.23x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.26 us: 1.23x faster                                                 |
| raytrace                   | 312 ms                                                 | 255 ms: 1.23x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.14 ms: 1.22x faster                                                 |
| scimark_sor                | 129 ms                                                 | 107 ms: 1.21x faster                                                  |
| logging_silent             | 104 ns                                                 | 87.1 ns: 1.20x faster                                                 |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 143 ms: 1.18x faster                                                  |
| pyflate                    | 482 ms                                                 | 410 ms: 1.18x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 126 ms: 1.17x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.1 ms: 1.16x faster                                                 |
| sympy_str                  | 300 ms                                                 | 258 ms: 1.16x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 18.9 ms: 1.13x faster                                                 |
| django_template            | 34.6 ms                                                | 30.6 ms: 1.13x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 72.5 ms: 1.13x faster                                                 |
| nbody                      | 97.0 ms                                                | 86.4 ms: 1.12x faster                                                 |
| hexiom                     | 6.41 ms                                                | 5.74 ms: 1.12x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 61.8 ms: 1.11x faster                                                 |
| nqueens                    | 83.3 ms                                                | 75.4 ms: 1.10x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 107 ms: 1.10x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.28 ms: 1.10x faster                                                 |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                                 |
| 2to3                       | 274 ms                                                 | 251 ms: 1.09x faster                                                  |
| sympy_expand               | 478 ms                                                 | 440 ms: 1.09x faster                                                  |
| regex_dna                  | 212 ms                                                 | 196 ms: 1.08x faster                                                  |
| typing_runtime_protocols   | 158 us                                                 | 148 us: 1.07x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.66 us: 1.07x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                |
| fannkuch                   | 417 ms                                                 | 393 ms: 1.06x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 306 us: 1.06x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 736 ms: 1.05x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                 |
| coroutines                 | 23.2 ms                                                | 22.1 ms: 1.05x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 103 ms: 1.04x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 86.8 ms: 1.03x faster                                                 |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.03x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.02x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 831 us: 1.01x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                 |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.01x slower                                                 |
| xml_etree_parse            | 159 ms                                                 | 163 ms: 1.02x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                 |
| richards                   | 45.8 ms                                                | 47.4 ms: 1.03x slower                                                 |
| telco                      | 7.10 ms                                                | 7.39 ms: 1.04x slower                                                 |
| richards_super             | 51.5 ms                                                | 55.6 ms: 1.08x slower                                                 |
| coverage                   | 72.7 ms                                                | 79.6 ms: 1.09x slower                                                 |
| pidigits                   | 187 ms                                                 | 219 ms: 1.17x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 12.5 ms: 1.20x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.97 ms: 1.31x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.54 ms: 1.72x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.13x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250312-3.14.0a5+-2ea4123-CLANG/bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.145x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.10x