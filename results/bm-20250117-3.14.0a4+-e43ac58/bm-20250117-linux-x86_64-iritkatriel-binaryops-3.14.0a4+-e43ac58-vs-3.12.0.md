# Results vs. 3.12.0

- fork: iritkatriel
- ref: binaryops
- machine: linux-x86_64
- commit hash: e43ac58
- commit date: 2025-01-17
- overall geometric mean: 1.117x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                             |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 582 ms: 2.03x faster                                             |
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 304 ms: 1.89x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 244 ms: 1.84x faster                                             |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 325 ms: 1.78x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 458 ms: 1.58x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 482 ms: 1.50x faster                                             |
| Geometric mean             | (ref)                                                  | 1.79x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.4 ms: 1.20x faster                                            |
| nbody          | 97.0 ms                                                | 95.4 ms: 1.02x faster                                            |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.07x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                             |
| regex_effbot   | 3.61 ms                                                | 3.29 ms: 1.10x faster                                            |
| regex_dna      | 212 ms                                                 | 205 ms: 1.03x faster                                             |
| regex_v8       | 23.1 ms                                                | 25.8 ms: 1.11x slower                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                           |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 97.5 ms: 1.10x faster                                            |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                             |
| xml_etree_generate   | 89.2 ms                                                | 84.6 ms: 1.05x faster                                            |
| xml_etree_process    | 61.7 ms                                                | 60.0 ms: 1.03x faster                                            |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                             |
| json_loads           | 28.5 us                                                | 29.5 us: 1.04x slower                                            |
| json_dumps           | 10.4 ms                                                | 12.0 ms: 1.16x slower                                            |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.01x slower                                            |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                            |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                            |
| mako            | 11.9 ms                                                | 11.5 ms: 1.03x faster                                            |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 582 ms: 2.03x faster                                             |
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 304 ms: 1.89x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 244 ms: 1.84x faster                                             |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 325 ms: 1.78x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 458 ms: 1.58x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 482 ms: 1.50x faster                                             |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                             |
| deepcopy_memo              | 40.7 us                                                | 30.9 us: 1.32x faster                                            |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                            |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                            |
| float                      | 84.7 ms                                                | 70.4 ms: 1.20x faster                                            |
| go                         | 139 ms                                                 | 117 ms: 1.20x faster                                             |
| async_generators           | 463 ms                                                 | 388 ms: 1.19x faster                                             |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                           |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                             |
| spectral_norm              | 115 ms                                                 | 97.8 ms: 1.17x faster                                            |
| logging_format             | 7.23 us                                                | 6.16 us: 1.17x faster                                            |
| deltablue                  | 3.72 ms                                                | 3.17 ms: 1.17x faster                                            |
| logging_simple             | 6.46 us                                                | 5.53 us: 1.17x faster                                            |
| chaos                      | 67.0 ms                                                | 57.8 ms: 1.16x faster                                            |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                             |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                             |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                             |
| crypto_pyaes               | 81.9 ms                                                | 71.6 ms: 1.14x faster                                            |
| generators                 | 31.2 ms                                                | 27.3 ms: 1.14x faster                                            |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.4 ms: 1.14x faster                                            |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.13x faster                                             |
| sympy_str                  | 300 ms                                                 | 266 ms: 1.13x faster                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 67.3 ms: 1.12x faster                                            |
| scimark_fft                | 382 ms                                                 | 347 ms: 1.10x faster                                             |
| regex_effbot               | 3.61 ms                                                | 3.29 ms: 1.10x faster                                            |
| xml_etree_iterparse        | 107 ms                                                 | 97.5 ms: 1.10x faster                                            |
| pprint_safe_repr           | 776 ms                                                 | 712 ms: 1.09x faster                                             |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.26 ms: 1.08x faster                                            |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                             |
| sqlglot_transpile          | 1.68 ms                                                | 1.56 ms: 1.08x faster                                            |
| pyflate                    | 482 ms                                                 | 449 ms: 1.07x faster                                             |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                             |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                            |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                           |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                           |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                             |
| dulwich_log                | 68.5 ms                                                | 64.2 ms: 1.07x faster                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.76 ms: 1.06x faster                                            |
| sympy_expand               | 478 ms                                                 | 451 ms: 1.06x faster                                             |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.06x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 84.6 ms: 1.05x faster                                            |
| sqlglot_normalize          | 110 ms                                                 | 105 ms: 1.05x faster                                             |
| richards                   | 45.8 ms                                                | 43.8 ms: 1.05x faster                                            |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.04x faster                                           |
| sqlglot_optimize           | 54.8 ms                                                | 52.6 ms: 1.04x faster                                            |
| fannkuch                   | 417 ms                                                 | 401 ms: 1.04x faster                                             |
| richards_super             | 51.5 ms                                                | 49.8 ms: 1.04x faster                                            |
| regex_dna                  | 212 ms                                                 | 205 ms: 1.03x faster                                             |
| nqueens                    | 83.3 ms                                                | 80.5 ms: 1.03x faster                                            |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.03x faster                                            |
| xml_etree_process          | 61.7 ms                                                | 60.0 ms: 1.03x faster                                            |
| hexiom                     | 6.41 ms                                                | 6.23 ms: 1.03x faster                                            |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                            |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                           |
| nbody                      | 97.0 ms                                                | 95.4 ms: 1.02x faster                                            |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                             |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                             |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                             |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.01x slower                                            |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                            |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                             |
| bench_thread_pool          | 842 us                                                 | 865 us: 1.03x slower                                             |
| logging_silent             | 104 ns                                                 | 107 ns: 1.03x slower                                             |
| json_loads                 | 28.5 us                                                | 29.5 us: 1.04x slower                                            |
| telco                      | 7.10 ms                                                | 7.77 ms: 1.09x slower                                            |
| regex_v8                   | 23.1 ms                                                | 25.8 ms: 1.11x slower                                            |
| json_dumps                 | 10.4 ms                                                | 12.0 ms: 1.16x slower                                            |
| gc_traversal               | 3.79 ms                                                | 4.59 ms: 1.21x slower                                            |
| coverage                   | 72.7 ms                                                | 89.6 ms: 1.23x slower                                            |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                            |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                            |
| bench_mp_pool              | 24.0 ms                                                | 81.3 ms: 3.39x slower                                            |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                     |

Benchmark hidden because not significant (2): json, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250117-3.14.0a4+-e43ac58/bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.117x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.09x