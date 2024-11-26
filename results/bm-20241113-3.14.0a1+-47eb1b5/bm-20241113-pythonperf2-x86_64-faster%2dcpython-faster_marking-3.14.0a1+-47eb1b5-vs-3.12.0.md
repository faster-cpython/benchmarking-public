# Results vs. 3.12.0

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: 47eb1b5
- commit date: 2024-11-13
- overall geometric mean: 1.031x faster
- HPT reliability: 57.42%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 289 ms: 1.01x slower                                                             |
| docutils       | 2.87 sec                                                     | 2.88 sec: 1.01x slower                                                           |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 652 ms: 1.62x faster                                                             |
| async_tree_io              | 1.04 sec                                                     | 653 ms: 1.59x faster                                                             |
| async_tree_memoization_tg  | 540 ms                                                       | 357 ms: 1.51x faster                                                             |
| async_tree_none            | 452 ms                                                       | 304 ms: 1.48x faster                                                             |
| async_tree_memoization     | 544 ms                                                       | 369 ms: 1.47x faster                                                             |
| async_tree_none_tg         | 431 ms                                                       | 300 ms: 1.44x faster                                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 523 ms: 1.33x faster                                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 537 ms: 1.30x faster                                                             |
| Geometric mean             | (ref)                                                        | 1.46x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                             |
| float          | 76.6 ms                                                      | 85.5 ms: 1.12x slower                                                            |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.03x faster                                                             |
| regex_effbot   | 3.57 ms                                                      | 3.62 ms: 1.01x slower                                                            |
| regex_dna      | 239 ms                                                       | 250 ms: 1.05x slower                                                             |
| regex_v8       | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 24.4 us                                                      | 24.9 us: 1.02x slower                                                            |
| unpickle_pure_python | 210 us                                                       | 215 us: 1.02x slower                                                             |
| xml_etree_generate   | 86.1 ms                                                      | 88.4 ms: 1.03x slower                                                            |
| pickle_pure_python   | 318 us                                                       | 332 us: 1.04x slower                                                             |
| xml_etree_process    | 58.4 ms                                                      | 62.8 ms: 1.08x slower                                                            |
| json_dumps           | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                            |
| tomli_loads          | 2.16 sec                                                     | 2.48 sec: 1.15x slower                                                           |
| xml_etree_parse      | 144 ms                                                       | 166 ms: 1.15x slower                                                             |
| xml_etree_iterparse  | 103 ms                                                       | 120 ms: 1.17x slower                                                             |
| Geometric mean       | (ref)                                                        | 1.09x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.59 ms: 1.00x faster                                                            |
| python_startup         | 11.6 ms                                                      | 15.5 ms: 1.33x slower                                                            |
| Geometric mean         | (ref)                                                        | 1.15x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 37.4 ms: 1.02x faster                                                            |
| mako            | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                            |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| gc_traversal               | 3.48 ms                                                      | 1.97 ms: 1.77x faster                                                            |
| async_tree_io_tg           | 1.05 sec                                                     | 652 ms: 1.62x faster                                                             |
| async_tree_io              | 1.04 sec                                                     | 653 ms: 1.59x faster                                                             |
| async_tree_memoization_tg  | 540 ms                                                       | 357 ms: 1.51x faster                                                             |
| async_tree_none            | 452 ms                                                       | 304 ms: 1.48x faster                                                             |
| async_tree_memoization     | 544 ms                                                       | 369 ms: 1.47x faster                                                             |
| async_tree_none_tg         | 431 ms                                                       | 300 ms: 1.44x faster                                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 523 ms: 1.33x faster                                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 537 ms: 1.30x faster                                                             |
| deepcopy                   | 368 us                                                       | 287 us: 1.28x faster                                                             |
| generators                 | 37.4 ms                                                      | 29.6 ms: 1.27x faster                                                            |
| deepcopy_memo              | 36.8 us                                                      | 29.5 us: 1.25x faster                                                            |
| comprehensions             | 21.9 us                                                      | 17.8 us: 1.23x faster                                                            |
| pathlib                    | 18.9 ms                                                      | 16.2 ms: 1.17x faster                                                            |
| deepcopy_reduce            | 3.37 us                                                      | 2.95 us: 1.14x faster                                                            |
| sqlalchemy_declarative     | 159 ms                                                       | 142 ms: 1.12x faster                                                             |
| go                         | 150 ms                                                       | 135 ms: 1.11x faster                                                             |
| crypto_pyaes               | 80.3 ms                                                      | 73.5 ms: 1.09x faster                                                            |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.09x faster                                                            |
| raytrace                   | 298 ms                                                       | 279 ms: 1.07x faster                                                             |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                             |
| logging_format             | 7.48 us                                                      | 7.09 us: 1.06x faster                                                            |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                             |
| logging_simple             | 6.71 us                                                      | 6.42 us: 1.04x faster                                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.59 sec: 1.04x faster                                                           |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.3 ms: 1.04x faster                                                            |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.1 ms: 1.03x faster                                                            |
| regex_compile              | 144 ms                                                       | 139 ms: 1.03x faster                                                             |
| sympy_str                  | 302 ms                                                       | 293 ms: 1.03x faster                                                             |
| bench_thread_pool          | 950 us                                                       | 924 us: 1.03x faster                                                             |
| sympy_integrate            | 23.9 ms                                                      | 23.3 ms: 1.03x faster                                                            |
| pprint_safe_repr           | 807 ms                                                       | 788 ms: 1.02x faster                                                             |
| scimark_lu                 | 98.8 ms                                                      | 96.6 ms: 1.02x faster                                                            |
| mdp                        | 2.57 sec                                                     | 2.52 sec: 1.02x faster                                                           |
| django_template            | 38.2 ms                                                      | 37.4 ms: 1.02x faster                                                            |
| chaos                      | 64.0 ms                                                      | 62.8 ms: 1.02x faster                                                            |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.01x faster                                                             |
| python_startup_no_site     | 8.64 ms                                                      | 8.59 ms: 1.00x faster                                                            |
| docutils                   | 2.87 sec                                                     | 2.88 sec: 1.01x slower                                                           |
| regex_effbot               | 3.57 ms                                                      | 3.62 ms: 1.01x slower                                                            |
| 2to3                       | 285 ms                                                       | 289 ms: 1.01x slower                                                             |
| nqueens                    | 89.9 ms                                                      | 91.3 ms: 1.02x slower                                                            |
| json_loads                 | 24.4 us                                                      | 24.9 us: 1.02x slower                                                            |
| unpickle_pure_python       | 210 us                                                       | 215 us: 1.02x slower                                                             |
| xml_etree_generate         | 86.1 ms                                                      | 88.4 ms: 1.03x slower                                                            |
| sqlglot_transpile          | 1.78 ms                                                      | 1.82 ms: 1.03x slower                                                            |
| sqlite_synth               | 2.77 us                                                      | 2.86 us: 1.03x slower                                                            |
| dulwich_log                | 65.4 ms                                                      | 67.7 ms: 1.04x slower                                                            |
| fannkuch                   | 350 ms                                                       | 364 ms: 1.04x slower                                                             |
| sympy_expand               | 484 ms                                                       | 503 ms: 1.04x slower                                                             |
| pickle_pure_python         | 318 us                                                       | 332 us: 1.04x slower                                                             |
| scimark_fft                | 301 ms                                                       | 315 ms: 1.05x slower                                                             |
| regex_dna                  | 239 ms                                                       | 250 ms: 1.05x slower                                                             |
| hexiom                     | 5.96 ms                                                      | 6.25 ms: 1.05x slower                                                            |
| sqlglot_parse              | 1.38 ms                                                      | 1.45 ms: 1.05x slower                                                            |
| spectral_norm              | 91.6 ms                                                      | 96.2 ms: 1.05x slower                                                            |
| sqlglot_normalize          | 116 ms                                                       | 122 ms: 1.06x slower                                                             |
| sqlglot_optimize           | 57.5 ms                                                      | 61.0 ms: 1.06x slower                                                            |
| regex_v8                   | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                            |
| mako                       | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                            |
| xml_etree_process          | 58.4 ms                                                      | 62.8 ms: 1.08x slower                                                            |
| logging_silent             | 94.4 ns                                                      | 102 ns: 1.08x slower                                                             |
| richards_super             | 51.3 ms                                                      | 55.5 ms: 1.08x slower                                                            |
| scimark_sor                | 109 ms                                                       | 119 ms: 1.09x slower                                                             |
| richards                   | 45.7 ms                                                      | 49.9 ms: 1.09x slower                                                            |
| deltablue                  | 3.24 ms                                                      | 3.60 ms: 1.11x slower                                                            |
| float                      | 76.6 ms                                                      | 85.5 ms: 1.12x slower                                                            |
| pyflate                    | 439 ms                                                       | 491 ms: 1.12x slower                                                             |
| json_dumps                 | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                            |
| async_generators           | 390 ms                                                       | 447 ms: 1.14x slower                                                             |
| create_gc_cycles           | 1.59 ms                                                      | 1.82 ms: 1.15x slower                                                            |
| tomli_loads                | 2.16 sec                                                     | 2.48 sec: 1.15x slower                                                           |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.83 ms: 1.15x slower                                                            |
| xml_etree_parse            | 144 ms                                                       | 166 ms: 1.15x slower                                                             |
| telco                      | 6.96 ms                                                      | 8.03 ms: 1.15x slower                                                            |
| typing_runtime_protocols   | 152 us                                                       | 175 us: 1.16x slower                                                             |
| xml_etree_iterparse        | 103 ms                                                       | 120 ms: 1.17x slower                                                             |
| coverage                   | 66.7 ms                                                      | 82.6 ms: 1.24x slower                                                            |
| python_startup             | 11.6 ms                                                      | 15.5 ms: 1.33x slower                                                            |
| bench_mp_pool              | 4.76 ms                                                      | 1.10 sec: 231.96x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                     |

Benchmark hidden because not significant (4): json, nbody, asyncio_websockets, pycparser
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241113-3.14.0a1+-47eb1b5/bm-20241113-pythonperf2-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 57.42% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x