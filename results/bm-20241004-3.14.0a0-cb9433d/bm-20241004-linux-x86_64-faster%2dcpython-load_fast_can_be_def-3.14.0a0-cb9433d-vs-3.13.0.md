# Results vs. 3.13.0

- fork: faster-cpython
- ref: load_fast_can_be_def
- machine: linux-x86_64
- commit hash: cb9433d
- commit date: 2024-10-04
- overall geometric mean: 1.00x faster
- HPT reliability: 66.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 257 ms: 1.03x faster                                                            |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                          |
| html5lib       | 64.5 ms                                                | 62.2 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 386 ms: 1.20x faster                                                            |
| async_tree_none            | 354 ms                                                 | 312 ms: 1.13x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 392 ms: 1.13x faster                                                            |
| async_tree_none_tg         | 320 ms                                                 | 304 ms: 1.05x faster                                                            |
| asyncio_tcp                | 488 ms                                                 | 469 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 562 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.77 sec: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 550 ms: 1.01x slower                                                            |
| async_tree_io              | 843 ms                                                 | 874 ms: 1.04x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 859 ms: 1.04x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (3): coroutines, async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 77.1 ms: 1.02x faster                                                           |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                            |
| nbody          | 85.7 ms                                                | 88.0 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.75 ms: 1.04x faster                                                           |
| regex_dna      | 220 ms                                                 | 223 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                           |
| xml_etree_process    | 60.4 ms                                                | 59.3 ms: 1.02x faster                                                           |
| xml_etree_generate   | 87.0 ms                                                | 86.3 ms: 1.01x faster                                                           |
| tomli_loads          | 2.11 sec                                               | 2.10 sec: 1.01x faster                                                          |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                            |
| pickle_list          | 5.01 us                                                | 5.06 us: 1.01x slower                                                           |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                           |
| xml_etree_iterparse  | 102 ms                                                 | 104 ms: 1.02x slower                                                            |
| pickle_pure_python   | 300 us                                                 | 308 us: 1.03x slower                                                            |
| pickle_dict          | 33.2 us                                                | 34.1 us: 1.03x slower                                                           |
| unpickle_list        | 4.96 us                                                | 5.32 us: 1.07x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (3): unpickle, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 6.99 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text    | 22.9 ms                                                | 22.7 ms: 1.01x faster                                                           |
| mako           | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 262 us: 1.34x faster                                                            |
| deepcopy_memo              | 38.0 us                                                | 30.3 us: 1.26x faster                                                           |
| async_tree_memoization_tg  | 465 ms                                                 | 386 ms: 1.20x faster                                                            |
| go                         | 142 ms                                                 | 120 ms: 1.18x faster                                                            |
| deepcopy_reduce            | 3.17 us                                                | 2.75 us: 1.15x faster                                                           |
| async_tree_none            | 354 ms                                                 | 312 ms: 1.13x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 392 ms: 1.13x faster                                                            |
| mdp                        | 2.74 sec                                               | 2.51 sec: 1.09x faster                                                          |
| pathlib                    | 17.1 ms                                                | 15.9 ms: 1.08x faster                                                           |
| telco                      | 8.45 ms                                                | 8.00 ms: 1.06x faster                                                           |
| async_tree_none_tg         | 320 ms                                                 | 304 ms: 1.05x faster                                                            |
| thrift                     | 796 us                                                 | 763 us: 1.04x faster                                                            |
| asyncio_tcp                | 488 ms                                                 | 469 ms: 1.04x faster                                                            |
| pprint_safe_repr           | 744 ms                                                 | 716 ms: 1.04x faster                                                            |
| html5lib                   | 64.5 ms                                                | 62.2 ms: 1.04x faster                                                           |
| generators                 | 28.8 ms                                                | 27.8 ms: 1.04x faster                                                           |
| regex_effbot               | 3.88 ms                                                | 3.75 ms: 1.04x faster                                                           |
| pycparser                  | 1.19 sec                                               | 1.16 sec: 1.03x faster                                                          |
| 2to3                       | 265 ms                                                 | 257 ms: 1.03x faster                                                            |
| richards                   | 48.1 ms                                                | 46.9 ms: 1.03x faster                                                           |
| gc_traversal               | 3.81 ms                                                | 3.72 ms: 1.02x faster                                                           |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                           |
| pprint_pformat             | 1.51 sec                                               | 1.48 sec: 1.02x faster                                                          |
| richards_super             | 54.4 ms                                                | 53.2 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 562 ms: 1.02x faster                                                            |
| sqlite_synth               | 2.85 us                                                | 2.80 us: 1.02x faster                                                           |
| xml_etree_process          | 60.4 ms                                                | 59.3 ms: 1.02x faster                                                           |
| float                      | 78.5 ms                                                | 77.1 ms: 1.02x faster                                                           |
| json                       | 5.20 ms                                                | 5.11 ms: 1.02x faster                                                           |
| scimark_lu                 | 115 ms                                                 | 114 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.77 sec: 1.01x faster                                                          |
| sympy_str                  | 274 ms                                                 | 271 ms: 1.01x faster                                                            |
| genshi_text                | 22.9 ms                                                | 22.7 ms: 1.01x faster                                                           |
| crypto_pyaes               | 73.0 ms                                                | 72.3 ms: 1.01x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.01x faster                                                            |
| xml_etree_generate         | 87.0 ms                                                | 86.3 ms: 1.01x faster                                                           |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| tomli_loads                | 2.11 sec                                               | 2.10 sec: 1.01x faster                                                          |
| sqlglot_optimize           | 53.9 ms                                                | 53.6 ms: 1.01x faster                                                           |
| spectral_norm              | 115 ms                                                 | 115 ms: 1.00x faster                                                            |
| python_startup_no_site     | 6.99 ms                                                | 6.99 ms: 1.00x slower                                                           |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.00x slower                                                           |
| sympy_integrate            | 19.9 ms                                                | 20.0 ms: 1.00x slower                                                           |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                            |
| logging_format             | 6.25 us                                                | 6.30 us: 1.01x slower                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.08 ms: 1.01x slower                                                           |
| nqueens                    | 80.6 ms                                                | 81.5 ms: 1.01x slower                                                           |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 550 ms: 1.01x slower                                                            |
| pickle_list                | 5.01 us                                                | 5.06 us: 1.01x slower                                                           |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                           |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                           |
| regex_dna                  | 220 ms                                                 | 223 ms: 1.01x slower                                                            |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                           |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                            |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                                            |
| coverage                   | 83.7 ms                                                | 85.6 ms: 1.02x slower                                                           |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                          |
| xml_etree_iterparse        | 102 ms                                                 | 104 ms: 1.02x slower                                                            |
| typing_runtime_protocols   | 159 us                                                 | 163 us: 1.03x slower                                                            |
| pickle_pure_python         | 300 us                                                 | 308 us: 1.03x slower                                                            |
| nbody                      | 85.7 ms                                                | 88.0 ms: 1.03x slower                                                           |
| hexiom                     | 6.13 ms                                                | 6.29 ms: 1.03x slower                                                           |
| meteor_contest             | 108 ms                                                 | 111 ms: 1.03x slower                                                            |
| pickle_dict                | 33.2 us                                                | 34.1 us: 1.03x slower                                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.83 sec: 1.03x slower                                                          |
| scimark_monte_carlo        | 66.3 ms                                                | 68.3 ms: 1.03x slower                                                           |
| async_tree_io              | 843 ms                                                 | 874 ms: 1.04x slower                                                            |
| pyflate                    | 460 ms                                                 | 477 ms: 1.04x slower                                                            |
| scimark_sor                | 122 ms                                                 | 127 ms: 1.04x slower                                                            |
| dulwich_log                | 63.0 ms                                                | 65.5 ms: 1.04x slower                                                           |
| async_tree_io_tg           | 825 ms                                                 | 859 ms: 1.04x slower                                                            |
| deltablue                  | 3.15 ms                                                | 3.28 ms: 1.04x slower                                                           |
| bench_thread_pool          | 815 us                                                 | 850 us: 1.04x slower                                                            |
| chaos                      | 58.4 ms                                                | 61.7 ms: 1.06x slower                                                           |
| fannkuch                   | 381 ms                                                 | 403 ms: 1.06x slower                                                            |
| create_gc_cycles           | 1.61 ms                                                | 1.71 ms: 1.06x slower                                                           |
| unpickle_list              | 4.96 us                                                | 5.32 us: 1.07x slower                                                           |
| unpack_sequence            | 42.4 ns                                                | 50.9 ns: 1.20x slower                                                           |
| bench_mp_pool              | 24.0 ms                                                | 56.1 ms: 2.34x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (16): unpickle, xml_etree_parse, coroutines, sympy_expand, scimark_fft, async_generators, regex_compile, regex_v8, django_template, tornado_http, genshi_xml, asyncio_websockets, json_loads, sqlglot_normalize, logging_simple, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 66.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x