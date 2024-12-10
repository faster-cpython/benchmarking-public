# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 1069d98
- commit date: 2024-12-10
- overall geometric mean: 1.082x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                      |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                    |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 637 ms: 1.86x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 639 ms: 1.81x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 258 ms: 1.74x faster                                                      |
| async_tree_none            | 472 ms                                                 | 275 ms: 1.71x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 345 ms: 1.68x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 482 ms: 1.50x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 500 ms: 1.45x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.69x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 79.3 ms: 1.07x faster                                                     |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                      |
| nbody          | 97.0 ms                                                | 99.3 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.40 ms: 1.06x faster                                                     |
| regex_dna      | 212 ms                                                 | 226 ms: 1.07x slower                                                      |
| regex_v8       | 23.1 ms                                                | 26.9 ms: 1.16x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.16x faster                                                      |
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.12x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 98.6 ms: 1.08x faster                                                     |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 85.8 ms: 1.04x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 59.5 ms: 1.04x faster                                                     |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                              |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                     |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                     |
| mako            | 11.9 ms                                                | 11.9 ms: 1.00x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 637 ms: 1.86x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 639 ms: 1.81x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 258 ms: 1.74x faster                                                      |
| async_tree_none            | 472 ms                                                 | 275 ms: 1.71x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 345 ms: 1.68x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 482 ms: 1.50x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 500 ms: 1.45x faster                                                      |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 30.4 us: 1.34x faster                                                     |
| comprehensions             | 21.8 us                                                | 17.4 us: 1.25x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                                     |
| go                         | 139 ms                                                 | 117 ms: 1.19x faster                                                      |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.17x faster                                                     |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.58 us: 1.16x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.16x faster                                                      |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.13x faster                                                     |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.5 ms: 1.13x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 72.5 ms: 1.13x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.12x faster                                                    |
| generators                 | 31.2 ms                                                | 28.1 ms: 1.11x faster                                                     |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 69.0 ms: 1.09x faster                                                     |
| async_generators           | 463 ms                                                 | 426 ms: 1.09x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 98.6 ms: 1.08x faster                                                     |
| chaos                      | 67.0 ms                                                | 62.0 ms: 1.08x faster                                                     |
| float                      | 84.7 ms                                                | 79.3 ms: 1.07x faster                                                     |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                      |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.07x faster                                                     |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                                     |
| django_template            | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                     |
| regex_effbot               | 3.61 ms                                                | 3.40 ms: 1.06x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                     |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                    |
| dulwich_log                | 68.5 ms                                                | 65.5 ms: 1.05x faster                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.04x faster                                                     |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 85.8 ms: 1.04x faster                                                     |
| scimark_fft                | 382 ms                                                 | 368 ms: 1.04x faster                                                      |
| hexiom                     | 6.41 ms                                                | 6.18 ms: 1.04x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 59.5 ms: 1.04x faster                                                     |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                                      |
| json                       | 5.26 ms                                                | 5.07 ms: 1.04x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 750 ms: 1.03x faster                                                      |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                      |
| sympy_expand               | 478 ms                                                 | 465 ms: 1.03x faster                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 53.8 ms: 1.02x faster                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.00 ms: 1.01x faster                                                     |
| scimark_sor                | 129 ms                                                 | 128 ms: 1.01x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                      |
| mako                       | 11.9 ms                                                | 11.9 ms: 1.00x slower                                                     |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                     |
| fannkuch                   | 417 ms                                                 | 424 ms: 1.02x slower                                                      |
| nqueens                    | 83.3 ms                                                | 84.6 ms: 1.02x slower                                                     |
| richards_super             | 51.5 ms                                                | 52.7 ms: 1.02x slower                                                     |
| nbody                      | 97.0 ms                                                | 99.3 ms: 1.02x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 863 us: 1.03x slower                                                      |
| mdp                        | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                    |
| coroutines                 | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                     |
| sqlite_synth               | 2.83 us                                                | 2.92 us: 1.03x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                      |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.07x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                     |
| telco                      | 7.10 ms                                                | 7.87 ms: 1.11x slower                                                     |
| coverage                   | 72.7 ms                                                | 83.1 ms: 1.14x slower                                                     |
| mypy2                      | 830 ms                                                 | 952 ms: 1.15x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 26.9 ms: 1.16x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 5.03 ms: 1.33x slower                                                     |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                              |

Benchmark hidden because not significant (5): pyflate, richards, pycparser, pickle_pure_python, spectral_norm
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241210-3.14.0a2+-1069d98/bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.082x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.10x