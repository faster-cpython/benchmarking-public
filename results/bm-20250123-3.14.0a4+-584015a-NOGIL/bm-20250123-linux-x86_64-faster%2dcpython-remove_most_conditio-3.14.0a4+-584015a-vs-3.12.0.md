# Results vs. 3.12.0

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 584015a
- commit date: 2025-01-23
- overall geometric mean: 1.048x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 313 ms: 1.14x slower                                                             |
| docutils       | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                           |
| Geometric mean | (ref)                                                  | 1.10x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 568 ms: 2.08x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 334 ms: 1.72x faster                                                             |
| async_tree_none            | 472 ms                                                 | 294 ms: 1.61x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 373 ms: 1.55x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 532 ms: 1.37x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.67x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.6 ms: 1.08x faster                                                            |
| pidigits       | 187 ms                                                 | 182 ms: 1.03x faster                                                             |
| nbody          | 97.0 ms                                                | 137 ms: 1.41x slower                                                             |
| Geometric mean | (ref)                                                  | 1.08x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.48 ms: 1.04x faster                                                            |
| regex_compile  | 148 ms                                                 | 152 ms: 1.03x slower                                                             |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                                             |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                            |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 95.9 ms: 1.11x faster                                                            |
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.06x faster                                                             |
| tomli_loads          | 2.33 sec                                               | 2.43 sec: 1.04x slower                                                           |
| xml_etree_generate   | 89.2 ms                                                | 96.2 ms: 1.08x slower                                                            |
| json_loads           | 28.5 us                                                | 31.4 us: 1.10x slower                                                            |
| xml_etree_process    | 61.7 ms                                                | 68.6 ms: 1.11x slower                                                            |
| unpickle_pure_python | 230 us                                                 | 261 us: 1.13x slower                                                             |
| pickle_pure_python   | 324 us                                                 | 377 us: 1.16x slower                                                             |
| json_dumps           | 10.4 ms                                                | 12.8 ms: 1.23x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.37 ms: 1.35x slower                                                            |
| python_startup         | 9.55 ms                                                | 15.1 ms: 1.58x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.46x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 42.9 ms: 1.24x slower                                                            |
| mako            | 11.9 ms                                                | 16.7 ms: 1.40x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.32x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 568 ms: 2.08x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 334 ms: 1.72x faster                                                             |
| async_tree_none            | 472 ms                                                 | 294 ms: 1.61x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 373 ms: 1.55x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 532 ms: 1.37x faster                                                             |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                            |
| deepcopy                   | 371 us                                                 | 315 us: 1.18x faster                                                             |
| xml_etree_iterparse        | 107 ms                                                 | 95.9 ms: 1.11x faster                                                            |
| float                      | 84.7 ms                                                | 78.6 ms: 1.08x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.06x faster                                                             |
| async_generators           | 463 ms                                                 | 438 ms: 1.06x faster                                                             |
| regex_effbot               | 3.61 ms                                                | 3.48 ms: 1.04x faster                                                            |
| comprehensions             | 21.8 us                                                | 21.0 us: 1.03x faster                                                            |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                            |
| pidigits                   | 187 ms                                                 | 182 ms: 1.03x faster                                                             |
| deepcopy_memo              | 40.7 us                                                | 40.0 us: 1.02x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 3.30 us: 1.01x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 69.3 ms: 1.01x slower                                                            |
| spectral_norm              | 115 ms                                                 | 117 ms: 1.02x slower                                                             |
| generators                 | 31.2 ms                                                | 32.0 ms: 1.02x slower                                                            |
| regex_compile              | 148 ms                                                 | 152 ms: 1.03x slower                                                             |
| tomli_loads                | 2.33 sec                                               | 2.43 sec: 1.04x slower                                                           |
| pycparser                  | 1.18 sec                                               | 1.23 sec: 1.04x slower                                                           |
| mdp                        | 2.63 sec                                               | 2.76 sec: 1.05x slower                                                           |
| go                         | 139 ms                                                 | 146 ms: 1.05x slower                                                             |
| docutils                   | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                           |
| sympy_sum                  | 169 ms                                                 | 178 ms: 1.05x slower                                                             |
| logging_format             | 7.23 us                                                | 7.64 us: 1.06x slower                                                            |
| logging_simple             | 6.46 us                                                | 6.83 us: 1.06x slower                                                            |
| json                       | 5.26 ms                                                | 5.58 ms: 1.06x slower                                                            |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                                             |
| sympy_str                  | 300 ms                                                 | 321 ms: 1.07x slower                                                             |
| xml_etree_generate         | 89.2 ms                                                | 96.2 ms: 1.08x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                            |
| sqlalchemy_imperative      | 18.7 ms                                                | 20.6 ms: 1.10x slower                                                            |
| scimark_fft                | 382 ms                                                 | 421 ms: 1.10x slower                                                             |
| json_loads                 | 28.5 us                                                | 31.4 us: 1.10x slower                                                            |
| crypto_pyaes               | 81.9 ms                                                | 90.7 ms: 1.11x slower                                                            |
| xml_etree_process          | 61.7 ms                                                | 68.6 ms: 1.11x slower                                                            |
| pyflate                    | 482 ms                                                 | 537 ms: 1.11x slower                                                             |
| sqlglot_normalize          | 110 ms                                                 | 123 ms: 1.11x slower                                                             |
| scimark_sor                | 129 ms                                                 | 144 ms: 1.12x slower                                                             |
| sqlalchemy_declarative     | 147 ms                                                 | 164 ms: 1.12x slower                                                             |
| pprint_safe_repr           | 776 ms                                                 | 867 ms: 1.12x slower                                                             |
| coroutines                 | 23.2 ms                                                | 25.9 ms: 1.12x slower                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 61.5 ms: 1.12x slower                                                            |
| chaos                      | 67.0 ms                                                | 75.2 ms: 1.12x slower                                                            |
| sympy_expand               | 478 ms                                                 | 538 ms: 1.13x slower                                                             |
| sympy_integrate            | 21.4 ms                                                | 24.2 ms: 1.13x slower                                                            |
| unpickle_pure_python       | 230 us                                                 | 261 us: 1.13x slower                                                             |
| 2to3                       | 274 ms                                                 | 313 ms: 1.14x slower                                                             |
| pprint_pformat             | 1.57 sec                                               | 1.79 sec: 1.14x slower                                                           |
| raytrace                   | 312 ms                                                 | 359 ms: 1.15x slower                                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 87.3 ms: 1.16x slower                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.58 ms: 1.16x slower                                                            |
| pickle_pure_python         | 324 us                                                 | 377 us: 1.16x slower                                                             |
| create_gc_cycles           | 1.48 ms                                                | 1.72 ms: 1.17x slower                                                            |
| logging_silent             | 104 ns                                                 | 122 ns: 1.17x slower                                                             |
| gc_traversal               | 3.79 ms                                                | 4.44 ms: 1.17x slower                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.98 ms: 1.18x slower                                                            |
| meteor_contest             | 112 ms                                                 | 134 ms: 1.20x slower                                                             |
| scimark_lu                 | 118 ms                                                 | 142 ms: 1.20x slower                                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.13 ms: 1.21x slower                                                            |
| nqueens                    | 83.3 ms                                                | 101 ms: 1.21x slower                                                             |
| json_dumps                 | 10.4 ms                                                | 12.8 ms: 1.23x slower                                                            |
| hexiom                     | 6.41 ms                                                | 7.89 ms: 1.23x slower                                                            |
| django_template            | 34.6 ms                                                | 42.9 ms: 1.24x slower                                                            |
| fannkuch                   | 417 ms                                                 | 522 ms: 1.25x slower                                                             |
| telco                      | 7.10 ms                                                | 9.14 ms: 1.29x slower                                                            |
| deltablue                  | 3.72 ms                                                | 4.84 ms: 1.30x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 9.37 ms: 1.35x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 213 us: 1.35x slower                                                             |
| richards                   | 45.8 ms                                                | 62.4 ms: 1.36x slower                                                            |
| richards_super             | 51.5 ms                                                | 71.8 ms: 1.39x slower                                                            |
| mako                       | 11.9 ms                                                | 16.7 ms: 1.40x slower                                                            |
| nbody                      | 97.0 ms                                                | 137 ms: 1.41x slower                                                             |
| coverage                   | 72.7 ms                                                | 107 ms: 1.47x slower                                                             |
| python_startup             | 9.55 ms                                                | 15.1 ms: 1.58x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 90.0 ms: 3.75x slower                                                            |
| bench_thread_pool          | 842 us                                                 | 3.47 ms: 4.12x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.08x slower                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250123-3.14.0a4+-584015a-NOGIL/bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.048x slower

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.31x