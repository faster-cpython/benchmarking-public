# Results vs. 3.13.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.01x faster
- HPT reliability: 79.41%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 266 ms: 1.00x slower                                                            |
| docutils       | 2.58 sec                                               | 2.73 sec: 1.06x slower                                                          |
| html5lib       | 64.5 ms                                                | 65.9 ms: 1.02x slower                                                           |
| tornado_http   | 91.5 ms                                                | 90.6 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 392 ms: 1.18x faster                                                            |
| async_tree_none            | 354 ms                                                 | 324 ms: 1.09x faster                                                            |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 427 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 533 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 565 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                          |
| async_tree_io_tg           | 825 ms                                                 | 865 ms: 1.05x slower                                                            |
| async_tree_io              | 843 ms                                                 | 906 ms: 1.08x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (4): asyncio_websockets, asyncio_tcp, async_generators, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 76.4 ms: 1.03x faster                                                           |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| nbody          | 85.7 ms                                                | 86.4 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.70 ms: 1.05x faster                                                           |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                            |
| regex_v8       | 25.3 ms                                                | 25.1 ms: 1.01x faster                                                           |
| regex_compile  | 131 ms                                                 | 135 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process   | 60.4 ms                                                | 58.7 ms: 1.03x faster                                                           |
| xml_etree_generate  | 87.0 ms                                                | 85.2 ms: 1.02x faster                                                           |
| json_dumps          | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                           |
| pickle_pure_python  | 300 us                                                 | 307 us: 1.02x slower                                                            |
| xml_etree_iterparse | 102 ms                                                 | 105 ms: 1.03x slower                                                            |
| json_loads          | 27.0 us                                                | 27.8 us: 1.03x slower                                                           |
| Geometric mean      | (ref)                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): tomli_loads, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.06 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                           |
| django_template | 34.4 ms                                                | 35.5 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 263 us: 1.34x faster                                                            |
| deepcopy_memo              | 38.0 us                                                | 30.3 us: 1.26x faster                                                           |
| async_tree_memoization_tg  | 465 ms                                                 | 392 ms: 1.18x faster                                                            |
| deepcopy_reduce            | 3.17 us                                                | 2.77 us: 1.14x faster                                                           |
| async_tree_none            | 354 ms                                                 | 324 ms: 1.09x faster                                                            |
| mdp                        | 2.74 sec                                               | 2.52 sec: 1.09x faster                                                          |
| pathlib                    | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                           |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.71 ms: 1.07x faster                                                           |
| regex_effbot               | 3.88 ms                                                | 3.70 ms: 1.05x faster                                                           |
| gc_traversal               | 3.81 ms                                                | 3.65 ms: 1.04x faster                                                           |
| telco                      | 8.45 ms                                                | 8.12 ms: 1.04x faster                                                           |
| async_tree_memoization     | 442 ms                                                 | 427 ms: 1.04x faster                                                            |
| pycparser                  | 1.19 sec                                               | 1.15 sec: 1.04x faster                                                          |
| richards                   | 48.1 ms                                                | 46.5 ms: 1.04x faster                                                           |
| bench_thread_pool          | 815 us                                                 | 787 us: 1.04x faster                                                            |
| generators                 | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                           |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.03x faster                                                            |
| richards_super             | 54.4 ms                                                | 52.8 ms: 1.03x faster                                                           |
| xml_etree_process          | 60.4 ms                                                | 58.7 ms: 1.03x faster                                                           |
| float                      | 78.5 ms                                                | 76.4 ms: 1.03x faster                                                           |
| xml_etree_generate         | 87.0 ms                                                | 85.2 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 533 ms: 1.02x faster                                                            |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 565 ms: 1.02x faster                                                            |
| tornado_http               | 91.5 ms                                                | 90.6 ms: 1.01x faster                                                           |
| logging_format             | 6.25 us                                                | 6.19 us: 1.01x faster                                                           |
| nqueens                    | 80.6 ms                                                | 80.0 ms: 1.01x faster                                                           |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| regex_v8                   | 25.3 ms                                                | 25.1 ms: 1.01x faster                                                           |
| pprint_safe_repr           | 744 ms                                                 | 740 ms: 1.01x faster                                                            |
| sqlglot_optimize           | 53.9 ms                                                | 53.8 ms: 1.00x faster                                                           |
| sympy_integrate            | 19.9 ms                                                | 19.8 ms: 1.00x faster                                                           |
| 2to3                       | 265 ms                                                 | 266 ms: 1.00x slower                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                          |
| sqlglot_normalize          | 107 ms                                                 | 108 ms: 1.00x slower                                                            |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| scimark_lu                 | 115 ms                                                 | 116 ms: 1.01x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                           |
| nbody                      | 85.7 ms                                                | 86.4 ms: 1.01x slower                                                           |
| raytrace                   | 262 ms                                                 | 264 ms: 1.01x slower                                                            |
| coverage                   | 83.7 ms                                                | 84.6 ms: 1.01x slower                                                           |
| python_startup_no_site     | 6.99 ms                                                | 7.06 ms: 1.01x slower                                                           |
| sympy_expand               | 462 ms                                                 | 467 ms: 1.01x slower                                                            |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                           |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.02x slower                                                            |
| go                         | 142 ms                                                 | 144 ms: 1.02x slower                                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                           |
| chaos                      | 58.4 ms                                                | 59.5 ms: 1.02x slower                                                           |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                            |
| html5lib                   | 64.5 ms                                                | 65.9 ms: 1.02x slower                                                           |
| comprehensions             | 16.4 us                                                | 16.8 us: 1.02x slower                                                           |
| deltablue                  | 3.15 ms                                                | 3.22 ms: 1.02x slower                                                           |
| pickle_pure_python         | 300 us                                                 | 307 us: 1.02x slower                                                            |
| crypto_pyaes               | 73.0 ms                                                | 74.8 ms: 1.02x slower                                                           |
| mako                       | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                           |
| regex_compile              | 131 ms                                                 | 135 ms: 1.03x slower                                                            |
| django_template            | 34.4 ms                                                | 35.5 ms: 1.03x slower                                                           |
| xml_etree_iterparse        | 102 ms                                                 | 105 ms: 1.03x slower                                                            |
| json_loads                 | 27.0 us                                                | 27.8 us: 1.03x slower                                                           |
| hexiom                     | 6.13 ms                                                | 6.33 ms: 1.03x slower                                                           |
| typing_runtime_protocols   | 159 us                                                 | 166 us: 1.04x slower                                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.89 sec: 1.04x slower                                                          |
| scimark_monte_carlo        | 66.3 ms                                                | 69.4 ms: 1.05x slower                                                           |
| async_tree_io_tg           | 825 ms                                                 | 865 ms: 1.05x slower                                                            |
| docutils                   | 2.58 sec                                               | 2.73 sec: 1.06x slower                                                          |
| dask                       | 338 ms                                                 | 357 ms: 1.06x slower                                                            |
| pyflate                    | 460 ms                                                 | 490 ms: 1.07x slower                                                            |
| async_tree_io              | 843 ms                                                 | 906 ms: 1.08x slower                                                            |
| fannkuch                   | 381 ms                                                 | 409 ms: 1.08x slower                                                            |
| create_gc_cycles           | 1.61 ms                                                | 1.73 ms: 1.08x slower                                                           |
| scimark_sor                | 122 ms                                                 | 134 ms: 1.09x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (18): logging_simple, scimark_fft, json, tomli_loads, genshi_text, genshi_xml, thrift, unpickle_pure_python, asyncio_websockets, xml_etree_parse, pprint_pformat, bench_mp_pool, asyncio_tcp, async_generators, meteor_contest, sympy_str, coroutines, pylint
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 79.41% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x