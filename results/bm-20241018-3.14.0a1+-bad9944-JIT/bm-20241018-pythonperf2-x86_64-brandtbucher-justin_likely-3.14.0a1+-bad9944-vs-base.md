# Results vs. base

- fork: brandtbucher
- ref: justin_likely
- machine: linux-x86_64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.00x slower
- HPT reliability: 98.02%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 317 ms                                                                       | 314 ms: 1.01x faster                                                        |
| docutils       | 3.23 sec                                                                     | 3.21 sec: 1.01x faster                                                      |
| html5lib       | 69.6 ms                                                                      | 70.7 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (2): sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io    | 851 ms                                                                       | 836 ms: 1.02x faster                                                        |
| async_tree_none  | 336 ms                                                                       | 332 ms: 1.01x faster                                                        |
| async_tree_io_tg | 872 ms                                                                       | 863 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl  | 1.58 sec                                                                     | 1.59 sec: 1.00x slower                                                      |
| asyncio_tcp      | 374 ms                                                                       | 378 ms: 1.01x slower                                                        |
| coroutines       | 21.6 ms                                                                      | 21.8 ms: 1.01x slower                                                       |
| async_generators | 378 ms                                                                       | 388 ms: 1.03x slower                                                        |
| Geometric mean   | (ref)                                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 85.0 ms                                                                      | 83.3 ms: 1.02x faster                                                       |
| pidigits       | 252 ms                                                                       | 251 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.52 ms                                                                      | 3.51 ms: 1.00x faster                                                       |
| regex_dna      | 246 ms                                                                       | 247 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|--------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_list      | 4.82 us                                                                      | 4.67 us: 1.03x faster                                                       |
| tomli_loads        | 2.16 sec                                                                     | 2.15 sec: 1.01x faster                                                      |
| xml_etree_generate | 81.5 ms                                                                      | 82.0 ms: 1.01x slower                                                       |
| xml_etree_process  | 58.2 ms                                                                      | 58.6 ms: 1.01x slower                                                       |
| json_loads         | 24.2 us                                                                      | 24.3 us: 1.01x slower                                                       |
| pickle             | 10.5 us                                                                      | 10.7 us: 1.02x slower                                                       |
| json_dumps         | 11.0 ms                                                                      | 11.2 ms: 1.02x slower                                                       |
| pickle_dict        | 30.9 us                                                                      | 31.7 us: 1.03x slower                                                       |
| pickle_list        | 4.43 us                                                                      | 4.60 us: 1.04x slower                                                       |
| Geometric mean     | (ref)                                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_iterparse, unpickle, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.0 ms                                                                      | 14.9 ms: 1.00x faster                                                       |
| python_startup_no_site | 9.01 ms                                                                      | 8.98 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 30.1 ms                                                                      | 28.3 ms: 1.06x faster                                                       |
| genshi_xml      | 65.7 ms                                                                      | 65.1 ms: 1.01x faster                                                       |
| mako            | 9.42 ms                                                                      | 9.39 ms: 1.00x faster                                                       |
| django_template | 43.5 ms                                                                      | 43.9 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                        | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text             | 30.1 ms                                                                      | 28.3 ms: 1.06x faster                                                       |
| scimark_sor             | 109 ms                                                                       | 103 ms: 1.06x faster                                                        |
| gc_traversal            | 5.50 ms                                                                      | 5.21 ms: 1.05x faster                                                       |
| unpickle_list           | 4.82 us                                                                      | 4.67 us: 1.03x faster                                                       |
| nqueens                 | 106 ms                                                                       | 103 ms: 1.03x faster                                                        |
| pyflate                 | 476 ms                                                                       | 467 ms: 1.02x faster                                                        |
| nbody                   | 85.0 ms                                                                      | 83.3 ms: 1.02x faster                                                       |
| async_tree_io           | 851 ms                                                                       | 836 ms: 1.02x faster                                                        |
| dulwich_log             | 65.4 ms                                                                      | 64.4 ms: 1.02x faster                                                       |
| scimark_lu              | 95.2 ms                                                                      | 93.9 ms: 1.01x faster                                                       |
| richards_super          | 49.6 ms                                                                      | 48.9 ms: 1.01x faster                                                       |
| mdp                     | 2.64 sec                                                                     | 2.60 sec: 1.01x faster                                                      |
| pycparser               | 1.28 sec                                                                     | 1.27 sec: 1.01x faster                                                      |
| logging_format          | 7.22 us                                                                      | 7.14 us: 1.01x faster                                                       |
| fannkuch                | 368 ms                                                                       | 364 ms: 1.01x faster                                                        |
| async_tree_none         | 336 ms                                                                       | 332 ms: 1.01x faster                                                        |
| async_tree_io_tg        | 872 ms                                                                       | 863 ms: 1.01x faster                                                        |
| genshi_xml              | 65.7 ms                                                                      | 65.1 ms: 1.01x faster                                                       |
| 2to3                    | 317 ms                                                                       | 314 ms: 1.01x faster                                                        |
| logging_silent          | 91.5 ns                                                                      | 90.8 ns: 1.01x faster                                                       |
| crypto_pyaes            | 72.1 ms                                                                      | 71.5 ms: 1.01x faster                                                       |
| bpe_tokeniser           | 4.81 sec                                                                     | 4.77 sec: 1.01x faster                                                      |
| chaos                   | 67.5 ms                                                                      | 67.0 ms: 1.01x faster                                                       |
| meteor_contest          | 132 ms                                                                       | 131 ms: 1.01x faster                                                        |
| docutils                | 3.23 sec                                                                     | 3.21 sec: 1.01x faster                                                      |
| sympy_expand            | 537 ms                                                                       | 534 ms: 1.01x faster                                                        |
| spectral_norm           | 93.3 ms                                                                      | 92.8 ms: 1.01x faster                                                       |
| tomli_loads             | 2.16 sec                                                                     | 2.15 sec: 1.01x faster                                                      |
| sqlglot_parse           | 1.52 ms                                                                      | 1.52 ms: 1.00x faster                                                       |
| create_gc_cycles        | 2.90 ms                                                                      | 2.89 ms: 1.00x faster                                                       |
| go                      | 152 ms                                                                       | 151 ms: 1.00x faster                                                        |
| python_startup          | 15.0 ms                                                                      | 14.9 ms: 1.00x faster                                                       |
| mako                    | 9.42 ms                                                                      | 9.39 ms: 1.00x faster                                                       |
| pidigits                | 252 ms                                                                       | 251 ms: 1.00x faster                                                        |
| python_startup_no_site  | 9.01 ms                                                                      | 8.98 ms: 1.00x faster                                                       |
| regex_effbot            | 3.52 ms                                                                      | 3.51 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl         | 1.58 sec                                                                     | 1.59 sec: 1.00x slower                                                      |
| pathlib                 | 15.8 ms                                                                      | 15.9 ms: 1.00x slower                                                       |
| sympy_str               | 323 ms                                                                       | 324 ms: 1.00x slower                                                        |
| sqlglot_optimize        | 70.0 ms                                                                      | 70.3 ms: 1.00x slower                                                       |
| regex_dna               | 246 ms                                                                       | 247 ms: 1.00x slower                                                        |
| richards                | 43.5 ms                                                                      | 43.7 ms: 1.01x slower                                                       |
| xml_etree_generate      | 81.5 ms                                                                      | 82.0 ms: 1.01x slower                                                       |
| sqlglot_transpile       | 2.00 ms                                                                      | 2.01 ms: 1.01x slower                                                       |
| sqlglot_normalize       | 133 ms                                                                       | 134 ms: 1.01x slower                                                        |
| xml_etree_process       | 58.2 ms                                                                      | 58.6 ms: 1.01x slower                                                       |
| json                    | 5.06 ms                                                                      | 5.10 ms: 1.01x slower                                                       |
| json_loads              | 24.2 us                                                                      | 24.3 us: 1.01x slower                                                       |
| thrift                  | 892 us                                                                       | 899 us: 1.01x slower                                                        |
| telco                   | 7.67 ms                                                                      | 7.73 ms: 1.01x slower                                                       |
| django_template         | 43.5 ms                                                                      | 43.9 ms: 1.01x slower                                                       |
| asyncio_tcp             | 374 ms                                                                       | 378 ms: 1.01x slower                                                        |
| logging_simple          | 6.57 us                                                                      | 6.63 us: 1.01x slower                                                       |
| deepcopy                | 310 us                                                                       | 313 us: 1.01x slower                                                        |
| coroutines              | 21.6 ms                                                                      | 21.8 ms: 1.01x slower                                                       |
| unpack_sequence         | 90.4 ns                                                                      | 91.3 ns: 1.01x slower                                                       |
| raytrace                | 303 ms                                                                       | 307 ms: 1.01x slower                                                        |
| sqlite_synth            | 2.70 us                                                                      | 2.74 us: 1.01x slower                                                       |
| pprint_safe_repr        | 795 ms                                                                       | 807 ms: 1.02x slower                                                        |
| html5lib                | 69.6 ms                                                                      | 70.7 ms: 1.02x slower                                                       |
| pickle                  | 10.5 us                                                                      | 10.7 us: 1.02x slower                                                       |
| json_dumps              | 11.0 ms                                                                      | 11.2 ms: 1.02x slower                                                       |
| deepcopy_reduce         | 3.05 us                                                                      | 3.11 us: 1.02x slower                                                       |
| scimark_fft             | 284 ms                                                                       | 291 ms: 1.02x slower                                                        |
| scimark_sparse_mat_mult | 4.37 ms                                                                      | 4.47 ms: 1.02x slower                                                       |
| pickle_dict             | 30.9 us                                                                      | 31.7 us: 1.03x slower                                                       |
| async_generators        | 378 ms                                                                       | 388 ms: 1.03x slower                                                        |
| deepcopy_memo           | 29.0 us                                                                      | 29.9 us: 1.03x slower                                                       |
| pickle_list             | 4.43 us                                                                      | 4.60 us: 1.04x slower                                                       |
| Geometric mean          | (ref)                                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (29): regex_v8, async_tree_none_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, typing_runtime_protocols, async_tree_memoization_tg, async_tree_cpu_io_mixed, bench_thread_pool, deltablue, regex_compile, comprehensions, generators, async_tree_memoization, xml_etree_parse, coverage, pylint, sphinx, hexiom, scimark_monte_carlo, sympy_sum, xml_etree_iterparse, unpickle, float, sympy_integrate, pprint_pformat, tornado_http, unpickle_pure_python, pickle_pure_python, bench_mp_pool

# HPT report

- Reliability score: 98.02% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x