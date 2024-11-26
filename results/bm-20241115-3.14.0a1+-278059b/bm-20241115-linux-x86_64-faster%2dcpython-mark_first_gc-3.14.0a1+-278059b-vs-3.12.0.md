# Results vs. 3.12.0

- fork: faster-cpython
- ref: mark_first_gc
- machine: linux-x86_64
- commit hash: 278059b
- commit date: 2024-11-15
- overall geometric mean: 1.095x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 263 ms: 1.04x faster                                                      |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 627 ms: 1.89x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 643 ms: 1.80x faster                                                      |
| async_tree_none            | 472 ms                                                 | 283 ms: 1.67x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 271 ms: 1.66x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 352 ms: 1.63x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 358 ms: 1.62x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 502 ms: 1.45x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 514 ms: 1.41x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.63x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 84.2 ms: 1.01x faster                                                     |
| nbody          | 97.0 ms                                                | 96.5 ms: 1.01x faster                                                     |
| pidigits       | 187 ms                                                 | 192 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                      |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                      |
| regex_effbot   | 3.61 ms                                                | 3.86 ms: 1.07x slower                                                     |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.11 sec: 1.10x faster                                                    |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 221 us: 1.04x faster                                                      |
| xml_etree_parse      | 159 ms                                                 | 155 ms: 1.03x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 87.9 ms: 1.01x faster                                                     |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 117 ms: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.72 ms: 1.03x faster                                                     |
| python_startup         | 9.55 ms                                                | 12.4 ms: 1.30x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.9 ms: 1.05x faster                                                     |
| mako            | 11.9 ms                                                | 11.6 ms: 1.03x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 627 ms: 1.89x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 643 ms: 1.80x faster                                                      |
| async_tree_none            | 472 ms                                                 | 283 ms: 1.67x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 2.29 ms: 1.66x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 271 ms: 1.66x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 352 ms: 1.63x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 358 ms: 1.62x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 502 ms: 1.45x faster                                                      |
| deepcopy                   | 371 us                                                 | 262 us: 1.41x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 514 ms: 1.41x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 30.8 us: 1.32x faster                                                     |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.20x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                                     |
| logging_format             | 7.23 us                                                | 6.23 us: 1.16x faster                                                     |
| go                         | 139 ms                                                 | 121 ms: 1.15x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.15x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.14x faster                                                      |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.5 ms: 1.14x faster                                                     |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                      |
| generators                 | 31.2 ms                                                | 27.9 ms: 1.12x faster                                                     |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 2.11 sec: 1.10x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 74.6 ms: 1.10x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 68.6 ms: 1.10x faster                                                     |
| chaos                      | 67.0 ms                                                | 61.5 ms: 1.09x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.42 ms: 1.09x faster                                                     |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.07x faster                                                     |
| json                       | 5.26 ms                                                | 4.92 ms: 1.07x faster                                                     |
| async_generators           | 463 ms                                                 | 433 ms: 1.07x faster                                                      |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 728 ms: 1.06x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                    |
| sympy_expand               | 478 ms                                                 | 454 ms: 1.05x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 65.1 ms: 1.05x faster                                                     |
| django_template            | 34.6 ms                                                | 32.9 ms: 1.05x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                    |
| scimark_fft                | 382 ms                                                 | 364 ms: 1.05x faster                                                      |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                      |
| 2to3                       | 274 ms                                                 | 263 ms: 1.04x faster                                                      |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 221 us: 1.04x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                     |
| python_startup_no_site     | 6.94 ms                                                | 6.72 ms: 1.03x faster                                                     |
| nqueens                    | 83.3 ms                                                | 80.8 ms: 1.03x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 155 ms: 1.03x faster                                                      |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.03x faster                                                     |
| pyflate                    | 482 ms                                                 | 472 ms: 1.02x faster                                                      |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.98 ms: 1.01x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 87.9 ms: 1.01x faster                                                     |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.01x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 54.3 ms: 1.01x faster                                                     |
| hexiom                     | 6.41 ms                                                | 6.37 ms: 1.01x faster                                                     |
| float                      | 84.7 ms                                                | 84.2 ms: 1.01x faster                                                     |
| nbody                      | 97.0 ms                                                | 96.5 ms: 1.01x faster                                                     |
| fannkuch                   | 417 ms                                                 | 415 ms: 1.00x faster                                                      |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 851 us: 1.01x slower                                                      |
| spectral_norm              | 115 ms                                                 | 117 ms: 1.02x slower                                                      |
| sqlite_synth               | 2.83 us                                                | 2.88 us: 1.02x slower                                                     |
| richards                   | 45.8 ms                                                | 46.8 ms: 1.02x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                                      |
| pidigits                   | 187 ms                                                 | 192 ms: 1.03x slower                                                      |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                                     |
| richards_super             | 51.5 ms                                                | 53.2 ms: 1.03x slower                                                     |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                      |
| logging_silent             | 104 ns                                                 | 109 ns: 1.04x slower                                                      |
| regex_effbot               | 3.61 ms                                                | 3.86 ms: 1.07x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 117 ms: 1.09x slower                                                      |
| telco                      | 7.10 ms                                                | 7.83 ms: 1.10x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.67 ms: 1.13x slower                                                     |
| coverage                   | 72.7 ms                                                | 88.1 ms: 1.21x slower                                                     |
| python_startup             | 9.55 ms                                                | 12.4 ms: 1.30x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 83.5 ms: 3.48x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_process
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241115-3.14.0a1+-278059b/bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.095x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.08x