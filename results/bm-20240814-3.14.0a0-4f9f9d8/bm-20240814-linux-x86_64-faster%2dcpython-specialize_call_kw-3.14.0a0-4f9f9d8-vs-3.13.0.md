# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_call_kw
- machine: linux-x86_64
- commit hash: 4f9f9d8
- commit date: 2024-08-14
- overall geometric mean: 1.02x faster
- HPT reliability: 82.40%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 262 ms: 1.01x faster                                                          |
| docutils       | 2.58 sec                                               | 2.73 sec: 1.06x slower                                                        |
| html5lib       | 64.5 ms                                                | 64.2 ms: 1.01x faster                                                         |
| tornado_http   | 91.5 ms                                                | 90.4 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 392 ms: 1.19x faster                                                          |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                                          |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                          |
| async_tree_memoization     | 442 ms                                                 | 413 ms: 1.07x faster                                                          |
| asyncio_tcp                | 488 ms                                                 | 478 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 533 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 565 ms: 1.02x faster                                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.01x faster                                                        |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                         |
| async_tree_io              | 843 ms                                                 | 898 ms: 1.07x slower                                                          |
| async_tree_io_tg           | 825 ms                                                 | 889 ms: 1.08x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                  |

Benchmark hidden because not significant (2): async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                          |
| nbody          | 85.7 ms                                                | 86.8 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.80 ms: 1.02x faster                                                         |
| regex_compile  | 131 ms                                                 | 130 ms: 1.01x faster                                                          |
| regex_dna      | 220 ms                                                 | 223 ms: 1.01x slower                                                          |
| regex_v8       | 25.3 ms                                                | 26.2 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 2.05 sec: 1.03x faster                                                        |
| xml_etree_process    | 60.4 ms                                                | 60.1 ms: 1.01x faster                                                         |
| unpickle_pure_python | 213 us                                                 | 212 us: 1.00x faster                                                          |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.02x slower                                                          |
| json_loads           | 27.0 us                                                | 28.4 us: 1.05x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (4): xml_etree_parse, json_dumps, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                         |
| python_startup_no_site | 6.99 ms                                                | 7.03 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 33.7 ms: 1.02x faster                                                         |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                         |
| genshi_xml      | 50.3 ms                                                | 51.2 ms: 1.02x slower                                                         |
| genshi_text     | 22.9 ms                                                | 23.3 ms: 1.02x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 260 us: 1.35x faster                                                          |
| deepcopy_memo              | 38.0 us                                                | 29.7 us: 1.28x faster                                                         |
| deepcopy_reduce            | 3.17 us                                                | 2.66 us: 1.19x faster                                                         |
| async_tree_memoization_tg  | 465 ms                                                 | 392 ms: 1.19x faster                                                          |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                                          |
| pathlib                    | 17.1 ms                                                | 15.7 ms: 1.09x faster                                                         |
| mdp                        | 2.74 sec                                               | 2.53 sec: 1.09x faster                                                        |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                          |
| async_tree_memoization     | 442 ms                                                 | 413 ms: 1.07x faster                                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.74 ms: 1.06x faster                                                         |
| logging_silent             | 102 ns                                                 | 97.0 ns: 1.05x faster                                                         |
| richards_super             | 54.4 ms                                                | 51.7 ms: 1.05x faster                                                         |
| richards                   | 48.1 ms                                                | 45.8 ms: 1.05x faster                                                         |
| logging_simple             | 5.66 us                                                | 5.42 us: 1.05x faster                                                         |
| bench_thread_pool          | 815 us                                                 | 785 us: 1.04x faster                                                          |
| telco                      | 8.45 ms                                                | 8.16 ms: 1.04x faster                                                         |
| logging_format             | 6.25 us                                                | 6.05 us: 1.03x faster                                                         |
| raytrace                   | 262 ms                                                 | 254 ms: 1.03x faster                                                          |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.03x faster                                                          |
| tomli_loads                | 2.11 sec                                               | 2.05 sec: 1.03x faster                                                        |
| nqueens                    | 80.6 ms                                                | 78.6 ms: 1.03x faster                                                         |
| regex_effbot               | 3.88 ms                                                | 3.80 ms: 1.02x faster                                                         |
| django_template            | 34.4 ms                                                | 33.7 ms: 1.02x faster                                                         |
| asyncio_tcp                | 488 ms                                                 | 478 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 533 ms: 1.02x faster                                                          |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                                          |
| thrift                     | 796 us                                                 | 781 us: 1.02x faster                                                          |
| hexiom                     | 6.13 ms                                                | 6.02 ms: 1.02x faster                                                         |
| gc_traversal               | 3.81 ms                                                | 3.75 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 565 ms: 1.02x faster                                                          |
| tornado_http               | 91.5 ms                                                | 90.4 ms: 1.01x faster                                                         |
| 2to3                       | 265 ms                                                 | 262 ms: 1.01x faster                                                          |
| pycparser                  | 1.19 sec                                               | 1.18 sec: 1.01x faster                                                        |
| scimark_fft                | 369 ms                                                 | 364 ms: 1.01x faster                                                          |
| generators                 | 28.8 ms                                                | 28.5 ms: 1.01x faster                                                         |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                         |
| regex_compile              | 131 ms                                                 | 130 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.01x faster                                                        |
| go                         | 142 ms                                                 | 141 ms: 1.01x faster                                                          |
| sqlglot_optimize           | 53.9 ms                                                | 53.6 ms: 1.01x faster                                                         |
| html5lib                   | 64.5 ms                                                | 64.2 ms: 1.01x faster                                                         |
| xml_etree_process          | 60.4 ms                                                | 60.1 ms: 1.01x faster                                                         |
| unpickle_pure_python       | 213 us                                                 | 212 us: 1.00x faster                                                          |
| sympy_integrate            | 19.9 ms                                                | 19.8 ms: 1.00x faster                                                         |
| deltablue                  | 3.15 ms                                                | 3.14 ms: 1.00x faster                                                         |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                          |
| crypto_pyaes               | 73.0 ms                                                | 73.1 ms: 1.00x slower                                                         |
| chaos                      | 58.4 ms                                                | 58.7 ms: 1.00x slower                                                         |
| pprint_pformat             | 1.51 sec                                               | 1.52 sec: 1.00x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.01x slower                                                          |
| scimark_sor                | 122 ms                                                 | 123 ms: 1.01x slower                                                          |
| python_startup_no_site     | 6.99 ms                                                | 7.03 ms: 1.01x slower                                                         |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                         |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                         |
| json                       | 5.20 ms                                                | 5.24 ms: 1.01x slower                                                         |
| nbody                      | 85.7 ms                                                | 86.8 ms: 1.01x slower                                                         |
| regex_dna                  | 220 ms                                                 | 223 ms: 1.01x slower                                                          |
| mako                       | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                         |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                         |
| genshi_xml                 | 50.3 ms                                                | 51.2 ms: 1.02x slower                                                         |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                         |
| scimark_monte_carlo        | 66.3 ms                                                | 67.5 ms: 1.02x slower                                                         |
| genshi_text                | 22.9 ms                                                | 23.3 ms: 1.02x slower                                                         |
| pyflate                    | 460 ms                                                 | 470 ms: 1.02x slower                                                          |
| xml_etree_iterparse        | 102 ms                                                 | 105 ms: 1.02x slower                                                          |
| typing_runtime_protocols   | 159 us                                                 | 163 us: 1.03x slower                                                          |
| bpe_tokeniser              | 4.69 sec                                               | 4.83 sec: 1.03x slower                                                        |
| regex_v8                   | 25.3 ms                                                | 26.2 ms: 1.04x slower                                                         |
| fannkuch                   | 381 ms                                                 | 398 ms: 1.05x slower                                                          |
| json_loads                 | 27.0 us                                                | 28.4 us: 1.05x slower                                                         |
| docutils                   | 2.58 sec                                               | 2.73 sec: 1.06x slower                                                        |
| async_tree_io              | 843 ms                                                 | 898 ms: 1.07x slower                                                          |
| async_tree_io_tg           | 825 ms                                                 | 889 ms: 1.08x slower                                                          |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                  |

Benchmark hidden because not significant (15): xml_etree_parse, sympy_str, json_dumps, pprint_safe_repr, sympy_expand, xml_etree_generate, float, meteor_contest, bench_mp_pool, coverage, sqlglot_normalize, async_generators, asyncio_websockets, pickle_pure_python, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 82.40% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x