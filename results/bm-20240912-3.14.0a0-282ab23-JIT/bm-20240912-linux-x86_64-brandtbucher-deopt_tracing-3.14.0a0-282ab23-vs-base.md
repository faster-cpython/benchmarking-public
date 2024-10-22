# Results vs. base

- fork: brandtbucher
- ref: deopt_tracing
- machine: linux-x86_64
- commit hash: 282ab23
- commit date: 2024-09-12
- overall geometric mean: 1.00x faster
- HPT reliability: 98.65%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 275 ms: 1.01x faster                                                 |
| docutils       | 2.96 sec                                                              | 2.94 sec: 1.01x faster                                               |
| html5lib       | 64.5 ms                                                               | 63.3 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_generators | 461 ms                                                                | 458 ms: 1.01x faster                                                 |
| coroutines       | 22.9 ms                                                               | 22.7 ms: 1.01x faster                                                |
| asyncio_tcp      | 498 ms                                                                | 496 ms: 1.00x faster                                                 |
| Geometric mean   | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (10): async_tree_memoization, async_tree_none, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.80 ms                                                               | 3.75 ms: 1.01x faster                                                |
| regex_compile  | 141 ms                                                                | 140 ms: 1.01x faster                                                 |
| regex_v8       | 24.7 ms                                                               | 25.1 ms: 1.02x slower                                                |
| regex_dna      | 216 ms                                                                | 224 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_process    | 55.6 ms                                                               | 54.2 ms: 1.03x faster                                                |
| pickle_dict          | 34.5 us                                                               | 33.8 us: 1.02x faster                                                |
| xml_etree_generate   | 78.7 ms                                                               | 77.2 ms: 1.02x faster                                                |
| pickle_pure_python   | 305 us                                                                | 303 us: 1.01x faster                                                 |
| pickle_list          | 5.17 us                                                               | 5.14 us: 1.01x faster                                                |
| pickle               | 11.6 us                                                               | 11.5 us: 1.01x faster                                                |
| unpickle_pure_python | 216 us                                                                | 215 us: 1.00x faster                                                 |
| unpickle_list        | 5.17 us                                                               | 5.19 us: 1.00x slower                                                |
| xml_etree_iterparse  | 97.9 ms                                                               | 98.8 ms: 1.01x slower                                                |
| xml_etree_parse      | 145 ms                                                                | 146 ms: 1.01x slower                                                 |
| tomli_loads          | 1.93 sec                                                              | 1.97 sec: 1.02x slower                                               |
| json_loads           | 26.7 us                                                               | 27.3 us: 1.02x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (2): unpickle, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                |
| python_startup_no_site | 7.07 ms                                                               | 7.07 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 9.88 ms                                                               | 9.84 ms: 1.00x faster                                                |
| django_template | 35.3 ms                                                               | 36.0 ms: 1.02x slower                                                |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mdp                      | 2.66 sec                                                              | 2.53 sec: 1.05x faster                                               |
| unpack_sequence          | 112 ns                                                                | 108 ns: 1.04x faster                                                 |
| gc_traversal             | 3.94 ms                                                               | 3.83 ms: 1.03x faster                                                |
| logging_simple           | 5.75 us                                                               | 5.60 us: 1.03x faster                                                |
| xml_etree_process        | 55.6 ms                                                               | 54.2 ms: 1.03x faster                                                |
| pprint_pformat           | 1.60 sec                                                              | 1.56 sec: 1.02x faster                                               |
| pprint_safe_repr         | 748 ms                                                                | 730 ms: 1.02x faster                                                 |
| typing_runtime_protocols | 166 us                                                                | 162 us: 1.02x faster                                                 |
| nqueens                  | 85.5 ms                                                               | 83.5 ms: 1.02x faster                                                |
| pickle_dict              | 34.5 us                                                               | 33.8 us: 1.02x faster                                                |
| telco                    | 8.05 ms                                                               | 7.89 ms: 1.02x faster                                                |
| html5lib                 | 64.5 ms                                                               | 63.3 ms: 1.02x faster                                                |
| xml_etree_generate       | 78.7 ms                                                               | 77.2 ms: 1.02x faster                                                |
| coverage                 | 85.2 ms                                                               | 83.8 ms: 1.02x faster                                                |
| deepcopy_memo            | 27.2 us                                                               | 26.8 us: 1.02x faster                                                |
| thrift                   | 790 us                                                                | 778 us: 1.02x faster                                                 |
| regex_effbot             | 3.80 ms                                                               | 3.75 ms: 1.01x faster                                                |
| sympy_expand             | 506 ms                                                                | 500 ms: 1.01x faster                                                 |
| raytrace                 | 281 ms                                                                | 277 ms: 1.01x faster                                                 |
| sympy_str                | 299 ms                                                                | 296 ms: 1.01x faster                                                 |
| sympy_sum                | 173 ms                                                                | 171 ms: 1.01x faster                                                 |
| scimark_monte_carlo      | 63.0 ms                                                               | 62.3 ms: 1.01x faster                                                |
| fannkuch                 | 375 ms                                                                | 371 ms: 1.01x faster                                                 |
| meteor_contest           | 107 ms                                                                | 106 ms: 1.01x faster                                                 |
| sqlglot_parse            | 1.35 ms                                                               | 1.34 ms: 1.01x faster                                                |
| regex_compile            | 141 ms                                                                | 140 ms: 1.01x faster                                                 |
| pickle_pure_python       | 305 us                                                                | 303 us: 1.01x faster                                                 |
| sympy_integrate          | 22.8 ms                                                               | 22.7 ms: 1.01x faster                                                |
| docutils                 | 2.96 sec                                                              | 2.94 sec: 1.01x faster                                               |
| pickle_list              | 5.17 us                                                               | 5.14 us: 1.01x faster                                                |
| sqlglot_optimize         | 58.2 ms                                                               | 57.8 ms: 1.01x faster                                                |
| sqlglot_transpile        | 1.69 ms                                                               | 1.68 ms: 1.01x faster                                                |
| pickle                   | 11.6 us                                                               | 11.5 us: 1.01x faster                                                |
| async_generators         | 461 ms                                                                | 458 ms: 1.01x faster                                                 |
| coroutines               | 22.9 ms                                                               | 22.7 ms: 1.01x faster                                                |
| 2to3                     | 276 ms                                                                | 275 ms: 1.01x faster                                                 |
| deltablue                | 3.21 ms                                                               | 3.19 ms: 1.01x faster                                                |
| comprehensions           | 16.6 us                                                               | 16.6 us: 1.00x faster                                                |
| bench_thread_pool        | 839 us                                                                | 835 us: 1.00x faster                                                 |
| mako                     | 9.88 ms                                                               | 9.84 ms: 1.00x faster                                                |
| unpickle_pure_python     | 216 us                                                                | 215 us: 1.00x faster                                                 |
| asyncio_tcp              | 498 ms                                                                | 496 ms: 1.00x faster                                                 |
| logging_silent           | 104 ns                                                                | 104 ns: 1.00x faster                                                 |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                |
| python_startup_no_site   | 7.07 ms                                                               | 7.07 ms: 1.00x slower                                                |
| unpickle_list            | 5.17 us                                                               | 5.19 us: 1.00x slower                                                |
| chaos                    | 58.0 ms                                                               | 58.4 ms: 1.01x slower                                                |
| pyflate                  | 448 ms                                                                | 451 ms: 1.01x slower                                                 |
| scimark_fft              | 308 ms                                                                | 310 ms: 1.01x slower                                                 |
| scimark_lu               | 110 ms                                                                | 111 ms: 1.01x slower                                                 |
| generators               | 32.8 ms                                                               | 33.1 ms: 1.01x slower                                                |
| xml_etree_iterparse      | 97.9 ms                                                               | 98.8 ms: 1.01x slower                                                |
| sqlite_synth             | 2.74 us                                                               | 2.77 us: 1.01x slower                                                |
| xml_etree_parse          | 145 ms                                                                | 146 ms: 1.01x slower                                                 |
| sqlglot_normalize        | 113 ms                                                                | 115 ms: 1.01x slower                                                 |
| go                       | 131 ms                                                                | 132 ms: 1.01x slower                                                 |
| create_gc_cycles         | 1.74 ms                                                               | 1.76 ms: 1.01x slower                                                |
| pathlib                  | 15.9 ms                                                               | 16.1 ms: 1.01x slower                                                |
| regex_v8                 | 24.7 ms                                                               | 25.1 ms: 1.02x slower                                                |
| crypto_pyaes             | 65.8 ms                                                               | 67.0 ms: 1.02x slower                                                |
| django_template          | 35.3 ms                                                               | 36.0 ms: 1.02x slower                                                |
| tomli_loads              | 1.93 sec                                                              | 1.97 sec: 1.02x slower                                               |
| spectral_norm            | 98.4 ms                                                               | 100 ms: 1.02x slower                                                 |
| json_loads               | 26.7 us                                                               | 27.3 us: 1.02x slower                                                |
| json                     | 4.94 ms                                                               | 5.12 ms: 1.04x slower                                                |
| scimark_sparse_mat_mult  | 4.21 ms                                                               | 4.36 ms: 1.04x slower                                                |
| regex_dna                | 216 ms                                                                | 224 ms: 1.04x slower                                                 |
| pycparser                | 1.15 sec                                                              | 1.20 sec: 1.04x slower                                               |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (29): async_tree_memoization, async_tree_none, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io_tg, deepcopy_reduce, genshi_text, pylint, async_tree_cpu_io_mixed_tg, genshi_xml, logging_format, dulwich_log, asyncio_websockets, scimark_sor, unpickle, pidigits, float, nbody, bench_mp_pool, asyncio_tcp_ssl, tornado_http, richards, bpe_tokeniser, hexiom, richards_super, deepcopy, json_dumps

# HPT report

- Reliability score: 98.65% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x