# Results vs. base

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: eb54546
- commit date: 2024-09-12
- overall geometric mean: 1.00x faster
- HPT reliability: 99.32%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 276 ms: 1.00x faster                                                      |
| docutils       | 2.96 sec                                                              | 2.95 sec: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_generators | 461 ms                                                                | 456 ms: 1.01x faster                                                      |
| asyncio_tcp      | 498 ms                                                                | 496 ms: 1.00x faster                                                      |
| async_tree_io    | 857 ms                                                                | 887 ms: 1.04x slower                                                      |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (10): async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization_tg, coroutines, async_tree_cpu_io_mixed_tg, asyncio_websockets, asyncio_tcp_ssl, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 80.2 ms                                                               | 80.9 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 24.7 ms                                                               | 24.1 ms: 1.03x faster                                                     |
| regex_compile  | 141 ms                                                                | 140 ms: 1.01x faster                                                      |
| regex_effbot   | 3.80 ms                                                               | 3.86 ms: 1.02x slower                                                     |
| regex_dna      | 216 ms                                                                | 224 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_process   | 55.6 ms                                                               | 54.4 ms: 1.02x faster                                                     |
| xml_etree_generate  | 78.7 ms                                                               | 77.0 ms: 1.02x faster                                                     |
| pickle_dict         | 34.5 us                                                               | 33.8 us: 1.02x faster                                                     |
| pickle_list         | 5.17 us                                                               | 5.08 us: 1.02x faster                                                     |
| json_dumps          | 10.1 ms                                                               | 9.96 ms: 1.02x faster                                                     |
| pickle              | 11.6 us                                                               | 11.4 us: 1.01x faster                                                     |
| tomli_loads         | 1.93 sec                                                              | 1.91 sec: 1.01x faster                                                    |
| xml_etree_iterparse | 97.9 ms                                                               | 99.1 ms: 1.01x slower                                                     |
| json_loads          | 26.7 us                                                               | 27.1 us: 1.02x slower                                                     |
| unpickle_list       | 5.17 us                                                               | 5.34 us: 1.03x slower                                                     |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (4): unpickle, unpickle_pure_python, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                     |
| python_startup_no_site | 7.07 ms                                                               | 7.07 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 60.0 ms                                                               | 56.8 ms: 1.06x faster                                                     |
| genshi_text     | 25.4 ms                                                               | 24.3 ms: 1.05x faster                                                     |
| mako            | 9.88 ms                                                               | 9.78 ms: 1.01x faster                                                     |
| django_template | 35.3 ms                                                               | 36.0 ms: 1.02x slower                                                     |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml               | 60.0 ms                                                               | 56.8 ms: 1.06x faster                                                     |
| genshi_text              | 25.4 ms                                                               | 24.3 ms: 1.05x faster                                                     |
| gc_traversal             | 3.94 ms                                                               | 3.79 ms: 1.04x faster                                                     |
| pprint_pformat           | 1.60 sec                                                              | 1.55 sec: 1.03x faster                                                    |
| mdp                      | 2.66 sec                                                              | 2.58 sec: 1.03x faster                                                    |
| typing_runtime_protocols | 166 us                                                                | 161 us: 1.03x faster                                                      |
| logging_simple           | 5.75 us                                                               | 5.61 us: 1.03x faster                                                     |
| regex_v8                 | 24.7 ms                                                               | 24.1 ms: 1.03x faster                                                     |
| xml_etree_process        | 55.6 ms                                                               | 54.4 ms: 1.02x faster                                                     |
| xml_etree_generate       | 78.7 ms                                                               | 77.0 ms: 1.02x faster                                                     |
| logging_format           | 6.24 us                                                               | 6.12 us: 1.02x faster                                                     |
| pickle_dict              | 34.5 us                                                               | 33.8 us: 1.02x faster                                                     |
| pickle_list              | 5.17 us                                                               | 5.08 us: 1.02x faster                                                     |
| unpack_sequence          | 112 ns                                                                | 110 ns: 1.02x faster                                                      |
| json_dumps               | 10.1 ms                                                               | 9.96 ms: 1.02x faster                                                     |
| sqlglot_normalize        | 113 ms                                                                | 112 ms: 1.02x faster                                                      |
| sqlglot_transpile        | 1.69 ms                                                               | 1.67 ms: 1.02x faster                                                     |
| pickle                   | 11.6 us                                                               | 11.4 us: 1.01x faster                                                     |
| hexiom                   | 6.86 ms                                                               | 6.78 ms: 1.01x faster                                                     |
| sympy_expand             | 506 ms                                                                | 500 ms: 1.01x faster                                                      |
| scimark_sor              | 117 ms                                                                | 116 ms: 1.01x faster                                                      |
| tomli_loads              | 1.93 sec                                                              | 1.91 sec: 1.01x faster                                                    |
| sqlglot_parse            | 1.35 ms                                                               | 1.33 ms: 1.01x faster                                                     |
| logging_silent           | 104 ns                                                                | 103 ns: 1.01x faster                                                      |
| raytrace                 | 281 ms                                                                | 277 ms: 1.01x faster                                                      |
| sympy_integrate          | 22.8 ms                                                               | 22.6 ms: 1.01x faster                                                     |
| deepcopy_memo            | 27.2 us                                                               | 26.9 us: 1.01x faster                                                     |
| richards_super           | 45.6 ms                                                               | 45.1 ms: 1.01x faster                                                     |
| mako                     | 9.88 ms                                                               | 9.78 ms: 1.01x faster                                                     |
| regex_compile            | 141 ms                                                                | 140 ms: 1.01x faster                                                      |
| sympy_sum                | 173 ms                                                                | 171 ms: 1.01x faster                                                      |
| async_generators         | 461 ms                                                                | 456 ms: 1.01x faster                                                      |
| spectral_norm            | 98.4 ms                                                               | 97.4 ms: 1.01x faster                                                     |
| coverage                 | 85.2 ms                                                               | 84.4 ms: 1.01x faster                                                     |
| sympy_str                | 299 ms                                                                | 296 ms: 1.01x faster                                                      |
| bpe_tokeniser            | 4.44 sec                                                              | 4.41 sec: 1.01x faster                                                    |
| sqlglot_optimize         | 58.2 ms                                                               | 57.8 ms: 1.01x faster                                                     |
| thrift                   | 790 us                                                                | 784 us: 1.01x faster                                                      |
| pathlib                  | 15.9 ms                                                               | 15.8 ms: 1.01x faster                                                     |
| fannkuch                 | 375 ms                                                                | 373 ms: 1.00x faster                                                      |
| richards                 | 39.9 ms                                                               | 39.7 ms: 1.00x faster                                                     |
| asyncio_tcp              | 498 ms                                                                | 496 ms: 1.00x faster                                                      |
| docutils                 | 2.96 sec                                                              | 2.95 sec: 1.00x faster                                                    |
| 2to3                     | 276 ms                                                                | 276 ms: 1.00x faster                                                      |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                     |
| python_startup_no_site   | 7.07 ms                                                               | 7.07 ms: 1.00x slower                                                     |
| sqlite_synth             | 2.74 us                                                               | 2.76 us: 1.01x slower                                                     |
| crypto_pyaes             | 65.8 ms                                                               | 66.2 ms: 1.01x slower                                                     |
| go                       | 131 ms                                                                | 132 ms: 1.01x slower                                                      |
| dulwich_log              | 67.8 ms                                                               | 68.3 ms: 1.01x slower                                                     |
| nbody                    | 80.2 ms                                                               | 80.9 ms: 1.01x slower                                                     |
| create_gc_cycles         | 1.74 ms                                                               | 1.76 ms: 1.01x slower                                                     |
| scimark_fft              | 308 ms                                                                | 311 ms: 1.01x slower                                                      |
| xml_etree_iterparse      | 97.9 ms                                                               | 99.1 ms: 1.01x slower                                                     |
| chaos                    | 58.0 ms                                                               | 58.8 ms: 1.01x slower                                                     |
| regex_effbot             | 3.80 ms                                                               | 3.86 ms: 1.02x slower                                                     |
| json_loads               | 26.7 us                                                               | 27.1 us: 1.02x slower                                                     |
| django_template          | 35.3 ms                                                               | 36.0 ms: 1.02x slower                                                     |
| scimark_lu               | 110 ms                                                                | 113 ms: 1.02x slower                                                      |
| unpickle_list            | 5.17 us                                                               | 5.34 us: 1.03x slower                                                     |
| async_tree_io            | 857 ms                                                                | 887 ms: 1.04x slower                                                      |
| json                     | 4.94 ms                                                               | 5.13 ms: 1.04x slower                                                     |
| regex_dna                | 216 ms                                                                | 224 ms: 1.04x slower                                                      |
| scimark_sparse_mat_mult  | 4.21 ms                                                               | 4.49 ms: 1.07x slower                                                     |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (33): async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed, pylint, unpickle, async_tree_none_tg, async_tree_memoization_tg, nqueens, deltablue, bench_thread_pool, tornado_http, float, coroutines, async_tree_cpu_io_mixed_tg, asyncio_websockets, asyncio_tcp_ssl, pidigits, html5lib, unpickle_pure_python, pyflate, telco, bench_mp_pool, generators, pickle_pure_python, meteor_contest, pycparser, comprehensions, deepcopy_reduce, deepcopy, scimark_monte_carlo, xml_etree_parse, async_tree_io_tg, pprint_safe_repr

# HPT report

- Reliability score: 99.32% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x