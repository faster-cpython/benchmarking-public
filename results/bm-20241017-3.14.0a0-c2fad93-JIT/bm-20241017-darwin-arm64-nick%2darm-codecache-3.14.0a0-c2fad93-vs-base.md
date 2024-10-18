# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: darwin-arm64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 181 ms                                                                | 170 ms: 1.07x faster                                           |
| docutils       | 1.57 sec                                                              | 1.50 sec: 1.05x faster                                         |
| html5lib       | 33.9 ms                                                               | 32.7 ms: 1.04x faster                                          |
| sphinx         | 666 ms                                                                | 625 ms: 1.07x faster                                           |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|---------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_eager    | 63.0 ms                                                               | 61.9 ms: 1.02x faster                                          |
| async_generators    | 290 ms                                                                | 288 ms: 1.01x faster                                           |
| async_tree_none     | 198 ms                                                                | 198 ms: 1.00x faster                                           |
| async_tree_eager_tg | 41.4 ms                                                               | 41.7 ms: 1.01x slower                                          |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (17): async_tree_eager_memoization, async_tree_memoization, async_tree_none_tg, async_tree_eager_io, async_tree_eager_cpu_io_mixed, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, coroutines, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed_tg, asyncio_tcp, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 46.4 ms                                                               | 46.2 ms: 1.00x faster                                          |
| nbody          | 63.6 ms                                                               | 63.7 ms: 1.00x slower                                          |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 76.1 ms                                                               | 72.0 ms: 1.06x faster                                          |
| regex_effbot   | 2.61 ms                                                               | 2.63 ms: 1.01x slower                                          |
| regex_v8       | 16.8 ms                                                               | 17.0 ms: 1.01x slower                                          |
| regex_dna      | 148 ms                                                                | 149 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|--------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_process  | 34.3 ms                                                               | 33.9 ms: 1.01x faster                                          |
| pickle             | 7.36 us                                                               | 7.29 us: 1.01x faster                                          |
| pickle_pure_python | 177 us                                                                | 176 us: 1.00x faster                                           |
| unpickle           | 9.03 us                                                               | 9.07 us: 1.00x slower                                          |
| unpickle_list      | 2.97 us                                                               | 3.00 us: 1.01x slower                                          |
| json_dumps         | 6.10 ms                                                               | 6.16 ms: 1.01x slower                                          |
| pickle_dict        | 18.2 us                                                               | 18.6 us: 1.02x slower                                          |
| xml_etree_parse    | 104 ms                                                                | 106 ms: 1.02x slower                                           |
| pickle_list        | 3.01 us                                                               | 3.11 us: 1.04x slower                                          |
| Geometric mean     | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (5): tomli_loads, json_loads, unpickle_pure_python, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 14.8 ms                                                               | 14.9 ms: 1.01x slower                                          |
| python_startup         | 19.1 ms                                                               | 19.2 ms: 1.01x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml      | 42.4 ms                                                               | 32.1 ms: 1.32x faster                                          |
| django_template | 23.0 ms                                                               | 20.2 ms: 1.14x faster                                          |
| genshi_text     | 16.3 ms                                                               | 14.4 ms: 1.13x faster                                          |
| mako            | 6.41 ms                                                               | 6.43 ms: 1.00x slower                                          |
| Geometric mean  | (ref)                                                                 | 1.14x faster                                                   |

All benchmarks:
===============

| Benchmark               | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml              | 42.4 ms                                                               | 32.1 ms: 1.32x faster                                          |
| richards                | 35.6 ms                                                               | 29.9 ms: 1.19x faster                                          |
| richards_super          | 39.0 ms                                                               | 33.4 ms: 1.17x faster                                          |
| go                      | 110 ms                                                                | 96.1 ms: 1.15x faster                                          |
| django_template         | 23.0 ms                                                               | 20.2 ms: 1.14x faster                                          |
| genshi_text             | 16.3 ms                                                               | 14.4 ms: 1.13x faster                                          |
| hexiom                  | 4.96 ms                                                               | 4.47 ms: 1.11x faster                                          |
| pprint_safe_repr        | 506 ms                                                                | 456 ms: 1.11x faster                                           |
| sqlglot_optimize        | 37.5 ms                                                               | 33.8 ms: 1.11x faster                                          |
| sqlglot_normalize       | 187 ms                                                                | 174 ms: 1.07x faster                                           |
| sqlglot_transpile       | 1.05 ms                                                               | 984 us: 1.07x faster                                           |
| sphinx                  | 666 ms                                                                | 625 ms: 1.07x faster                                           |
| 2to3                    | 181 ms                                                                | 170 ms: 1.07x faster                                           |
| sympy_integrate         | 12.5 ms                                                               | 11.8 ms: 1.06x faster                                          |
| raytrace                | 191 ms                                                                | 180 ms: 1.06x faster                                           |
| sqlglot_parse           | 855 us                                                                | 808 us: 1.06x faster                                           |
| pprint_pformat          | 1.01 sec                                                              | 952 ms: 1.06x faster                                           |
| regex_compile           | 76.1 ms                                                               | 72.0 ms: 1.06x faster                                          |
| sympy_str               | 150 ms                                                                | 142 ms: 1.05x faster                                           |
| sympy_sum               | 78.3 ms                                                               | 74.5 ms: 1.05x faster                                          |
| pycparser               | 682 ms                                                                | 650 ms: 1.05x faster                                           |
| docutils                | 1.57 sec                                                              | 1.50 sec: 1.05x faster                                         |
| deltablue               | 2.42 ms                                                               | 2.31 ms: 1.05x faster                                          |
| fannkuch                | 269 ms                                                                | 257 ms: 1.05x faster                                           |
| generators              | 25.2 ms                                                               | 24.2 ms: 1.04x faster                                          |
| sympy_expand            | 246 ms                                                                | 236 ms: 1.04x faster                                           |
| deepcopy                | 155 us                                                                | 149 us: 1.04x faster                                           |
| html5lib                | 33.9 ms                                                               | 32.7 ms: 1.04x faster                                          |
| chaos                   | 41.0 ms                                                               | 39.8 ms: 1.03x faster                                          |
| pyflate                 | 323 ms                                                                | 314 ms: 1.03x faster                                           |
| logging_simple          | 3.10 us                                                               | 3.02 us: 1.03x faster                                          |
| comprehensions          | 12.8 us                                                               | 12.5 us: 1.03x faster                                          |
| meteor_contest          | 76.3 ms                                                               | 74.5 ms: 1.02x faster                                          |
| logging_format          | 3.41 us                                                               | 3.33 us: 1.02x faster                                          |
| bench_mp_pool           | 62.2 ms                                                               | 61.0 ms: 1.02x faster                                          |
| async_tree_eager        | 63.0 ms                                                               | 61.9 ms: 1.02x faster                                          |
| deepcopy_reduce         | 1.51 us                                                               | 1.49 us: 1.02x faster                                          |
| xml_etree_process       | 34.3 ms                                                               | 33.9 ms: 1.01x faster                                          |
| mdp                     | 1.50 sec                                                              | 1.48 sec: 1.01x faster                                         |
| bench_thread_pool       | 480 us                                                                | 475 us: 1.01x faster                                           |
| dulwich_log             | 29.0 ms                                                               | 28.6 ms: 1.01x faster                                          |
| scimark_monte_carlo     | 45.1 ms                                                               | 44.6 ms: 1.01x faster                                          |
| nqueens                 | 57.1 ms                                                               | 56.6 ms: 1.01x faster                                          |
| pickle                  | 7.36 us                                                               | 7.29 us: 1.01x faster                                          |
| coverage                | 43.9 ms                                                               | 43.5 ms: 1.01x faster                                          |
| unpack_sequence         | 75.7 ns                                                               | 75.2 ns: 1.01x faster                                          |
| scimark_sparse_mat_mult | 2.99 ms                                                               | 2.97 ms: 1.01x faster                                          |
| bpe_tokeniser           | 3.10 sec                                                              | 3.08 sec: 1.01x faster                                         |
| deepcopy_memo           | 16.7 us                                                               | 16.6 us: 1.01x faster                                          |
| pathlib                 | 22.3 ms                                                               | 22.2 ms: 1.01x faster                                          |
| async_generators        | 290 ms                                                                | 288 ms: 1.01x faster                                           |
| scimark_fft             | 185 ms                                                                | 184 ms: 1.00x faster                                           |
| async_tree_none         | 198 ms                                                                | 198 ms: 1.00x faster                                           |
| float                   | 46.4 ms                                                               | 46.2 ms: 1.00x faster                                          |
| pickle_pure_python      | 177 us                                                                | 176 us: 1.00x faster                                           |
| scimark_lu              | 64.1 ms                                                               | 64.0 ms: 1.00x faster                                          |
| logging_silent          | 56.4 ns                                                               | 56.4 ns: 1.00x faster                                          |
| scimark_sor             | 85.8 ms                                                               | 85.8 ms: 1.00x faster                                          |
| nbody                   | 63.6 ms                                                               | 63.7 ms: 1.00x slower                                          |
| mako                    | 6.41 ms                                                               | 6.43 ms: 1.00x slower                                          |
| unpickle                | 9.03 us                                                               | 9.07 us: 1.00x slower                                          |
| crypto_pyaes            | 51.9 ms                                                               | 52.2 ms: 1.00x slower                                          |
| async_tree_eager_tg     | 41.4 ms                                                               | 41.7 ms: 1.01x slower                                          |
| thrift                  | 420 us                                                                | 423 us: 1.01x slower                                           |
| regex_effbot            | 2.61 ms                                                               | 2.63 ms: 1.01x slower                                          |
| python_startup_no_site  | 14.8 ms                                                               | 14.9 ms: 1.01x slower                                          |
| regex_v8                | 16.8 ms                                                               | 17.0 ms: 1.01x slower                                          |
| python_startup          | 19.1 ms                                                               | 19.2 ms: 1.01x slower                                          |
| regex_dna               | 148 ms                                                                | 149 ms: 1.01x slower                                           |
| unpickle_list           | 2.97 us                                                               | 3.00 us: 1.01x slower                                          |
| json_dumps              | 6.10 ms                                                               | 6.16 ms: 1.01x slower                                          |
| telco                   | 4.50 ms                                                               | 4.56 ms: 1.01x slower                                          |
| pickle_dict             | 18.2 us                                                               | 18.6 us: 1.02x slower                                          |
| xml_etree_parse         | 104 ms                                                                | 106 ms: 1.02x slower                                           |
| pickle_list             | 3.01 us                                                               | 3.11 us: 1.04x slower                                          |
| Geometric mean          | (ref)                                                                 | 1.02x faster                                                   |

Benchmark hidden because not significant (31): pylint, tornado_http, async_tree_eager_memoization, async_tree_memoization, async_tree_none_tg, async_tree_eager_io, async_tree_eager_cpu_io_mixed, async_tree_io_tg, tomli_loads, json_loads, async_tree_cpu_io_mixed, async_tree_io, json, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, spectral_norm, asyncio_websockets, sqlite_synth, coroutines, async_tree_eager_io_tg, pidigits, typing_runtime_protocols, unpickle_pure_python, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed_tg, gc_traversal, xml_etree_iterparse, create_gc_cycles, xml_etree_generate, asyncio_tcp, asyncio_tcp_ssl

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x