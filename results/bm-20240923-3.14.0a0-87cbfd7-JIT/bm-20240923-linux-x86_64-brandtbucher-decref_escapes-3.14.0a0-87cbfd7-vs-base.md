# Results vs. base

- fork: brandtbucher
- ref: decref_escapes
- machine: linux-x86_64
- commit hash: 87cbfd7
- commit date: 2024-09-23
- overall geometric mean: 1.00x slower
- HPT reliability: 90.43%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 278 ms: 1.00x slower                                                  |
| html5lib       | 64.5 ms                                                               | 62.7 ms: 1.03x faster                                                 |
| tornado_http   | 94.6 ms                                                               | 94.9 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines       | 22.9 ms                                                               | 22.6 ms: 1.01x faster                                                 |
| asyncio_tcp      | 498 ms                                                                | 494 ms: 1.01x faster                                                  |
| async_generators | 461 ms                                                                | 457 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl  | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (9): async_tree_memoization, async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                  |
| float          | 70.0 ms                                                               | 70.6 ms: 1.01x slower                                                 |
| nbody          | 80.2 ms                                                               | 81.4 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.80 ms                                                               | 3.61 ms: 1.05x faster                                                 |
| regex_v8       | 24.7 ms                                                               | 24.1 ms: 1.02x faster                                                 |
| regex_dna      | 216 ms                                                                | 215 ms: 1.00x faster                                                  |
| regex_compile  | 141 ms                                                                | 142 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_dict         | 34.5 us                                                               | 33.2 us: 1.04x faster                                                 |
| pickle_list         | 5.17 us                                                               | 5.04 us: 1.03x faster                                                 |
| xml_etree_process   | 55.6 ms                                                               | 55.0 ms: 1.01x faster                                                 |
| pickle              | 11.6 us                                                               | 11.4 us: 1.01x faster                                                 |
| pickle_pure_python  | 305 us                                                                | 308 us: 1.01x slower                                                  |
| tomli_loads         | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                                |
| xml_etree_iterparse | 97.9 ms                                                               | 99.3 ms: 1.01x slower                                                 |
| unpickle            | 14.6 us                                                               | 14.9 us: 1.02x slower                                                 |
| unpickle_list       | 5.17 us                                                               | 5.31 us: 1.03x slower                                                 |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (5): xml_etree_generate, json_dumps, unpickle_pure_python, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 25.4 ms                                                               | 24.9 ms: 1.02x faster                                                 |
| mako            | 9.88 ms                                                               | 9.77 ms: 1.01x faster                                                 |
| django_template | 35.3 ms                                                               | 36.4 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                      | 2.66 sec                                                              | 2.52 sec: 1.05x faster                                                |
| regex_effbot             | 3.80 ms                                                               | 3.61 ms: 1.05x faster                                                 |
| pprint_pformat           | 1.60 sec                                                              | 1.53 sec: 1.04x faster                                                |
| pickle_dict              | 34.5 us                                                               | 33.2 us: 1.04x faster                                                 |
| pprint_safe_repr         | 748 ms                                                                | 726 ms: 1.03x faster                                                  |
| html5lib                 | 64.5 ms                                                               | 62.7 ms: 1.03x faster                                                 |
| pickle_list              | 5.17 us                                                               | 5.04 us: 1.03x faster                                                 |
| typing_runtime_protocols | 166 us                                                                | 162 us: 1.03x faster                                                  |
| regex_v8                 | 24.7 ms                                                               | 24.1 ms: 1.02x faster                                                 |
| deepcopy_reduce          | 2.68 us                                                               | 2.62 us: 1.02x faster                                                 |
| genshi_text              | 25.4 ms                                                               | 24.9 ms: 1.02x faster                                                 |
| xml_etree_process        | 55.6 ms                                                               | 55.0 ms: 1.01x faster                                                 |
| pickle                   | 11.6 us                                                               | 11.4 us: 1.01x faster                                                 |
| logging_simple           | 5.75 us                                                               | 5.69 us: 1.01x faster                                                 |
| pyflate                  | 448 ms                                                                | 443 ms: 1.01x faster                                                  |
| mako                     | 9.88 ms                                                               | 9.77 ms: 1.01x faster                                                 |
| coroutines               | 22.9 ms                                                               | 22.6 ms: 1.01x faster                                                 |
| coverage                 | 85.2 ms                                                               | 84.4 ms: 1.01x faster                                                 |
| gc_traversal             | 3.94 ms                                                               | 3.91 ms: 1.01x faster                                                 |
| asyncio_tcp              | 498 ms                                                                | 494 ms: 1.01x faster                                                  |
| meteor_contest           | 107 ms                                                                | 106 ms: 1.01x faster                                                  |
| async_generators         | 461 ms                                                                | 457 ms: 1.01x faster                                                  |
| deepcopy_memo            | 27.2 us                                                               | 27.0 us: 1.01x faster                                                 |
| logging_silent           | 104 ns                                                                | 103 ns: 1.01x faster                                                  |
| sqlite_synth             | 2.74 us                                                               | 2.73 us: 1.01x faster                                                 |
| sympy_sum                | 173 ms                                                                | 172 ms: 1.01x faster                                                  |
| sympy_integrate          | 22.8 ms                                                               | 22.7 ms: 1.00x faster                                                 |
| regex_dna                | 216 ms                                                                | 215 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                 |
| unpack_sequence          | 112 ns                                                                | 112 ns: 1.00x slower                                                  |
| tornado_http             | 94.6 ms                                                               | 94.9 ms: 1.00x slower                                                 |
| pidigits                 | 185 ms                                                                | 186 ms: 1.00x slower                                                  |
| 2to3                     | 276 ms                                                                | 278 ms: 1.00x slower                                                  |
| regex_compile            | 141 ms                                                                | 142 ms: 1.01x slower                                                  |
| bpe_tokeniser            | 4.44 sec                                                              | 4.47 sec: 1.01x slower                                                |
| pickle_pure_python       | 305 us                                                                | 308 us: 1.01x slower                                                  |
| sqlglot_transpile        | 1.69 ms                                                               | 1.71 ms: 1.01x slower                                                 |
| nqueens                  | 85.5 ms                                                               | 86.1 ms: 1.01x slower                                                 |
| comprehensions           | 16.6 us                                                               | 16.8 us: 1.01x slower                                                 |
| float                    | 70.0 ms                                                               | 70.6 ms: 1.01x slower                                                 |
| pathlib                  | 15.9 ms                                                               | 16.1 ms: 1.01x slower                                                 |
| deepcopy                 | 258 us                                                                | 260 us: 1.01x slower                                                  |
| dulwich_log              | 67.8 ms                                                               | 68.5 ms: 1.01x slower                                                 |
| tomli_loads              | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                                |
| create_gc_cycles         | 1.74 ms                                                               | 1.76 ms: 1.01x slower                                                 |
| xml_etree_iterparse      | 97.9 ms                                                               | 99.3 ms: 1.01x slower                                                 |
| fannkuch                 | 375 ms                                                                | 380 ms: 1.01x slower                                                  |
| scimark_sor              | 117 ms                                                                | 119 ms: 1.01x slower                                                  |
| nbody                    | 80.2 ms                                                               | 81.4 ms: 1.01x slower                                                 |
| go                       | 131 ms                                                                | 133 ms: 1.02x slower                                                  |
| pycparser                | 1.15 sec                                                              | 1.17 sec: 1.02x slower                                                |
| scimark_lu               | 110 ms                                                                | 112 ms: 1.02x slower                                                  |
| json                     | 4.94 ms                                                               | 5.04 ms: 1.02x slower                                                 |
| hexiom                   | 6.86 ms                                                               | 7.00 ms: 1.02x slower                                                 |
| deltablue                | 3.21 ms                                                               | 3.27 ms: 1.02x slower                                                 |
| unpickle                 | 14.6 us                                                               | 14.9 us: 1.02x slower                                                 |
| scimark_fft              | 308 ms                                                                | 315 ms: 1.02x slower                                                  |
| chaos                    | 58.0 ms                                                               | 59.4 ms: 1.02x slower                                                 |
| scimark_sparse_mat_mult  | 4.21 ms                                                               | 4.32 ms: 1.03x slower                                                 |
| unpickle_list            | 5.17 us                                                               | 5.31 us: 1.03x slower                                                 |
| crypto_pyaes             | 65.8 ms                                                               | 67.6 ms: 1.03x slower                                                 |
| django_template          | 35.3 ms                                                               | 36.4 ms: 1.03x slower                                                 |
| richards_super           | 45.6 ms                                                               | 47.2 ms: 1.04x slower                                                 |
| spectral_norm            | 98.4 ms                                                               | 103 ms: 1.05x slower                                                  |
| richards                 | 39.9 ms                                                               | 42.7 ms: 1.07x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (31): async_tree_memoization, async_tree_none, raytrace, xml_etree_generate, thrift, async_tree_none_tg, json_dumps, pylint, async_tree_cpu_io_mixed, async_tree_memoization_tg, sympy_expand, sympy_str, genshi_xml, asyncio_websockets, python_startup_no_site, bench_mp_pool, bench_thread_pool, sqlglot_optimize, unpickle_pure_python, sqlglot_parse, telco, docutils, scimark_monte_carlo, sqlglot_normalize, json_loads, generators, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, logging_format, xml_etree_parse

# HPT report

- Reliability score: 90.43% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x