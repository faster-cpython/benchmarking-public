# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: flag_object_maybe_in
- machine: linux-x86_64
- commit hash: bb874c3
- commit date: 2024-06-07
- overall geometric mean: 1.00x slower
- HPT reliability: 94.96%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 272 ms: 1.01x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.78 sec: 1.02x faster                                                          |
| html5lib       | 67.2 ms                                                    | 66.9 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|-------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg      | 336 ms                                                     | 344 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed | 611 ms                                                     | 632 ms: 1.03x slower                                                            |
| Geometric mean          | (ref)                                                      | 1.02x slower                                                                    |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 190 ms: 1.01x faster                                                            |
| float          | 78.9 ms                                                    | 79.7 ms: 1.01x slower                                                           |
| nbody          | 88.3 ms                                                    | 97.0 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                      | 1.03x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                                           |
| regex_compile  | 137 ms                                                     | 135 ms: 1.01x faster                                                            |
| regex_effbot   | 3.67 ms                                                    | 3.74 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                      | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_dict          | 34.8 us                                                    | 33.7 us: 1.03x faster                                                           |
| xml_etree_parse      | 162 ms                                                     | 159 ms: 1.02x faster                                                            |
| json_dumps           | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                           |
| unpickle_list        | 5.34 us                                                    | 5.38 us: 1.01x slower                                                           |
| unpickle             | 15.1 us                                                    | 15.2 us: 1.01x slower                                                           |
| pickle_list          | 5.11 us                                                    | 5.15 us: 1.01x slower                                                           |
| pickle               | 11.5 us                                                    | 11.6 us: 1.02x slower                                                           |
| pickle_pure_python   | 305 us                                                     | 312 us: 1.02x slower                                                            |
| unpickle_pure_python | 218 us                                                     | 223 us: 1.02x slower                                                            |
| tomli_loads          | 2.12 sec                                                   | 2.21 sec: 1.04x slower                                                          |
| Geometric mean       | (ref)                                                      | 1.00x slower                                                                    |

Benchmark hidden because not significant (4): json_loads, xml_etree_generate, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.7 ms: 1.00x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                      | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 23.8 ms: 1.00x slower                                                           |
| genshi_xml      | 51.6 ms                                                    | 52.1 ms: 1.01x slower                                                           |
| django_template | 34.8 ms                                                    | 35.3 ms: 1.01x slower                                                           |
| mako            | 11.2 ms                                                    | 11.5 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|-------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                     | 2.79 sec                                                   | 2.59 sec: 1.08x faster                                                          |
| pathlib                 | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                                           |
| scimark_sparse_mat_mult | 5.27 ms                                                    | 5.01 ms: 1.05x faster                                                           |
| gc_traversal            | 3.98 ms                                                    | 3.79 ms: 1.05x faster                                                           |
| scimark_fft             | 392 ms                                                     | 376 ms: 1.04x faster                                                            |
| pickle_dict             | 34.8 us                                                    | 33.7 us: 1.03x faster                                                           |
| richards                | 50.9 ms                                                    | 49.4 ms: 1.03x faster                                                           |
| scimark_lu              | 122 ms                                                     | 119 ms: 1.03x faster                                                            |
| richards_super          | 57.4 ms                                                    | 56.0 ms: 1.02x faster                                                           |
| create_gc_cycles        | 1.82 ms                                                    | 1.77 ms: 1.02x faster                                                           |
| dulwich_log             | 67.2 ms                                                    | 65.6 ms: 1.02x faster                                                           |
| logging_silent          | 105 ns                                                     | 102 ns: 1.02x faster                                                            |
| sqlite_synth            | 2.99 us                                                    | 2.93 us: 1.02x faster                                                           |
| deepcopy_reduce         | 3.35 us                                                    | 3.29 us: 1.02x faster                                                           |
| docutils                | 2.83 sec                                                   | 2.78 sec: 1.02x faster                                                          |
| thrift                  | 823 us                                                     | 810 us: 1.02x faster                                                            |
| asyncio_tcp             | 508 ms                                                     | 500 ms: 1.02x faster                                                            |
| xml_etree_parse         | 162 ms                                                     | 159 ms: 1.02x faster                                                            |
| regex_v8                | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                                           |
| regex_compile           | 137 ms                                                     | 135 ms: 1.01x faster                                                            |
| json_dumps              | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                           |
| coverage                | 93.1 ms                                                    | 92.4 ms: 1.01x faster                                                           |
| 2to3                    | 274 ms                                                     | 272 ms: 1.01x faster                                                            |
| pidigits                | 191 ms                                                     | 190 ms: 1.01x faster                                                            |
| html5lib                | 67.2 ms                                                    | 66.9 ms: 1.00x faster                                                           |
| crypto_pyaes            | 77.5 ms                                                    | 77.2 ms: 1.00x faster                                                           |
| sqlglot_transpile       | 1.63 ms                                                    | 1.63 ms: 1.00x faster                                                           |
| python_startup          | 10.8 ms                                                    | 10.7 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl         | 1.84 sec                                                   | 1.84 sec: 1.00x slower                                                          |
| python_startup_no_site  | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                                           |
| genshi_text             | 23.7 ms                                                    | 23.8 ms: 1.00x slower                                                           |
| sympy_expand            | 473 ms                                                     | 475 ms: 1.00x slower                                                            |
| deepcopy                | 367 us                                                     | 369 us: 1.00x slower                                                            |
| coroutines              | 23.2 ms                                                    | 23.3 ms: 1.01x slower                                                           |
| sympy_sum               | 156 ms                                                     | 157 ms: 1.01x slower                                                            |
| sqlglot_normalize       | 110 ms                                                     | 111 ms: 1.01x slower                                                            |
| bench_thread_pool       | 834 us                                                     | 840 us: 1.01x slower                                                            |
| pprint_pformat          | 1.56 sec                                                   | 1.57 sec: 1.01x slower                                                          |
| unpickle_list           | 5.34 us                                                    | 5.38 us: 1.01x slower                                                           |
| sympy_integrate         | 20.5 ms                                                    | 20.7 ms: 1.01x slower                                                           |
| unpickle                | 15.1 us                                                    | 15.2 us: 1.01x slower                                                           |
| hexiom                  | 6.30 ms                                                    | 6.35 ms: 1.01x slower                                                           |
| pickle_list             | 5.11 us                                                    | 5.15 us: 1.01x slower                                                           |
| float                   | 78.9 ms                                                    | 79.7 ms: 1.01x slower                                                           |
| meteor_contest          | 110 ms                                                     | 111 ms: 1.01x slower                                                            |
| genshi_xml              | 51.6 ms                                                    | 52.1 ms: 1.01x slower                                                           |
| comprehensions          | 16.6 us                                                    | 16.8 us: 1.01x slower                                                           |
| deepcopy_memo           | 39.7 us                                                    | 40.2 us: 1.01x slower                                                           |
| go                      | 145 ms                                                     | 146 ms: 1.01x slower                                                            |
| django_template         | 34.8 ms                                                    | 35.3 ms: 1.01x slower                                                           |
| json                    | 5.31 ms                                                    | 5.38 ms: 1.01x slower                                                           |
| pprint_safe_repr        | 758 ms                                                     | 770 ms: 1.01x slower                                                            |
| async_generators        | 442 ms                                                     | 449 ms: 1.01x slower                                                            |
| pickle                  | 11.5 us                                                    | 11.6 us: 1.02x slower                                                           |
| spectral_norm           | 116 ms                                                     | 118 ms: 1.02x slower                                                            |
| scimark_monte_carlo     | 69.2 ms                                                    | 70.3 ms: 1.02x slower                                                           |
| regex_effbot            | 3.67 ms                                                    | 3.74 ms: 1.02x slower                                                           |
| pickle_pure_python      | 305 us                                                     | 312 us: 1.02x slower                                                            |
| unpickle_pure_python    | 218 us                                                     | 223 us: 1.02x slower                                                            |
| async_tree_none_tg      | 336 ms                                                     | 344 ms: 1.02x slower                                                            |
| mako                    | 11.2 ms                                                    | 11.5 ms: 1.02x slower                                                           |
| logging_simple          | 5.74 us                                                    | 5.87 us: 1.02x slower                                                           |
| fannkuch                | 402 ms                                                     | 411 ms: 1.02x slower                                                            |
| raytrace                | 267 ms                                                     | 273 ms: 1.02x slower                                                            |
| deltablue               | 3.25 ms                                                    | 3.34 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed | 611 ms                                                     | 632 ms: 1.03x slower                                                            |
| tomli_loads             | 2.12 sec                                                   | 2.21 sec: 1.04x slower                                                          |
| pyflate                 | 484 ms                                                     | 514 ms: 1.06x slower                                                            |
| nbody                   | 88.3 ms                                                    | 97.0 ms: 1.10x slower                                                           |
| Geometric mean          | (ref)                                                      | 1.00x slower                                                                    |

Benchmark hidden because not significant (27): async_tree_io_tg, pylint, sqlglot_parse, sympy_str, json_loads, nqueens, xml_etree_generate, xml_etree_process, async_tree_none, pycparser, generators, scimark_sor, telco, typing_runtime_protocols, asyncio_websockets, chaos, sqlglot_optimize, tornado_http, bench_mp_pool, logging_format, regex_dna, dask, xml_etree_iterparse, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 94.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x