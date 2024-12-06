# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 0c20416
- commit date: 2024-12-06
- overall geometric mean: 1.085x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                      |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                    |
| Geometric mean | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 605 ms: 1.91x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                      |
| async_tree_none            | 472 ms                                                 | 274 ms: 1.72x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 335 ms: 1.71x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 263 ms: 1.71x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 346 ms: 1.67x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 500 ms: 1.45x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.69x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.4 ms: 1.08x faster                                                     |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                      |
| nbody          | 97.0 ms                                                | 98.4 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.50 ms: 1.03x faster                                                     |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                                      |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 143 ms: 1.11x faster                                                      |
| tomli_loads          | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                    |
| json_loads           | 28.5 us                                                | 26.0 us: 1.09x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 99.4 ms: 1.07x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 84.5 ms: 1.05x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 331 us: 1.02x slower                                                      |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                     |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                     |
| mako            | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 605 ms: 1.91x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                      |
| async_tree_none            | 472 ms                                                 | 274 ms: 1.72x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 335 ms: 1.71x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 263 ms: 1.71x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 346 ms: 1.67x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 500 ms: 1.45x faster                                                      |
| deepcopy                   | 371 us                                                 | 268 us: 1.39x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 30.6 us: 1.33x faster                                                     |
| comprehensions             | 21.8 us                                                | 17.3 us: 1.26x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.81 us: 1.19x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                     |
| go                         | 139 ms                                                 | 118 ms: 1.18x faster                                                      |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                                      |
| logging_format             | 7.23 us                                                | 6.27 us: 1.15x faster                                                     |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 143 ms: 1.11x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 74.0 ms: 1.11x faster                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                                     |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                      |
| json_loads                 | 28.5 us                                                | 26.0 us: 1.09x faster                                                     |
| json                       | 5.26 ms                                                | 4.81 ms: 1.09x faster                                                     |
| generators                 | 31.2 ms                                                | 28.8 ms: 1.08x faster                                                     |
| async_generators           | 463 ms                                                 | 428 ms: 1.08x faster                                                      |
| float                      | 84.7 ms                                                | 78.4 ms: 1.08x faster                                                     |
| django_template            | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 69.8 ms: 1.08x faster                                                     |
| chaos                      | 67.0 ms                                                | 62.4 ms: 1.07x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 99.4 ms: 1.07x faster                                                     |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                      |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                      |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 84.5 ms: 1.05x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 65.3 ms: 1.05x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                     |
| sympy_expand               | 478 ms                                                 | 462 ms: 1.03x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                                     |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                                      |
| regex_effbot               | 3.61 ms                                                | 3.50 ms: 1.03x faster                                                     |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                                      |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                                      |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                     |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 54.2 ms: 1.01x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 769 ms: 1.01x faster                                                      |
| hexiom                     | 6.41 ms                                                | 6.36 ms: 1.01x faster                                                     |
| scimark_fft                | 382 ms                                                 | 379 ms: 1.01x faster                                                      |
| richards                   | 45.8 ms                                                | 45.6 ms: 1.01x faster                                                     |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                      |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.13 ms: 1.01x slower                                                     |
| nbody                      | 97.0 ms                                                | 98.4 ms: 1.01x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 857 us: 1.02x slower                                                      |
| pyflate                    | 482 ms                                                 | 492 ms: 1.02x slower                                                      |
| nqueens                    | 83.3 ms                                                | 84.9 ms: 1.02x slower                                                     |
| pickle_pure_python         | 324 us                                                 | 331 us: 1.02x slower                                                      |
| sqlite_synth               | 2.83 us                                                | 2.90 us: 1.02x slower                                                     |
| fannkuch                   | 417 ms                                                 | 429 ms: 1.03x slower                                                      |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.03x slower                                                      |
| mdp                        | 2.63 sec                                               | 2.72 sec: 1.04x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                      |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                                      |
| coroutines                 | 23.2 ms                                                | 24.5 ms: 1.06x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                     |
| telco                      | 7.10 ms                                                | 7.86 ms: 1.11x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                     |
| coverage                   | 72.7 ms                                                | 84.0 ms: 1.16x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 4.61 ms: 1.21x slower                                                     |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.24 ms: 1.51x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 78.7 ms: 3.28x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                              |

Benchmark hidden because not significant (2): pprint_pformat, richards_super
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241206-3.14.0a2+-0c20416/bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.085x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.09x