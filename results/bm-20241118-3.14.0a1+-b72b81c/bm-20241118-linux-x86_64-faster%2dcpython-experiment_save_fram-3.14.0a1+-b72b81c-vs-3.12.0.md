# Results vs. 3.12.0

- fork: faster-cpython
- ref: experiment_save_fram
- machine: linux-x86_64
- commit hash: b72b81c
- commit date: 2024-11-18
- overall geometric mean: 1.061x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                             |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 383 ms: 1.50x faster                                                             |
| async_tree_none            | 472 ms                                                 | 331 ms: 1.42x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 416 ms: 1.39x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 327 ms: 1.38x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 848 ms: 1.36x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 575 ms: 1.26x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 580 ms: 1.25x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 967 ms: 1.22x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.35x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 80.0 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                             |
| regex_effbot   | 3.61 ms                                                | 3.58 ms: 1.01x faster                                                            |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                             |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                                             |
| json_loads           | 28.5 us                                                | 27.1 us: 1.05x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 86.8 ms: 1.03x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                            |
| pickle_pure_python   | 324 us                                                 | 326 us: 1.01x slower                                                             |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                            |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.2 ms: 1.08x faster                                                            |
| mako            | 11.9 ms                                                | 11.5 ms: 1.03x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 383 ms: 1.50x faster                                                             |
| async_tree_none            | 472 ms                                                 | 331 ms: 1.42x faster                                                             |
| deepcopy                   | 371 us                                                 | 266 us: 1.39x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 416 ms: 1.39x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 327 ms: 1.38x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 848 ms: 1.36x faster                                                             |
| deepcopy_memo              | 40.7 us                                                | 30.2 us: 1.35x faster                                                            |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 575 ms: 1.26x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 580 ms: 1.25x faster                                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 967 ms: 1.22x faster                                                             |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                            |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                                            |
| go                         | 139 ms                                                 | 119 ms: 1.17x faster                                                             |
| logging_simple             | 6.46 us                                                | 5.59 us: 1.16x faster                                                            |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.15x faster                                                             |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                             |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                             |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                             |
| crypto_pyaes               | 81.9 ms                                                | 71.9 ms: 1.14x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.26 ms: 1.14x faster                                                            |
| generators                 | 31.2 ms                                                | 27.8 ms: 1.12x faster                                                            |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                                             |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                                            |
| tomli_loads                | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                           |
| chaos                      | 67.0 ms                                                | 61.6 ms: 1.09x faster                                                            |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.08x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 724 ms: 1.07x faster                                                             |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 70.3 ms: 1.07x faster                                                            |
| async_generators           | 463 ms                                                 | 434 ms: 1.07x faster                                                             |
| float                      | 84.7 ms                                                | 80.0 ms: 1.06x faster                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                                             |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                            |
| json_loads                 | 28.5 us                                                | 27.1 us: 1.05x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 65.3 ms: 1.05x faster                                                            |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                             |
| json                       | 5.26 ms                                                | 5.03 ms: 1.05x faster                                                            |
| fannkuch                   | 417 ms                                                 | 404 ms: 1.03x faster                                                             |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.03x faster                                                            |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                             |
| xml_etree_generate         | 89.2 ms                                                | 86.8 ms: 1.03x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                            |
| pyflate                    | 482 ms                                                 | 470 ms: 1.03x faster                                                             |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 53.7 ms: 1.02x faster                                                            |
| nqueens                    | 83.3 ms                                                | 81.6 ms: 1.02x faster                                                            |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                                             |
| hexiom                     | 6.41 ms                                                | 6.33 ms: 1.01x faster                                                            |
| scimark_fft                | 382 ms                                                 | 379 ms: 1.01x faster                                                             |
| regex_effbot               | 3.61 ms                                                | 3.58 ms: 1.01x faster                                                            |
| logging_silent             | 104 ns                                                 | 104 ns: 1.01x faster                                                             |
| pickle_pure_python         | 324 us                                                 | 326 us: 1.01x slower                                                             |
| scimark_sor                | 129 ms                                                 | 130 ms: 1.01x slower                                                             |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                            |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                            |
| bench_thread_pool          | 842 us                                                 | 852 us: 1.01x slower                                                             |
| richards                   | 45.8 ms                                                | 46.4 ms: 1.01x slower                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.13 ms: 1.01x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                            |
| spectral_norm              | 115 ms                                                 | 117 ms: 1.02x slower                                                             |
| mdp                        | 2.63 sec                                               | 2.67 sec: 1.02x slower                                                           |
| richards_super             | 51.5 ms                                                | 52.8 ms: 1.02x slower                                                            |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                             |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                             |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                            |
| telco                      | 7.10 ms                                                | 7.82 ms: 1.10x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                            |
| coverage                   | 72.7 ms                                                | 84.0 ms: 1.16x slower                                                            |
| gc_traversal               | 3.79 ms                                                | 4.72 ms: 1.24x slower                                                            |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                            |
| create_gc_cycles           | 1.48 ms                                                | 2.70 ms: 1.83x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 78.7 ms: 3.28x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                                     |

Benchmark hidden because not significant (7): xml_etree_parse, pycparser, xml_etree_iterparse, nbody, scimark_lu, pidigits, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241118-3.14.0a1+-b72b81c/bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.061x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.09x