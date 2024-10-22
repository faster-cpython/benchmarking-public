# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_call_ex
- machine: linux-x86_64
- commit hash: ade1f65
- commit date: 2024-08-15
- overall geometric mean: 1.01x faster
- HPT reliability: 93.36%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 262 ms: 1.01x faster                                                          |
| docutils       | 2.58 sec                                               | 2.72 sec: 1.05x slower                                                        |
| html5lib       | 64.5 ms                                                | 65.4 ms: 1.01x slower                                                         |
| tornado_http   | 91.5 ms                                                | 90.1 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 395 ms: 1.18x faster                                                          |
| async_tree_none           | 354 ms                                                 | 327 ms: 1.08x faster                                                          |
| async_tree_none_tg        | 320 ms                                                 | 301 ms: 1.06x faster                                                          |
| async_tree_memoization    | 442 ms                                                 | 425 ms: 1.04x faster                                                          |
| asyncio_tcp               | 488 ms                                                 | 479 ms: 1.02x faster                                                          |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.78 sec: 1.01x faster                                                        |
| asyncio_websockets        | 555 ms                                                 | 561 ms: 1.01x slower                                                          |
| async_generators          | 433 ms                                                 | 444 ms: 1.03x slower                                                          |
| coroutines                | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                         |
| async_tree_io             | 843 ms                                                 | 908 ms: 1.08x slower                                                          |
| async_tree_io_tg          | 825 ms                                                 | 897 ms: 1.09x slower                                                          |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                          |
| nbody          | 85.7 ms                                                | 86.9 ms: 1.01x slower                                                         |
| float          | 78.5 ms                                                | 79.8 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.61 ms: 1.08x faster                                                         |
| regex_dna      | 220 ms                                                 | 222 ms: 1.01x slower                                                          |
| regex_v8       | 25.3 ms                                                | 26.1 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 59.2 ms: 1.02x faster                                                         |
| tomli_loads          | 2.11 sec                                               | 2.09 sec: 1.01x faster                                                        |
| xml_etree_generate   | 87.0 ms                                                | 86.2 ms: 1.01x faster                                                         |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                         |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                          |
| pickle_pure_python   | 300 us                                                 | 306 us: 1.02x slower                                                          |
| xml_etree_iterparse  | 102 ms                                                 | 104 ms: 1.02x slower                                                          |
| json_loads           | 27.0 us                                                | 28.7 us: 1.06x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.4 ms: 1.01x faster                                                         |
| python_startup_no_site | 6.99 ms                                                | 7.03 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 34.2 ms: 1.01x faster                                                         |
| genshi_text     | 22.9 ms                                                | 23.2 ms: 1.01x slower                                                         |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 267 us: 1.32x faster                                                          |
| deepcopy_memo             | 38.0 us                                                | 30.9 us: 1.23x faster                                                         |
| async_tree_memoization_tg | 465 ms                                                 | 395 ms: 1.18x faster                                                          |
| deepcopy_reduce           | 3.17 us                                                | 2.70 us: 1.17x faster                                                         |
| async_tree_none           | 354 ms                                                 | 327 ms: 1.08x faster                                                          |
| mdp                       | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                        |
| regex_effbot              | 3.88 ms                                                | 3.61 ms: 1.08x faster                                                         |
| pathlib                   | 17.1 ms                                                | 15.9 ms: 1.08x faster                                                         |
| async_tree_none_tg        | 320 ms                                                 | 301 ms: 1.06x faster                                                          |
| spectral_norm             | 115 ms                                                 | 109 ms: 1.05x faster                                                          |
| async_tree_memoization    | 442 ms                                                 | 425 ms: 1.04x faster                                                          |
| bench_thread_pool         | 815 us                                                 | 785 us: 1.04x faster                                                          |
| richards                  | 48.1 ms                                                | 46.4 ms: 1.04x faster                                                         |
| telco                     | 8.45 ms                                                | 8.16 ms: 1.04x faster                                                         |
| richards_super            | 54.4 ms                                                | 52.8 ms: 1.03x faster                                                         |
| logging_format            | 6.25 us                                                | 6.09 us: 1.03x faster                                                         |
| logging_simple            | 5.66 us                                                | 5.52 us: 1.03x faster                                                         |
| xml_etree_process         | 60.4 ms                                                | 59.2 ms: 1.02x faster                                                         |
| asyncio_tcp               | 488 ms                                                 | 479 ms: 1.02x faster                                                          |
| nqueens                   | 80.6 ms                                                | 79.2 ms: 1.02x faster                                                         |
| thrift                    | 796 us                                                 | 783 us: 1.02x faster                                                          |
| tornado_http              | 91.5 ms                                                | 90.1 ms: 1.02x faster                                                         |
| 2to3                      | 265 ms                                                 | 262 ms: 1.01x faster                                                          |
| python_startup            | 10.6 ms                                                | 10.4 ms: 1.01x faster                                                         |
| scimark_lu                | 115 ms                                                 | 114 ms: 1.01x faster                                                          |
| tomli_loads               | 2.11 sec                                               | 2.09 sec: 1.01x faster                                                        |
| xml_etree_generate        | 87.0 ms                                                | 86.2 ms: 1.01x faster                                                         |
| generators                | 28.8 ms                                                | 28.6 ms: 1.01x faster                                                         |
| raytrace                  | 262 ms                                                 | 259 ms: 1.01x faster                                                          |
| django_template           | 34.4 ms                                                | 34.2 ms: 1.01x faster                                                         |
| sympy_integrate           | 19.9 ms                                                | 19.8 ms: 1.01x faster                                                         |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.78 sec: 1.01x faster                                                        |
| sqlglot_optimize          | 53.9 ms                                                | 53.8 ms: 1.00x faster                                                         |
| pidigits                  | 186 ms                                                 | 187 ms: 1.00x slower                                                          |
| sqlglot_normalize         | 107 ms                                                 | 108 ms: 1.00x slower                                                          |
| pyflate                   | 460 ms                                                 | 462 ms: 1.00x slower                                                          |
| gc_traversal              | 3.81 ms                                                | 3.82 ms: 1.00x slower                                                         |
| python_startup_no_site    | 6.99 ms                                                | 7.03 ms: 1.01x slower                                                         |
| sqlglot_transpile         | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                         |
| hexiom                    | 6.13 ms                                                | 6.17 ms: 1.01x slower                                                         |
| json_dumps                | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                         |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 5.07 ms: 1.01x slower                                                         |
| sympy_sum                 | 150 ms                                                 | 151 ms: 1.01x slower                                                          |
| asyncio_websockets        | 555 ms                                                 | 561 ms: 1.01x slower                                                          |
| regex_dna                 | 220 ms                                                 | 222 ms: 1.01x slower                                                          |
| coverage                  | 83.7 ms                                                | 84.7 ms: 1.01x slower                                                         |
| pprint_safe_repr          | 744 ms                                                 | 754 ms: 1.01x slower                                                          |
| nbody                     | 85.7 ms                                                | 86.9 ms: 1.01x slower                                                         |
| genshi_text               | 22.9 ms                                                | 23.2 ms: 1.01x slower                                                         |
| html5lib                  | 64.5 ms                                                | 65.4 ms: 1.01x slower                                                         |
| scimark_fft               | 369 ms                                                 | 374 ms: 1.01x slower                                                          |
| json                      | 5.20 ms                                                | 5.27 ms: 1.01x slower                                                         |
| mako                      | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                         |
| unpickle_pure_python      | 213 us                                                 | 217 us: 1.02x slower                                                          |
| sqlglot_parse             | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                         |
| float                     | 78.5 ms                                                | 79.8 ms: 1.02x slower                                                         |
| pickle_pure_python        | 300 us                                                 | 306 us: 1.02x slower                                                          |
| comprehensions            | 16.4 us                                                | 16.7 us: 1.02x slower                                                         |
| xml_etree_iterparse       | 102 ms                                                 | 104 ms: 1.02x slower                                                          |
| pprint_pformat            | 1.51 sec                                               | 1.54 sec: 1.02x slower                                                        |
| async_generators          | 433 ms                                                 | 444 ms: 1.03x slower                                                          |
| bpe_tokeniser             | 4.69 sec                                               | 4.83 sec: 1.03x slower                                                        |
| typing_runtime_protocols  | 159 us                                                 | 164 us: 1.03x slower                                                          |
| logging_silent            | 102 ns                                                 | 105 ns: 1.03x slower                                                          |
| deltablue                 | 3.15 ms                                                | 3.25 ms: 1.03x slower                                                         |
| coroutines                | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                         |
| regex_v8                  | 25.3 ms                                                | 26.1 ms: 1.03x slower                                                         |
| scimark_monte_carlo       | 66.3 ms                                                | 68.6 ms: 1.03x slower                                                         |
| fannkuch                  | 381 ms                                                 | 396 ms: 1.04x slower                                                          |
| scimark_sor               | 122 ms                                                 | 129 ms: 1.05x slower                                                          |
| docutils                  | 2.58 sec                                               | 2.72 sec: 1.05x slower                                                        |
| json_loads                | 27.0 us                                                | 28.7 us: 1.06x slower                                                         |
| async_tree_io             | 843 ms                                                 | 908 ms: 1.08x slower                                                          |
| create_gc_cycles          | 1.61 ms                                                | 1.75 ms: 1.08x slower                                                         |
| async_tree_io_tg          | 825 ms                                                 | 897 ms: 1.09x slower                                                          |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (14): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, pycparser, meteor_contest, regex_compile, bench_mp_pool, chaos, crypto_pyaes, go, sympy_str, xml_etree_parse, genshi_xml, sympy_expand, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 93.36% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x