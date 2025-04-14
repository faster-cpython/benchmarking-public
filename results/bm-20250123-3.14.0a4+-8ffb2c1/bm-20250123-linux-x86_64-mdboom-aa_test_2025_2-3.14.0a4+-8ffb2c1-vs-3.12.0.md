# Results vs. 3.12.0

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-x86_64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.108x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                             |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.06x faster                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 585 ms: 2.02x faster                                             |
| async_tree_io              | 1.16 sec                                               | 598 ms: 1.93x faster                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 306 ms: 1.88x faster                                             |
| async_tree_none            | 472 ms                                                 | 254 ms: 1.86x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.82x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 321 ms: 1.80x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                             |
| Geometric mean             | (ref)                                                  | 1.78x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.9 ms: 1.18x faster                                            |
| nbody          | 97.0 ms                                                | 96.2 ms: 1.01x faster                                            |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.06x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                             |
| regex_effbot   | 3.61 ms                                                | 3.24 ms: 1.11x faster                                            |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                             |
| regex_v8       | 23.1 ms                                                | 25.2 ms: 1.09x slower                                            |
| Geometric mean | (ref)                                                  | 1.04x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.99 sec: 1.17x faster                                           |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.14x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 97.1 ms: 1.10x faster                                            |
| xml_etree_generate   | 89.2 ms                                                | 84.5 ms: 1.06x faster                                            |
| unpickle_pure_python | 230 us                                                 | 226 us: 1.02x faster                                             |
| xml_etree_process    | 61.7 ms                                                | 61.4 ms: 1.00x faster                                            |
| json_loads           | 28.5 us                                                | 29.2 us: 1.02x slower                                            |
| json_dumps           | 10.4 ms                                                | 11.9 ms: 1.15x slower                                            |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                     |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.11 ms: 1.03x slower                                            |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.36x slower                                            |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.2 ms: 1.07x faster                                            |
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                            |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 585 ms: 2.02x faster                                             |
| async_tree_io              | 1.16 sec                                               | 598 ms: 1.93x faster                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 306 ms: 1.88x faster                                             |
| async_tree_none            | 472 ms                                                 | 254 ms: 1.86x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.82x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 321 ms: 1.80x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                             |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                             |
| deepcopy_memo              | 40.7 us                                                | 30.8 us: 1.32x faster                                            |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.63 us: 1.27x faster                                            |
| go                         | 139 ms                                                 | 116 ms: 1.20x faster                                             |
| async_generators           | 463 ms                                                 | 391 ms: 1.18x faster                                             |
| float                      | 84.7 ms                                                | 71.9 ms: 1.18x faster                                            |
| deltablue                  | 3.72 ms                                                | 3.16 ms: 1.18x faster                                            |
| tomli_loads                | 2.33 sec                                               | 1.99 sec: 1.17x faster                                           |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.17x faster                                            |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                             |
| raytrace                   | 312 ms                                                 | 270 ms: 1.15x faster                                             |
| chaos                      | 67.0 ms                                                | 58.0 ms: 1.15x faster                                            |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                             |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.14x faster                                             |
| generators                 | 31.2 ms                                                | 27.7 ms: 1.13x faster                                            |
| logging_format             | 7.23 us                                                | 6.44 us: 1.12x faster                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 67.0 ms: 1.12x faster                                            |
| logging_simple             | 6.46 us                                                | 5.77 us: 1.12x faster                                            |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                             |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.7 ms: 1.12x faster                                            |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.12x faster                                             |
| crypto_pyaes               | 81.9 ms                                                | 73.4 ms: 1.11x faster                                            |
| regex_effbot               | 3.61 ms                                                | 3.24 ms: 1.11x faster                                            |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                             |
| xml_etree_iterparse        | 107 ms                                                 | 97.1 ms: 1.10x faster                                            |
| scimark_fft                | 382 ms                                                 | 349 ms: 1.09x faster                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.25 ms: 1.09x faster                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.55 ms: 1.08x faster                                            |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                            |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.07x faster                                            |
| pprint_safe_repr           | 776 ms                                                 | 724 ms: 1.07x faster                                             |
| pyflate                    | 482 ms                                                 | 450 ms: 1.07x faster                                             |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                             |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                            |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.06x faster                                           |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                             |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                           |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 84.5 ms: 1.06x faster                                            |
| sympy_expand               | 478 ms                                                 | 454 ms: 1.05x faster                                             |
| sqlglot_normalize          | 110 ms                                                 | 105 ms: 1.05x faster                                             |
| dulwich_log                | 68.5 ms                                                | 65.1 ms: 1.05x faster                                            |
| mdp                        | 2.63 sec                                               | 2.51 sec: 1.05x faster                                           |
| richards                   | 45.8 ms                                                | 43.8 ms: 1.05x faster                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.85 ms: 1.04x faster                                            |
| nqueens                    | 83.3 ms                                                | 80.2 ms: 1.04x faster                                            |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.04x faster                                           |
| sqlglot_optimize           | 54.8 ms                                                | 53.0 ms: 1.03x faster                                            |
| fannkuch                   | 417 ms                                                 | 404 ms: 1.03x faster                                             |
| richards_super             | 51.5 ms                                                | 50.1 ms: 1.03x faster                                            |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                             |
| hexiom                     | 6.41 ms                                                | 6.28 ms: 1.02x faster                                            |
| unpickle_pure_python       | 230 us                                                 | 226 us: 1.02x faster                                             |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                            |
| logging_silent             | 104 ns                                                 | 103 ns: 1.02x faster                                             |
| nbody                      | 97.0 ms                                                | 96.2 ms: 1.01x faster                                            |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                             |
| xml_etree_process          | 61.7 ms                                                | 61.4 ms: 1.00x faster                                            |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                             |
| json_loads                 | 28.5 us                                                | 29.2 us: 1.02x slower                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.11 ms: 1.03x slower                                            |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                            |
| bench_thread_pool          | 842 us                                                 | 866 us: 1.03x slower                                             |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                             |
| regex_v8                   | 23.1 ms                                                | 25.2 ms: 1.09x slower                                            |
| telco                      | 7.10 ms                                                | 7.99 ms: 1.13x slower                                            |
| json_dumps                 | 10.4 ms                                                | 11.9 ms: 1.15x slower                                            |
| coverage                   | 72.7 ms                                                | 90.7 ms: 1.25x slower                                            |
| gc_traversal               | 3.79 ms                                                | 5.03 ms: 1.33x slower                                            |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.36x slower                                            |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                            |
| bench_mp_pool              | 24.0 ms                                                | 81.8 ms: 3.41x slower                                            |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                     |

Benchmark hidden because not significant (3): json, asyncio_websockets, pickle_pure_python
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250123-3.14.0a4+-8ffb2c1/bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.09x