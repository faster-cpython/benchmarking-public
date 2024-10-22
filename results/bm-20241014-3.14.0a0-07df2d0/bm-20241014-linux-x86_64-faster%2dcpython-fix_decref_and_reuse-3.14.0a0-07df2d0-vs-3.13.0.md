# Results vs. 3.13.0

- fork: faster-cpython
- ref: fix_decref_and_reuse
- machine: linux-x86_64
- commit hash: 07df2d0
- commit date: 2024-10-14
- overall geometric mean: 1.01x slower
- HPT reliability: 67.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 255 ms: 1.04x faster                                                            |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                          |
| html5lib       | 64.5 ms                                                | 62.1 ms: 1.04x faster                                                           |
| tornado_http   | 91.5 ms                                                | 90.4 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_tcp      | 488 ms                                                 | 480 ms: 1.02x faster                                                            |
| async_generators | 433 ms                                                 | 438 ms: 1.01x slower                                                            |
| coroutines       | 22.5 ms                                                | 23.4 ms: 1.04x slower                                                           |
| Geometric mean   | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| nbody          | 85.7 ms                                                | 94.2 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.63 ms: 1.07x faster                                                           |
| regex_compile  | 131 ms                                                 | 129 ms: 1.01x faster                                                            |
| regex_v8       | 25.3 ms                                                | 25.0 ms: 1.01x faster                                                           |
| regex_dna      | 220 ms                                                 | 221 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 59.8 ms: 1.01x faster                                                           |
| xml_etree_generate   | 87.0 ms                                                | 86.3 ms: 1.01x faster                                                           |
| json_loads           | 27.0 us                                                | 26.8 us: 1.01x faster                                                           |
| tomli_loads          | 2.11 sec                                               | 2.13 sec: 1.01x slower                                                          |
| pickle_list          | 5.01 us                                                | 5.11 us: 1.02x slower                                                           |
| pickle               | 11.6 us                                                | 11.9 us: 1.03x slower                                                           |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                                            |
| unpickle_pure_python | 213 us                                                 | 222 us: 1.04x slower                                                            |
| pickle_pure_python   | 300 us                                                 | 313 us: 1.04x slower                                                            |
| pickle_dict          | 33.2 us                                                | 35.0 us: 1.05x slower                                                           |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                           |
| unpickle_list        | 4.96 us                                                | 5.43 us: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                                    |

Benchmark hidden because not significant (2): unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.02 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 34.1 ms: 1.01x faster                                                           |
| mako            | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                           |
| genshi_xml      | 50.3 ms                                                | 51.9 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                | 352 us                                                 | 261 us: 1.35x faster                                                            |
| deepcopy_memo           | 38.0 us                                                | 31.2 us: 1.22x faster                                                           |
| deepcopy_reduce         | 3.17 us                                                | 2.68 us: 1.18x faster                                                           |
| go                      | 142 ms                                                 | 122 ms: 1.16x faster                                                            |
| mdp                     | 2.74 sec                                               | 2.53 sec: 1.08x faster                                                          |
| regex_effbot            | 3.88 ms                                                | 3.63 ms: 1.07x faster                                                           |
| pathlib                 | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                           |
| pycparser               | 1.19 sec                                               | 1.13 sec: 1.06x faster                                                          |
| telco                   | 8.45 ms                                                | 8.00 ms: 1.06x faster                                                           |
| scimark_sparse_mat_mult | 5.03 ms                                                | 4.76 ms: 1.06x faster                                                           |
| 2to3                    | 265 ms                                                 | 255 ms: 1.04x faster                                                            |
| html5lib                | 64.5 ms                                                | 62.1 ms: 1.04x faster                                                           |
| generators              | 28.8 ms                                                | 28.0 ms: 1.03x faster                                                           |
| richards_super          | 54.4 ms                                                | 53.0 ms: 1.03x faster                                                           |
| thrift                  | 796 us                                                 | 779 us: 1.02x faster                                                            |
| sympy_str               | 274 ms                                                 | 268 ms: 1.02x faster                                                            |
| json                    | 5.20 ms                                                | 5.09 ms: 1.02x faster                                                           |
| pprint_safe_repr        | 744 ms                                                 | 729 ms: 1.02x faster                                                            |
| sympy_sum               | 150 ms                                                 | 147 ms: 1.02x faster                                                            |
| richards                | 48.1 ms                                                | 47.3 ms: 1.02x faster                                                           |
| asyncio_tcp             | 488 ms                                                 | 480 ms: 1.02x faster                                                            |
| sympy_expand            | 462 ms                                                 | 455 ms: 1.02x faster                                                            |
| regex_compile           | 131 ms                                                 | 129 ms: 1.01x faster                                                            |
| tornado_http            | 91.5 ms                                                | 90.4 ms: 1.01x faster                                                           |
| meteor_contest          | 108 ms                                                 | 106 ms: 1.01x faster                                                            |
| pprint_pformat          | 1.51 sec                                               | 1.49 sec: 1.01x faster                                                          |
| regex_v8                | 25.3 ms                                                | 25.0 ms: 1.01x faster                                                           |
| xml_etree_process       | 60.4 ms                                                | 59.8 ms: 1.01x faster                                                           |
| sqlglot_optimize        | 53.9 ms                                                | 53.4 ms: 1.01x faster                                                           |
| django_template         | 34.4 ms                                                | 34.1 ms: 1.01x faster                                                           |
| spectral_norm           | 115 ms                                                 | 114 ms: 1.01x faster                                                            |
| sqlglot_normalize       | 107 ms                                                 | 106 ms: 1.01x faster                                                            |
| logging_simple          | 5.66 us                                                | 5.62 us: 1.01x faster                                                           |
| xml_etree_generate      | 87.0 ms                                                | 86.3 ms: 1.01x faster                                                           |
| json_loads              | 27.0 us                                                | 26.8 us: 1.01x faster                                                           |
| sympy_integrate         | 19.9 ms                                                | 19.8 ms: 1.00x faster                                                           |
| python_startup          | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                           |
| pyflate                 | 460 ms                                                 | 462 ms: 1.00x slower                                                            |
| bpe_tokeniser           | 4.69 sec                                               | 4.71 sec: 1.01x slower                                                          |
| python_startup_no_site  | 6.99 ms                                                | 7.02 ms: 1.01x slower                                                           |
| regex_dna               | 220 ms                                                 | 221 ms: 1.01x slower                                                            |
| tomli_loads             | 2.11 sec                                               | 2.13 sec: 1.01x slower                                                          |
| nqueens                 | 80.6 ms                                                | 81.4 ms: 1.01x slower                                                           |
| pidigits                | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| async_generators        | 433 ms                                                 | 438 ms: 1.01x slower                                                            |
| docutils                | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                          |
| sqlglot_transpile       | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                           |
| crypto_pyaes            | 73.0 ms                                                | 74.1 ms: 1.02x slower                                                           |
| coverage                | 83.7 ms                                                | 85.0 ms: 1.02x slower                                                           |
| dulwich_log             | 63.0 ms                                                | 64.2 ms: 1.02x slower                                                           |
| gc_traversal            | 3.81 ms                                                | 3.89 ms: 1.02x slower                                                           |
| pickle_list             | 5.01 us                                                | 5.11 us: 1.02x slower                                                           |
| sqlglot_parse           | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                           |
| comprehensions          | 16.4 us                                                | 16.8 us: 1.02x slower                                                           |
| pickle                  | 11.6 us                                                | 11.9 us: 1.03x slower                                                           |
| xml_etree_iterparse     | 102 ms                                                 | 105 ms: 1.03x slower                                                            |
| bench_thread_pool       | 815 us                                                 | 838 us: 1.03x slower                                                            |
| mako                    | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                           |
| genshi_xml              | 50.3 ms                                                | 51.9 ms: 1.03x slower                                                           |
| scimark_sor             | 122 ms                                                 | 127 ms: 1.04x slower                                                            |
| raytrace                | 262 ms                                                 | 271 ms: 1.04x slower                                                            |
| coroutines              | 22.5 ms                                                | 23.4 ms: 1.04x slower                                                           |
| unpickle_pure_python    | 213 us                                                 | 222 us: 1.04x slower                                                            |
| hexiom                  | 6.13 ms                                                | 6.38 ms: 1.04x slower                                                           |
| pickle_pure_python      | 300 us                                                 | 313 us: 1.04x slower                                                            |
| chaos                   | 58.4 ms                                                | 61.0 ms: 1.04x slower                                                           |
| deltablue               | 3.15 ms                                                | 3.31 ms: 1.05x slower                                                           |
| scimark_monte_carlo     | 66.3 ms                                                | 69.7 ms: 1.05x slower                                                           |
| pickle_dict             | 33.2 us                                                | 35.0 us: 1.05x slower                                                           |
| logging_silent          | 102 ns                                                 | 109 ns: 1.07x slower                                                            |
| json_dumps              | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                           |
| fannkuch                | 381 ms                                                 | 411 ms: 1.08x slower                                                            |
| unpickle_list           | 4.96 us                                                | 5.43 us: 1.09x slower                                                           |
| nbody                   | 85.7 ms                                                | 94.2 ms: 1.10x slower                                                           |
| create_gc_cycles        | 1.61 ms                                                | 1.78 ms: 1.11x slower                                                           |
| unpack_sequence         | 42.4 ns                                                | 47.4 ns: 1.12x slower                                                           |
| bench_mp_pool           | 24.0 ms                                                | 56.2 ms: 2.34x slower                                                           |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (12): scimark_fft, float, asyncio_tcp_ssl, asyncio_websockets, unpickle, sqlite_synth, logging_format, typing_runtime_protocols, genshi_text, scimark_lu, xml_etree_parse, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 67.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x