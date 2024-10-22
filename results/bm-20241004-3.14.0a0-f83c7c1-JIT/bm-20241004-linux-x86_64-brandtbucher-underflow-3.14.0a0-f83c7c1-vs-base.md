# Results vs. base

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: f83c7c1
- commit date: 2024-10-04
- overall geometric mean: 1.02x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 280 ms                                                                | 291 ms: 1.04x slower                                             |
| docutils       | 2.92 sec                                                              | 3.07 sec: 1.05x slower                                           |
| html5lib       | 65.5 ms                                                               | 71.3 ms: 1.09x slower                                            |
| tornado_http   | 95.4 ms                                                               | 102 ms: 1.07x slower                                             |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| asyncio_websockets     | 555 ms                                                                | 558 ms: 1.01x slower                                             |
| asyncio_tcp_ssl        | 1.79 sec                                                              | 1.80 sec: 1.01x slower                                           |
| async_tree_memoization | 412 ms                                                                | 415 ms: 1.01x slower                                             |
| coroutines             | 23.2 ms                                                               | 23.4 ms: 1.01x slower                                            |
| asyncio_tcp            | 488 ms                                                                | 502 ms: 1.03x slower                                             |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                     |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_io, async_generators, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 72.0 ms                                                               | 71.3 ms: 1.01x faster                                            |
| pidigits       | 186 ms                                                                | 188 ms: 1.01x slower                                             |
| nbody          | 80.7 ms                                                               | 81.5 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.79 ms                                                               | 3.67 ms: 1.03x faster                                            |
| regex_dna      | 218 ms                                                                | 217 ms: 1.01x faster                                             |
| regex_v8       | 24.6 ms                                                               | 24.7 ms: 1.01x slower                                            |
| regex_compile  | 145 ms                                                                | 155 ms: 1.07x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 214 us                                                                | 202 us: 1.06x faster                                             |
| unpickle_list        | 5.44 us                                                               | 5.14 us: 1.06x faster                                            |
| unpickle             | 15.3 us                                                               | 14.6 us: 1.05x faster                                            |
| xml_etree_iterparse  | 97.8 ms                                                               | 97.4 ms: 1.00x faster                                            |
| pickle_dict          | 34.7 us                                                               | 34.8 us: 1.00x slower                                            |
| xml_etree_process    | 54.9 ms                                                               | 55.4 ms: 1.01x slower                                            |
| pickle               | 11.4 us                                                               | 11.6 us: 1.02x slower                                            |
| pickle_list          | 4.92 us                                                               | 5.07 us: 1.03x slower                                            |
| pickle_pure_python   | 306 us                                                                | 318 us: 1.04x slower                                             |
| json_loads           | 26.6 us                                                               | 28.3 us: 1.06x slower                                            |
| tomli_loads          | 1.93 sec                                                              | 2.08 sec: 1.08x slower                                           |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                     |

Benchmark hidden because not significant (3): json_dumps, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                            |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 24.7 ms                                                               | 24.3 ms: 1.02x faster                                            |
| mako            | 9.80 ms                                                               | 9.86 ms: 1.01x slower                                            |
| django_template | 36.3 ms                                                               | 41.1 ms: 1.13x slower                                            |
| genshi_xml      | 57.3 ms                                                               | 70.3 ms: 1.23x slower                                            |
| Geometric mean  | (ref)                                                                 | 1.08x slower                                                     |

All benchmarks:
===============

| Benchmark               | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python    | 214 us                                                                | 202 us: 1.06x faster                                             |
| unpickle_list           | 5.44 us                                                               | 5.14 us: 1.06x faster                                            |
| scimark_monte_carlo     | 62.9 ms                                                               | 60.0 ms: 1.05x faster                                            |
| unpickle                | 15.3 us                                                               | 14.6 us: 1.05x faster                                            |
| gc_traversal            | 3.84 ms                                                               | 3.69 ms: 1.04x faster                                            |
| unpack_sequence         | 110 ns                                                                | 106 ns: 1.04x faster                                             |
| regex_effbot            | 3.79 ms                                                               | 3.67 ms: 1.03x faster                                            |
| scimark_sparse_mat_mult | 4.55 ms                                                               | 4.44 ms: 1.02x faster                                            |
| pyflate                 | 450 ms                                                                | 440 ms: 1.02x faster                                             |
| deepcopy_memo           | 27.1 us                                                               | 26.6 us: 1.02x faster                                            |
| genshi_text             | 24.7 ms                                                               | 24.3 ms: 1.02x faster                                            |
| mdp                     | 2.56 sec                                                              | 2.52 sec: 1.01x faster                                           |
| scimark_fft             | 317 ms                                                                | 313 ms: 1.01x faster                                             |
| create_gc_cycles        | 1.74 ms                                                               | 1.72 ms: 1.01x faster                                            |
| thrift                  | 792 us                                                                | 784 us: 1.01x faster                                             |
| float                   | 72.0 ms                                                               | 71.3 ms: 1.01x faster                                            |
| spectral_norm           | 103 ms                                                                | 102 ms: 1.01x faster                                             |
| regex_dna               | 218 ms                                                                | 217 ms: 1.01x faster                                             |
| telco                   | 7.55 ms                                                               | 7.51 ms: 1.01x faster                                            |
| xml_etree_iterparse     | 97.8 ms                                                               | 97.4 ms: 1.00x faster                                            |
| python_startup          | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                            |
| pickle_dict             | 34.7 us                                                               | 34.8 us: 1.00x slower                                            |
| mako                    | 9.80 ms                                                               | 9.86 ms: 1.01x slower                                            |
| asyncio_websockets      | 555 ms                                                                | 558 ms: 1.01x slower                                             |
| regex_v8                | 24.6 ms                                                               | 24.7 ms: 1.01x slower                                            |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.80 sec: 1.01x slower                                           |
| hexiom                  | 6.93 ms                                                               | 6.97 ms: 1.01x slower                                            |
| coverage                | 85.9 ms                                                               | 86.5 ms: 1.01x slower                                            |
| async_tree_memoization  | 412 ms                                                                | 415 ms: 1.01x slower                                             |
| sqlite_synth            | 2.72 us                                                               | 2.74 us: 1.01x slower                                            |
| xml_etree_process       | 54.9 ms                                                               | 55.4 ms: 1.01x slower                                            |
| pidigits                | 186 ms                                                                | 188 ms: 1.01x slower                                             |
| nbody                   | 80.7 ms                                                               | 81.5 ms: 1.01x slower                                            |
| coroutines              | 23.2 ms                                                               | 23.4 ms: 1.01x slower                                            |
| generators              | 34.8 ms                                                               | 35.3 ms: 1.01x slower                                            |
| bench_thread_pool       | 891 us                                                                | 902 us: 1.01x slower                                             |
| scimark_lu              | 110 ms                                                                | 112 ms: 1.01x slower                                             |
| chaos                   | 59.6 ms                                                               | 60.4 ms: 1.01x slower                                            |
| pprint_pformat          | 1.54 sec                                                              | 1.56 sec: 1.01x slower                                           |
| crypto_pyaes            | 65.9 ms                                                               | 67.0 ms: 1.02x slower                                            |
| pickle                  | 11.4 us                                                               | 11.6 us: 1.02x slower                                            |
| richards_super          | 45.3 ms                                                               | 46.2 ms: 1.02x slower                                            |
| raytrace                | 276 ms                                                                | 282 ms: 1.02x slower                                             |
| fannkuch                | 372 ms                                                                | 380 ms: 1.02x slower                                             |
| scimark_sor             | 119 ms                                                                | 122 ms: 1.02x slower                                             |
| richards                | 39.7 ms                                                               | 40.6 ms: 1.02x slower                                            |
| deltablue               | 3.21 ms                                                               | 3.29 ms: 1.02x slower                                            |
| asyncio_tcp             | 488 ms                                                                | 502 ms: 1.03x slower                                             |
| pickle_list             | 4.92 us                                                               | 5.07 us: 1.03x slower                                            |
| 2to3                    | 280 ms                                                                | 291 ms: 1.04x slower                                             |
| pickle_pure_python      | 306 us                                                                | 318 us: 1.04x slower                                             |
| go                      | 131 ms                                                                | 136 ms: 1.04x slower                                             |
| sympy_str               | 308 ms                                                                | 323 ms: 1.05x slower                                             |
| sympy_expand            | 511 ms                                                                | 537 ms: 1.05x slower                                             |
| docutils                | 2.92 sec                                                              | 3.07 sec: 1.05x slower                                           |
| sqlglot_optimize        | 60.3 ms                                                               | 63.8 ms: 1.06x slower                                            |
| logging_silent          | 105 ns                                                                | 111 ns: 1.06x slower                                             |
| json_loads              | 26.6 us                                                               | 28.3 us: 1.06x slower                                            |
| dulwich_log             | 69.0 ms                                                               | 73.6 ms: 1.07x slower                                            |
| logging_format          | 6.12 us                                                               | 6.52 us: 1.07x slower                                            |
| regex_compile           | 145 ms                                                                | 155 ms: 1.07x slower                                             |
| tornado_http            | 95.4 ms                                                               | 102 ms: 1.07x slower                                             |
| sqlglot_transpile       | 1.70 ms                                                               | 1.83 ms: 1.08x slower                                            |
| tomli_loads             | 1.93 sec                                                              | 2.08 sec: 1.08x slower                                           |
| sympy_sum               | 177 ms                                                                | 191 ms: 1.08x slower                                             |
| logging_simple          | 5.54 us                                                               | 5.99 us: 1.08x slower                                            |
| sqlglot_normalize       | 116 ms                                                                | 126 ms: 1.09x slower                                             |
| html5lib                | 65.5 ms                                                               | 71.3 ms: 1.09x slower                                            |
| sympy_integrate         | 23.5 ms                                                               | 26.1 ms: 1.11x slower                                            |
| pycparser               | 1.16 sec                                                              | 1.30 sec: 1.12x slower                                           |
| django_template         | 36.3 ms                                                               | 41.1 ms: 1.13x slower                                            |
| sqlglot_parse           | 1.35 ms                                                               | 1.54 ms: 1.14x slower                                            |
| genshi_xml              | 57.3 ms                                                               | 70.3 ms: 1.23x slower                                            |
| Geometric mean          | (ref)                                                                 | 1.02x slower                                                     |

Benchmark hidden because not significant (24): async_tree_cpu_io_mixed, async_tree_io_tg, json_dumps, deepcopy, comprehensions, bpe_tokeniser, xml_etree_generate, pathlib, async_tree_io, meteor_contest, pprint_safe_repr, bench_mp_pool, python_startup_no_site, nqueens, async_generators, typing_runtime_protocols, deepcopy_reduce, json, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none, xml_etree_parse, pylint

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x