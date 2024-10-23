# Results vs. 3.13.0

- fork: faster-cpython
- ref: load_const_return_re
- machine: linux-x86_64
- commit hash: 2a3b1e2
- commit date: 2024-10-23
- overall geometric mean: 1.01x slower
- HPT reliability: 53.20%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 254 ms: 1.04x faster                                                             |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                           |
| html5lib       | 64.5 ms                                                | 63.4 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 386 ms: 1.20x faster                                                             |
| async_tree_none            | 354 ms                                                 | 327 ms: 1.08x faster                                                             |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                             |
| async_generators           | 433 ms                                                 | 427 ms: 1.01x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 556 ms: 1.02x slower                                                             |
| coroutines                 | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 977 ms: 1.18x slower                                                             |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                             |
| float          | 78.5 ms                                                | 80.3 ms: 1.02x slower                                                            |
| nbody          | 85.7 ms                                                | 95.8 ms: 1.12x slower                                                            |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.60 ms: 1.08x faster                                                            |
| regex_dna      | 220 ms                                                 | 214 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 27.0 us                                                | 26.2 us: 1.03x faster                                                            |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                             |
| xml_etree_iterparse  | 102 ms                                                 | 106 ms: 1.04x slower                                                             |
| pickle_pure_python   | 300 us                                                 | 315 us: 1.05x slower                                                             |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.06x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                     |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_generate, xml_etree_parse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                            |
| python_startup         | 10.6 ms                                                | 11.8 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 34.8 ms: 1.01x slower                                                            |
| mako            | 11.1 ms                                                | 11.4 ms: 1.02x slower                                                            |
| genshi_text     | 22.9 ms                                                | 23.8 ms: 1.04x slower                                                            |
| genshi_xml      | 50.3 ms                                                | 52.5 ms: 1.04x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 263 us: 1.34x faster                                                             |
| deepcopy_memo              | 38.0 us                                                | 31.1 us: 1.22x faster                                                            |
| async_tree_memoization_tg  | 465 ms                                                 | 386 ms: 1.20x faster                                                             |
| go                         | 142 ms                                                 | 120 ms: 1.18x faster                                                             |
| deepcopy_reduce            | 3.17 us                                                | 2.69 us: 1.18x faster                                                            |
| mdp                        | 2.74 sec                                               | 2.50 sec: 1.10x faster                                                           |
| async_tree_none            | 354 ms                                                 | 327 ms: 1.08x faster                                                             |
| regex_effbot               | 3.88 ms                                                | 3.60 ms: 1.08x faster                                                            |
| pathlib                    | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                            |
| generators                 | 28.8 ms                                                | 26.8 ms: 1.07x faster                                                            |
| json                       | 5.20 ms                                                | 4.85 ms: 1.07x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                             |
| telco                      | 8.45 ms                                                | 8.02 ms: 1.05x faster                                                            |
| pycparser                  | 1.19 sec                                               | 1.14 sec: 1.04x faster                                                           |
| richards                   | 48.1 ms                                                | 46.1 ms: 1.04x faster                                                            |
| 2to3                       | 265 ms                                                 | 254 ms: 1.04x faster                                                             |
| logging_silent             | 102 ns                                                 | 98.3 ns: 1.04x faster                                                            |
| richards_super             | 54.4 ms                                                | 52.7 ms: 1.03x faster                                                            |
| thrift                     | 796 us                                                 | 773 us: 1.03x faster                                                             |
| json_loads                 | 27.0 us                                                | 26.2 us: 1.03x faster                                                            |
| regex_dna                  | 220 ms                                                 | 214 ms: 1.03x faster                                                             |
| sympy_str                  | 274 ms                                                 | 267 ms: 1.02x faster                                                             |
| html5lib                   | 64.5 ms                                                | 63.4 ms: 1.02x faster                                                            |
| crypto_pyaes               | 73.0 ms                                                | 71.8 ms: 1.02x faster                                                            |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                             |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                             |
| async_generators           | 433 ms                                                 | 427 ms: 1.01x faster                                                             |
| sympy_expand               | 462 ms                                                 | 456 ms: 1.01x faster                                                             |
| sqlglot_optimize           | 53.9 ms                                                | 53.3 ms: 1.01x faster                                                            |
| logging_format             | 6.25 us                                                | 6.18 us: 1.01x faster                                                            |
| sqlglot_normalize          | 107 ms                                                 | 106 ms: 1.01x faster                                                             |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                             |
| scimark_fft                | 369 ms                                                 | 365 ms: 1.01x faster                                                             |
| pprint_safe_repr           | 744 ms                                                 | 738 ms: 1.01x faster                                                             |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                             |
| coverage                   | 83.7 ms                                                | 84.4 ms: 1.01x slower                                                            |
| python_startup_no_site     | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                            |
| django_template            | 34.4 ms                                                | 34.8 ms: 1.01x slower                                                            |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                            |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                            |
| dulwich_log                | 63.0 ms                                                | 64.0 ms: 1.02x slower                                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.77 sec: 1.02x slower                                                           |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                             |
| scimark_lu                 | 115 ms                                                 | 117 ms: 1.02x slower                                                             |
| typing_runtime_protocols   | 159 us                                                 | 163 us: 1.02x slower                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 556 ms: 1.02x slower                                                             |
| float                      | 78.5 ms                                                | 80.3 ms: 1.02x slower                                                            |
| mako                       | 11.1 ms                                                | 11.4 ms: 1.02x slower                                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.02x slower                                                            |
| hexiom                     | 6.13 ms                                                | 6.28 ms: 1.03x slower                                                            |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                           |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                                             |
| bench_thread_pool          | 815 us                                                 | 842 us: 1.03x slower                                                             |
| coroutines                 | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                            |
| deltablue                  | 3.15 ms                                                | 3.26 ms: 1.03x slower                                                            |
| genshi_text                | 22.9 ms                                                | 23.8 ms: 1.04x slower                                                            |
| genshi_xml                 | 50.3 ms                                                | 52.5 ms: 1.04x slower                                                            |
| xml_etree_iterparse        | 102 ms                                                 | 106 ms: 1.04x slower                                                             |
| scimark_monte_carlo        | 66.3 ms                                                | 69.1 ms: 1.04x slower                                                            |
| pickle_pure_python         | 300 us                                                 | 315 us: 1.05x slower                                                             |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.06x slower                                                            |
| fannkuch                   | 381 ms                                                 | 405 ms: 1.06x slower                                                             |
| chaos                      | 58.4 ms                                                | 62.6 ms: 1.07x slower                                                            |
| scimark_sor                | 122 ms                                                 | 132 ms: 1.08x slower                                                             |
| python_startup             | 10.6 ms                                                | 11.8 ms: 1.12x slower                                                            |
| nbody                      | 85.7 ms                                                | 95.8 ms: 1.12x slower                                                            |
| gc_traversal               | 3.81 ms                                                | 4.47 ms: 1.18x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 977 ms: 1.18x slower                                                             |
| create_gc_cycles           | 1.61 ms                                                | 2.67 ms: 1.66x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 78.7 ms: 3.28x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (18): async_tree_cpu_io_mixed, logging_simple, xml_etree_process, asyncio_websockets, scimark_sparse_mat_mult, pyflate, pprint_pformat, tornado_http, regex_compile, nqueens, regex_v8, xml_etree_generate, sympy_integrate, xml_etree_parse, tomli_loads, async_tree_none_tg, async_tree_io, pylint
Ignored benchmarks (16) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20241023-3.14.0a1+-2a3b1e2/bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2.json: sphinx

# HPT report

- Reliability score: 53.20% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.13x