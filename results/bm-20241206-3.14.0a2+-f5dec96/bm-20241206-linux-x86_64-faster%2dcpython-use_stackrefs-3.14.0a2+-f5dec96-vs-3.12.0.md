# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: f5dec96
- commit date: 2024-12-06
- overall geometric mean: 1.089x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.07x faster                                                      |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                    |
| Geometric mean | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 605 ms: 1.91x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 624 ms: 1.89x faster                                                      |
| async_tree_none            | 472 ms                                                 | 274 ms: 1.72x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 335 ms: 1.72x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 265 ms: 1.70x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 347 ms: 1.67x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 489 ms: 1.48x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 501 ms: 1.45x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.68x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.8 ms: 1.08x faster                                                     |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.35 ms: 1.08x faster                                                     |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                      |
| regex_v8       | 23.1 ms                                                | 26.4 ms: 1.14x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                                      |
| json_loads           | 28.5 us                                                | 26.2 us: 1.09x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 99.2 ms: 1.08x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 58.6 ms: 1.05x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 84.7 ms: 1.05x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 326 us: 1.01x slower                                                      |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                     |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                     |
| mako            | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 605 ms: 1.91x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 624 ms: 1.89x faster                                                      |
| async_tree_none            | 472 ms                                                 | 274 ms: 1.72x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 335 ms: 1.72x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 265 ms: 1.70x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 347 ms: 1.67x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 489 ms: 1.48x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 501 ms: 1.45x faster                                                      |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 30.0 us: 1.36x faster                                                     |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.79 us: 1.20x faster                                                     |
| go                         | 139 ms                                                 | 117 ms: 1.19x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                     |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                      |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                                      |
| logging_format             | 7.23 us                                                | 6.25 us: 1.16x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.25 ms: 1.14x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.13x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.71 us: 1.13x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 72.8 ms: 1.12x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                    |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.10x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.10x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 68.8 ms: 1.09x faster                                                     |
| chaos                      | 67.0 ms                                                | 61.4 ms: 1.09x faster                                                     |
| json_loads                 | 28.5 us                                                | 26.2 us: 1.09x faster                                                     |
| json                       | 5.26 ms                                                | 4.83 ms: 1.09x faster                                                     |
| django_template            | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                     |
| async_generators           | 463 ms                                                 | 429 ms: 1.08x faster                                                      |
| regex_effbot               | 3.61 ms                                                | 3.35 ms: 1.08x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 99.2 ms: 1.08x faster                                                     |
| float                      | 84.7 ms                                                | 78.8 ms: 1.08x faster                                                     |
| 2to3                       | 274 ms                                                 | 255 ms: 1.07x faster                                                      |
| generators                 | 31.2 ms                                                | 29.1 ms: 1.07x faster                                                     |
| logging_silent             | 104 ns                                                 | 97.5 ns: 1.07x faster                                                     |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                     |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 58.6 ms: 1.05x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 84.7 ms: 1.05x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 65.1 ms: 1.05x faster                                                     |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                      |
| sympy_expand               | 478 ms                                                 | 459 ms: 1.04x faster                                                      |
| scimark_fft                | 382 ms                                                 | 367 ms: 1.04x faster                                                      |
| hexiom                     | 6.41 ms                                                | 6.19 ms: 1.04x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 755 ms: 1.03x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                    |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 53.7 ms: 1.02x faster                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                    |
| pyflate                    | 482 ms                                                 | 476 ms: 1.01x faster                                                      |
| mako                       | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.62 sec: 1.00x faster                                                    |
| richards_super             | 51.5 ms                                                | 51.9 ms: 1.01x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                      |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                      |
| pickle_pure_python         | 324 us                                                 | 326 us: 1.01x slower                                                      |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                     |
| fannkuch                   | 417 ms                                                 | 423 ms: 1.02x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 855 us: 1.02x slower                                                      |
| spectral_norm              | 115 ms                                                 | 117 ms: 1.02x slower                                                      |
| scimark_sor                | 129 ms                                                 | 132 ms: 1.02x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.19 ms: 1.03x slower                                                     |
| nqueens                    | 83.3 ms                                                | 85.6 ms: 1.03x slower                                                     |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                      |
| coroutines                 | 23.2 ms                                                | 24.4 ms: 1.05x slower                                                     |
| telco                      | 7.10 ms                                                | 7.81 ms: 1.10x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 26.4 ms: 1.14x slower                                                     |
| coverage                   | 72.7 ms                                                | 83.2 ms: 1.15x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 4.57 ms: 1.20x slower                                                     |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.27 ms: 1.54x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 79.1 ms: 3.30x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                              |

Benchmark hidden because not significant (2): richards, nbody
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241206-3.14.0a2+-f5dec96/bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.089x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.09x