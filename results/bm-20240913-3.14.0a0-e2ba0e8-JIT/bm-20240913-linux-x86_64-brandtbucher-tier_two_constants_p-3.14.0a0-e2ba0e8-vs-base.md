# Results vs. base

- fork: brandtbucher
- ref: tier_two_constants_p
- machine: linux-x86_64
- commit hash: e2ba0e8
- commit date: 2024-09-13
- overall geometric mean: 1.00x slower
- HPT reliability: 92.51%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 280 ms: 1.01x slower                                                        |
| docutils       | 2.96 sec                                                              | 2.97 sec: 1.00x slower                                                      |
| html5lib       | 64.5 ms                                                               | 65.6 ms: 1.02x slower                                                       |
| tornado_http   | 94.6 ms                                                               | 95.1 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coroutines     | 22.9 ms                                                               | 23.0 ms: 1.00x slower                                                       |
| asyncio_tcp    | 498 ms                                                                | 502 ms: 1.01x slower                                                        |
| async_tree_io  | 857 ms                                                                | 888 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (10): async_tree_none_tg, async_tree_memoization_tg, async_generators, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none, asyncio_websockets, asyncio_tcp_ssl, async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 70.0 ms                                                               | 69.6 ms: 1.01x faster                                                       |
| pidigits       | 185 ms                                                                | 186 ms: 1.01x slower                                                        |
| nbody          | 80.2 ms                                                               | 81.7 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.80 ms                                                               | 3.59 ms: 1.06x faster                                                       |
| regex_dna      | 216 ms                                                                | 221 ms: 1.02x slower                                                        |
| regex_v8       | 24.7 ms                                                               | 25.4 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 55.6 ms                                                               | 54.1 ms: 1.03x faster                                                       |
| xml_etree_generate   | 78.7 ms                                                               | 76.9 ms: 1.02x faster                                                       |
| pickle_list          | 5.17 us                                                               | 5.11 us: 1.01x faster                                                       |
| pickle_pure_python   | 305 us                                                                | 303 us: 1.01x faster                                                        |
| json_dumps           | 10.1 ms                                                               | 10.1 ms: 1.01x faster                                                       |
| unpickle_pure_python | 216 us                                                                | 215 us: 1.01x faster                                                        |
| pickle_dict          | 34.5 us                                                               | 34.6 us: 1.00x slower                                                       |
| json_loads           | 26.7 us                                                               | 26.7 us: 1.00x slower                                                       |
| xml_etree_iterparse  | 97.9 ms                                                               | 98.6 ms: 1.01x slower                                                       |
| xml_etree_parse      | 145 ms                                                                | 147 ms: 1.01x slower                                                        |
| pickle               | 11.6 us                                                               | 11.8 us: 1.02x slower                                                       |
| tomli_loads          | 1.93 sec                                                              | 1.98 sec: 1.02x slower                                                      |
| unpickle_list        | 5.17 us                                                               | 5.34 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                       |
| python_startup_no_site | 7.07 ms                                                               | 7.05 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 60.0 ms                                                               | 59.0 ms: 1.02x faster                                                       |
| mako            | 9.88 ms                                                               | 9.73 ms: 1.02x faster                                                       |
| django_template | 35.3 ms                                                               | 35.8 ms: 1.01x slower                                                       |
| genshi_text     | 25.4 ms                                                               | 25.8 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal             | 3.94 ms                                                               | 3.72 ms: 1.06x faster                                                       |
| regex_effbot             | 3.80 ms                                                               | 3.59 ms: 1.06x faster                                                       |
| mdp                      | 2.66 sec                                                              | 2.53 sec: 1.05x faster                                                      |
| pprint_pformat           | 1.60 sec                                                              | 1.53 sec: 1.04x faster                                                      |
| unpack_sequence          | 112 ns                                                                | 108 ns: 1.04x faster                                                        |
| pprint_safe_repr         | 748 ms                                                                | 722 ms: 1.04x faster                                                        |
| xml_etree_process        | 55.6 ms                                                               | 54.1 ms: 1.03x faster                                                       |
| xml_etree_generate       | 78.7 ms                                                               | 76.9 ms: 1.02x faster                                                       |
| genshi_xml               | 60.0 ms                                                               | 59.0 ms: 1.02x faster                                                       |
| mako                     | 9.88 ms                                                               | 9.73 ms: 1.02x faster                                                       |
| typing_runtime_protocols | 166 us                                                                | 164 us: 1.02x faster                                                        |
| logging_simple           | 5.75 us                                                               | 5.67 us: 1.01x faster                                                       |
| pickle_list              | 5.17 us                                                               | 5.11 us: 1.01x faster                                                       |
| richards_super           | 45.6 ms                                                               | 45.1 ms: 1.01x faster                                                       |
| pickle_pure_python       | 305 us                                                                | 303 us: 1.01x faster                                                        |
| bpe_tokeniser            | 4.44 sec                                                              | 4.40 sec: 1.01x faster                                                      |
| json_dumps               | 10.1 ms                                                               | 10.1 ms: 1.01x faster                                                       |
| richards                 | 39.9 ms                                                               | 39.6 ms: 1.01x faster                                                       |
| unpickle_pure_python     | 216 us                                                                | 215 us: 1.01x faster                                                        |
| float                    | 70.0 ms                                                               | 69.6 ms: 1.01x faster                                                       |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                       |
| sqlglot_normalize        | 113 ms                                                                | 113 ms: 1.00x faster                                                        |
| python_startup_no_site   | 7.07 ms                                                               | 7.05 ms: 1.00x faster                                                       |
| pickle_dict              | 34.5 us                                                               | 34.6 us: 1.00x slower                                                       |
| json_loads               | 26.7 us                                                               | 26.7 us: 1.00x slower                                                       |
| docutils                 | 2.96 sec                                                              | 2.97 sec: 1.00x slower                                                      |
| coroutines               | 22.9 ms                                                               | 23.0 ms: 1.00x slower                                                       |
| meteor_contest           | 107 ms                                                                | 107 ms: 1.00x slower                                                        |
| go                       | 131 ms                                                                | 131 ms: 1.01x slower                                                        |
| pidigits                 | 185 ms                                                                | 186 ms: 1.01x slower                                                        |
| pathlib                  | 15.9 ms                                                               | 16.0 ms: 1.01x slower                                                       |
| tornado_http             | 94.6 ms                                                               | 95.1 ms: 1.01x slower                                                       |
| sqlglot_parse            | 1.35 ms                                                               | 1.36 ms: 1.01x slower                                                       |
| dulwich_log              | 67.8 ms                                                               | 68.3 ms: 1.01x slower                                                       |
| sqlglot_transpile        | 1.69 ms                                                               | 1.71 ms: 1.01x slower                                                       |
| xml_etree_iterparse      | 97.9 ms                                                               | 98.6 ms: 1.01x slower                                                       |
| asyncio_tcp              | 498 ms                                                                | 502 ms: 1.01x slower                                                        |
| sqlglot_optimize         | 58.2 ms                                                               | 58.7 ms: 1.01x slower                                                       |
| thrift                   | 790 us                                                                | 797 us: 1.01x slower                                                        |
| create_gc_cycles         | 1.74 ms                                                               | 1.75 ms: 1.01x slower                                                       |
| scimark_lu               | 110 ms                                                                | 111 ms: 1.01x slower                                                        |
| sympy_integrate          | 22.8 ms                                                               | 23.1 ms: 1.01x slower                                                       |
| sympy_str                | 299 ms                                                                | 302 ms: 1.01x slower                                                        |
| django_template          | 35.3 ms                                                               | 35.8 ms: 1.01x slower                                                       |
| nqueens                  | 85.5 ms                                                               | 86.5 ms: 1.01x slower                                                       |
| 2to3                     | 276 ms                                                                | 280 ms: 1.01x slower                                                        |
| spectral_norm            | 98.4 ms                                                               | 99.6 ms: 1.01x slower                                                       |
| xml_etree_parse          | 145 ms                                                                | 147 ms: 1.01x slower                                                        |
| json                     | 4.94 ms                                                               | 5.02 ms: 1.01x slower                                                       |
| pickle                   | 11.6 us                                                               | 11.8 us: 1.02x slower                                                       |
| sympy_sum                | 173 ms                                                                | 176 ms: 1.02x slower                                                        |
| genshi_text              | 25.4 ms                                                               | 25.8 ms: 1.02x slower                                                       |
| html5lib                 | 64.5 ms                                                               | 65.6 ms: 1.02x slower                                                       |
| nbody                    | 80.2 ms                                                               | 81.7 ms: 1.02x slower                                                       |
| chaos                    | 58.0 ms                                                               | 59.2 ms: 1.02x slower                                                       |
| crypto_pyaes             | 65.8 ms                                                               | 67.3 ms: 1.02x slower                                                       |
| regex_dna                | 216 ms                                                                | 221 ms: 1.02x slower                                                        |
| tomli_loads              | 1.93 sec                                                              | 1.98 sec: 1.02x slower                                                      |
| scimark_fft              | 308 ms                                                                | 316 ms: 1.03x slower                                                        |
| hexiom                   | 6.86 ms                                                               | 7.05 ms: 1.03x slower                                                       |
| regex_v8                 | 24.7 ms                                                               | 25.4 ms: 1.03x slower                                                       |
| unpickle_list            | 5.17 us                                                               | 5.34 us: 1.03x slower                                                       |
| comprehensions           | 16.6 us                                                               | 17.2 us: 1.04x slower                                                       |
| async_tree_io            | 857 ms                                                                | 888 ms: 1.04x slower                                                        |
| pycparser                | 1.15 sec                                                              | 1.21 sec: 1.05x slower                                                      |
| scimark_sparse_mat_mult  | 4.21 ms                                                               | 4.47 ms: 1.06x slower                                                       |
| deepcopy                 | 258 us                                                                | 277 us: 1.07x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (30): async_tree_none_tg, logging_format, deltablue, deepcopy_memo, async_tree_memoization_tg, pyflate, async_generators, async_tree_memoization, generators, fannkuch, async_tree_cpu_io_mixed_tg, async_tree_none, raytrace, asyncio_websockets, asyncio_tcp_ssl, logging_silent, bench_mp_pool, bench_thread_pool, sqlite_synth, pylint, coverage, regex_compile, telco, sympy_expand, async_tree_cpu_io_mixed, async_tree_io_tg, scimark_sor, scimark_monte_carlo, deepcopy_reduce, unpickle

# HPT report

- Reliability score: 92.51% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x