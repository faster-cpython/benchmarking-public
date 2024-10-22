# Results vs. 3.13.0

- fork: faster-cpython
- ref: immortal_ref_count_s
- machine: linux-x86_64
- commit hash: 506492e
- commit date: 2024-09-20
- overall geometric mean: 1.02x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 254 ms: 1.04x faster                                                            |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.03x slower                                                          |
| html5lib       | 64.5 ms                                                | 63.4 ms: 1.02x faster                                                           |
| tornado_http   | 91.5 ms                                                | 91.1 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 388 ms: 1.20x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 390 ms: 1.14x faster                                                            |
| async_tree_none           | 354 ms                                                 | 312 ms: 1.13x faster                                                            |
| async_tree_none_tg        | 320 ms                                                 | 306 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 557 ms: 1.03x faster                                                            |
| asyncio_tcp               | 488 ms                                                 | 481 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| coroutines                | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                           |
| async_tree_io_tg          | 825 ms                                                 | 875 ms: 1.06x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (4): asyncio_websockets, async_generators, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 76.2 ms: 1.03x faster                                                           |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                            |
| nbody          | 85.7 ms                                                | 87.7 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.66 ms: 1.06x faster                                                           |
| regex_compile  | 131 ms                                                 | 127 ms: 1.03x faster                                                            |
| regex_v8       | 25.3 ms                                                | 24.8 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle               | 11.6 us                                                | 11.2 us: 1.03x faster                                                           |
| xml_etree_process    | 60.4 ms                                                | 58.5 ms: 1.03x faster                                                           |
| xml_etree_generate   | 87.0 ms                                                | 84.4 ms: 1.03x faster                                                           |
| tomli_loads          | 2.11 sec                                               | 2.06 sec: 1.03x faster                                                          |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| unpickle             | 14.9 us                                                | 14.7 us: 1.01x faster                                                           |
| json_loads           | 27.0 us                                                | 26.6 us: 1.01x faster                                                           |
| pickle_dict          | 33.2 us                                                | 33.5 us: 1.01x slower                                                           |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                            |
| pickle_pure_python   | 300 us                                                 | 305 us: 1.02x slower                                                            |
| pickle_list          | 5.01 us                                                | 5.13 us: 1.02x slower                                                           |
| xml_etree_iterparse  | 102 ms                                                 | 106 ms: 1.04x slower                                                            |
| unpickle_list        | 4.96 us                                                | 5.40 us: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 6.98 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text    | 22.9 ms                                                | 22.0 ms: 1.04x faster                                                           |
| genshi_xml     | 50.3 ms                                                | 50.0 ms: 1.01x faster                                                           |
| mako           | 11.1 ms                                                | 11.1 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 259 us: 1.36x faster                                                            |
| deepcopy_memo             | 38.0 us                                                | 30.0 us: 1.27x faster                                                           |
| go                        | 142 ms                                                 | 118 ms: 1.20x faster                                                            |
| async_tree_memoization_tg | 465 ms                                                 | 388 ms: 1.20x faster                                                            |
| deepcopy_reduce           | 3.17 us                                                | 2.70 us: 1.17x faster                                                           |
| async_tree_memoization    | 442 ms                                                 | 390 ms: 1.14x faster                                                            |
| async_tree_none           | 354 ms                                                 | 312 ms: 1.13x faster                                                            |
| mdp                       | 2.74 sec                                               | 2.53 sec: 1.08x faster                                                          |
| regex_effbot              | 3.88 ms                                                | 3.66 ms: 1.06x faster                                                           |
| pathlib                   | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                           |
| pprint_safe_repr          | 744 ms                                                 | 707 ms: 1.05x faster                                                            |
| json                      | 5.20 ms                                                | 4.95 ms: 1.05x faster                                                           |
| async_tree_none_tg        | 320 ms                                                 | 306 ms: 1.05x faster                                                            |
| richards                  | 48.1 ms                                                | 46.0 ms: 1.05x faster                                                           |
| richards_super            | 54.4 ms                                                | 52.0 ms: 1.05x faster                                                           |
| 2to3                      | 265 ms                                                 | 254 ms: 1.04x faster                                                            |
| pprint_pformat            | 1.51 sec                                               | 1.45 sec: 1.04x faster                                                          |
| genshi_text               | 22.9 ms                                                | 22.0 ms: 1.04x faster                                                           |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.85 ms: 1.04x faster                                                           |
| pickle                    | 11.6 us                                                | 11.2 us: 1.03x faster                                                           |
| xml_etree_process         | 60.4 ms                                                | 58.5 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 557 ms: 1.03x faster                                                            |
| xml_etree_generate        | 87.0 ms                                                | 84.4 ms: 1.03x faster                                                           |
| thrift                    | 796 us                                                 | 773 us: 1.03x faster                                                            |
| regex_compile             | 131 ms                                                 | 127 ms: 1.03x faster                                                            |
| float                     | 78.5 ms                                                | 76.2 ms: 1.03x faster                                                           |
| generators                | 28.8 ms                                                | 28.0 ms: 1.03x faster                                                           |
| bench_thread_pool         | 815 us                                                 | 792 us: 1.03x faster                                                            |
| tomli_loads               | 2.11 sec                                               | 2.06 sec: 1.03x faster                                                          |
| sympy_integrate           | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                           |
| regex_v8                  | 25.3 ms                                                | 24.8 ms: 1.02x faster                                                           |
| sympy_str                 | 274 ms                                                 | 269 ms: 1.02x faster                                                            |
| html5lib                  | 64.5 ms                                                | 63.4 ms: 1.02x faster                                                           |
| spectral_norm             | 115 ms                                                 | 113 ms: 1.02x faster                                                            |
| pycparser                 | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                          |
| telco                     | 8.45 ms                                                | 8.32 ms: 1.02x faster                                                           |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.01x faster                                                            |
| asyncio_tcp               | 488 ms                                                 | 481 ms: 1.01x faster                                                            |
| json_dumps                | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| sympy_sum                 | 150 ms                                                 | 148 ms: 1.01x faster                                                            |
| sqlglot_optimize          | 53.9 ms                                                | 53.2 ms: 1.01x faster                                                           |
| unpickle                  | 14.9 us                                                | 14.7 us: 1.01x faster                                                           |
| json_loads                | 27.0 us                                                | 26.6 us: 1.01x faster                                                           |
| sqlglot_normalize         | 107 ms                                                 | 106 ms: 1.01x faster                                                            |
| crypto_pyaes              | 73.0 ms                                                | 72.4 ms: 1.01x faster                                                           |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| genshi_xml                | 50.3 ms                                                | 50.0 ms: 1.01x faster                                                           |
| unpack_sequence           | 42.4 ns                                                | 42.2 ns: 1.01x faster                                                           |
| tornado_http              | 91.5 ms                                                | 91.1 ms: 1.01x faster                                                           |
| nqueens                   | 80.6 ms                                                | 80.3 ms: 1.00x faster                                                           |
| gc_traversal              | 3.81 ms                                                | 3.79 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| python_startup_no_site    | 6.99 ms                                                | 6.98 ms: 1.00x faster                                                           |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x slower                                                            |
| mako                      | 11.1 ms                                                | 11.1 ms: 1.00x slower                                                           |
| raytrace                  | 262 ms                                                 | 262 ms: 1.00x slower                                                            |
| pickle_dict               | 33.2 us                                                | 33.5 us: 1.01x slower                                                           |
| sqlglot_parse             | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                           |
| chaos                     | 58.4 ms                                                | 59.0 ms: 1.01x slower                                                           |
| comprehensions            | 16.4 us                                                | 16.6 us: 1.01x slower                                                           |
| unpickle_pure_python      | 213 us                                                 | 216 us: 1.01x slower                                                            |
| deltablue                 | 3.15 ms                                                | 3.19 ms: 1.01x slower                                                           |
| scimark_monte_carlo       | 66.3 ms                                                | 67.1 ms: 1.01x slower                                                           |
| hexiom                    | 6.13 ms                                                | 6.21 ms: 1.01x slower                                                           |
| pickle_pure_python        | 300 us                                                 | 305 us: 1.02x slower                                                            |
| scimark_sor               | 122 ms                                                 | 124 ms: 1.02x slower                                                            |
| bpe_tokeniser             | 4.69 sec                                               | 4.79 sec: 1.02x slower                                                          |
| nbody                     | 85.7 ms                                                | 87.7 ms: 1.02x slower                                                           |
| pickle_list               | 5.01 us                                                | 5.13 us: 1.02x slower                                                           |
| docutils                  | 2.58 sec                                               | 2.65 sec: 1.03x slower                                                          |
| pyflate                   | 460 ms                                                 | 474 ms: 1.03x slower                                                            |
| coroutines                | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                           |
| xml_etree_iterparse       | 102 ms                                                 | 106 ms: 1.04x slower                                                            |
| dulwich_log               | 63.0 ms                                                | 65.2 ms: 1.04x slower                                                           |
| coverage                  | 83.7 ms                                                | 87.1 ms: 1.04x slower                                                           |
| fannkuch                  | 381 ms                                                 | 400 ms: 1.05x slower                                                            |
| async_tree_io_tg          | 825 ms                                                 | 875 ms: 1.06x slower                                                            |
| create_gc_cycles          | 1.61 ms                                                | 1.73 ms: 1.07x slower                                                           |
| unpickle_list             | 4.96 us                                                | 5.40 us: 1.09x slower                                                           |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (18): logging_simple, logging_format, scimark_lu, scimark_fft, sympy_expand, typing_runtime_protocols, asyncio_websockets, django_template, async_generators, bench_mp_pool, sqlglot_transpile, regex_dna, sqlite_synth, xml_etree_parse, async_tree_cpu_io_mixed_tg, async_tree_io, logging_silent, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x