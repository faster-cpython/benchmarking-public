# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: remove_slice_opcodes
- machine: linux-x86_64
- commit hash: 072a294
- commit date: 2024-05-24
- overall geometric mean: 1.00x faster
- HPT reliability: 76.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 271 ms: 1.01x faster                                                            |
| chameleon      | 7.22 ms                                                    | 7.05 ms: 1.02x faster                                                           |
| docutils       | 2.83 sec                                                   | 2.78 sec: 1.02x faster                                                          |
| html5lib       | 67.2 ms                                                    | 67.8 ms: 1.01x slower                                                           |
| tornado_http   | 94.6 ms                                                    | 94.2 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io          | 939 ms                                                     | 976 ms: 1.04x slower                                                            |
| async_tree_memoization | 463 ms                                                     | 485 ms: 1.05x slower                                                            |
| Geometric mean         | (ref)                                                      | 1.02x slower                                                                    |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 86.0 ms: 1.03x faster                                                           |
| pidigits       | 191 ms                                                     | 190 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 133 ms: 1.03x faster                                                            |
| regex_effbot   | 3.67 ms                                                    | 3.78 ms: 1.03x slower                                                           |
| regex_v8       | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                                           |
| regex_dna      | 221 ms                                                     | 230 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                      | 1.02x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 218 us                                                     | 215 us: 1.01x faster                                                            |
| xml_etree_process    | 61.2 ms                                                    | 60.3 ms: 1.01x faster                                                           |
| xml_etree_generate   | 87.4 ms                                                    | 86.8 ms: 1.01x faster                                                           |
| pickle_list          | 5.11 us                                                    | 5.07 us: 1.01x faster                                                           |
| pickle_dict          | 34.8 us                                                    | 34.9 us: 1.00x slower                                                           |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                                           |
| tomli_loads          | 2.12 sec                                                   | 2.16 sec: 1.02x slower                                                          |
| unpickle_list        | 5.34 us                                                    | 5.60 us: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                      | 1.00x slower                                                                    |

Benchmark hidden because not significant (6): xml_etree_parse, pickle_pure_python, xml_etree_iterparse, json_dumps, unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.14 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 51.6 ms                                                    | 52.1 ms: 1.01x slower                                                           |
| django_template | 34.8 ms                                                    | 35.2 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240524-linux-x86_64-faster%2dcpython-remove_slice_opcodes-3.14.0a0-072a294 |
|-------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| scimark_fft             | 392 ms                                                     | 365 ms: 1.07x faster                                                            |
| richards                | 50.9 ms                                                    | 47.5 ms: 1.07x faster                                                           |
| richards_super          | 57.4 ms                                                    | 54.3 ms: 1.06x faster                                                           |
| scimark_lu              | 122 ms                                                     | 117 ms: 1.04x faster                                                            |
| scimark_sparse_mat_mult | 5.27 ms                                                    | 5.05 ms: 1.04x faster                                                           |
| pathlib                 | 17.3 ms                                                    | 16.7 ms: 1.04x faster                                                           |
| crypto_pyaes            | 77.5 ms                                                    | 75.0 ms: 1.03x faster                                                           |
| python_startup          | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                           |
| scimark_monte_carlo     | 69.2 ms                                                    | 67.2 ms: 1.03x faster                                                           |
| hexiom                  | 6.30 ms                                                    | 6.12 ms: 1.03x faster                                                           |
| gc_traversal            | 3.98 ms                                                    | 3.87 ms: 1.03x faster                                                           |
| dulwich_log             | 67.2 ms                                                    | 65.4 ms: 1.03x faster                                                           |
| regex_compile           | 137 ms                                                     | 133 ms: 1.03x faster                                                            |
| nbody                   | 88.3 ms                                                    | 86.0 ms: 1.03x faster                                                           |
| chameleon               | 7.22 ms                                                    | 7.05 ms: 1.02x faster                                                           |
| chaos                   | 61.3 ms                                                    | 60.0 ms: 1.02x faster                                                           |
| deepcopy_reduce         | 3.35 us                                                    | 3.27 us: 1.02x faster                                                           |
| thrift                  | 823 us                                                     | 807 us: 1.02x faster                                                            |
| docutils                | 2.83 sec                                                   | 2.78 sec: 1.02x faster                                                          |
| unpickle_pure_python    | 218 us                                                     | 215 us: 1.01x faster                                                            |
| coverage                | 93.1 ms                                                    | 91.8 ms: 1.01x faster                                                           |
| xml_etree_process       | 61.2 ms                                                    | 60.3 ms: 1.01x faster                                                           |
| meteor_contest          | 110 ms                                                     | 109 ms: 1.01x faster                                                            |
| sqlglot_optimize        | 55.5 ms                                                    | 54.9 ms: 1.01x faster                                                           |
| 2to3                    | 274 ms                                                     | 271 ms: 1.01x faster                                                            |
| spectral_norm           | 116 ms                                                     | 115 ms: 1.01x faster                                                            |
| xml_etree_generate      | 87.4 ms                                                    | 86.8 ms: 1.01x faster                                                           |
| pidigits                | 191 ms                                                     | 190 ms: 1.01x faster                                                            |
| pprint_safe_repr        | 758 ms                                                     | 753 ms: 1.01x faster                                                            |
| pickle_list             | 5.11 us                                                    | 5.07 us: 1.01x faster                                                           |
| logging_silent          | 105 ns                                                     | 104 ns: 1.01x faster                                                            |
| sympy_integrate         | 20.5 ms                                                    | 20.4 ms: 1.01x faster                                                           |
| pprint_pformat          | 1.56 sec                                                   | 1.55 sec: 1.01x faster                                                          |
| tornado_http            | 94.6 ms                                                    | 94.2 ms: 1.01x faster                                                           |
| deepcopy                | 367 us                                                     | 366 us: 1.00x faster                                                            |
| sqlglot_normalize       | 110 ms                                                     | 110 ms: 1.00x faster                                                            |
| mdp                     | 2.79 sec                                                   | 2.78 sec: 1.00x faster                                                          |
| asyncio_tcp_ssl         | 1.84 sec                                                   | 1.85 sec: 1.00x slower                                                          |
| pickle_dict             | 34.8 us                                                    | 34.9 us: 1.00x slower                                                           |
| python_startup_no_site  | 7.11 ms                                                    | 7.14 ms: 1.01x slower                                                           |
| sqlglot_parse           | 1.32 ms                                                    | 1.33 ms: 1.01x slower                                                           |
| html5lib                | 67.2 ms                                                    | 67.8 ms: 1.01x slower                                                           |
| raytrace                | 267 ms                                                     | 269 ms: 1.01x slower                                                            |
| genshi_xml              | 51.6 ms                                                    | 52.1 ms: 1.01x slower                                                           |
| async_generators        | 442 ms                                                     | 447 ms: 1.01x slower                                                            |
| django_template         | 34.8 ms                                                    | 35.2 ms: 1.01x slower                                                           |
| json                    | 5.31 ms                                                    | 5.37 ms: 1.01x slower                                                           |
| coroutines              | 23.2 ms                                                    | 23.5 ms: 1.01x slower                                                           |
| pickle                  | 11.5 us                                                    | 11.6 us: 1.01x slower                                                           |
| pyflate                 | 484 ms                                                     | 491 ms: 1.01x slower                                                            |
| tomli_loads             | 2.12 sec                                                   | 2.16 sec: 1.02x slower                                                          |
| nqueens                 | 81.4 ms                                                    | 82.9 ms: 1.02x slower                                                           |
| deltablue               | 3.25 ms                                                    | 3.32 ms: 1.02x slower                                                           |
| logging_simple          | 5.74 us                                                    | 5.90 us: 1.03x slower                                                           |
| create_gc_cycles        | 1.82 ms                                                    | 1.87 ms: 1.03x slower                                                           |
| regex_effbot            | 3.67 ms                                                    | 3.78 ms: 1.03x slower                                                           |
| regex_v8                | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                                           |
| fannkuch                | 402 ms                                                     | 416 ms: 1.03x slower                                                            |
| async_tree_io           | 939 ms                                                     | 976 ms: 1.04x slower                                                            |
| regex_dna               | 221 ms                                                     | 230 ms: 1.04x slower                                                            |
| scimark_sor             | 127 ms                                                     | 133 ms: 1.04x slower                                                            |
| async_tree_memoization  | 463 ms                                                     | 485 ms: 1.05x slower                                                            |
| unpickle_list           | 5.34 us                                                    | 5.60 us: 1.05x slower                                                           |
| pycparser               | 1.16 sec                                                   | 1.25 sec: 1.08x slower                                                          |
| Geometric mean          | (ref)                                                      | 1.00x faster                                                                    |

Benchmark hidden because not significant (34): flaskblogging, sympy_str, xml_etree_parse, generators, genshi_text, pickle_pure_python, dask, go, mako, sympy_expand, telco, sqlite_synth, xml_etree_iterparse, asyncio_websockets, json_dumps, asyncio_tcp, sqlglot_transpile, sympy_sum, pylint, comprehensions, bench_mp_pool, deepcopy_memo, bench_thread_pool, float, async_tree_cpu_io_mixed_tg, typing_runtime_protocols, unpickle, json_loads, logging_format, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2

# HPT report

- Reliability score: 76.57% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x