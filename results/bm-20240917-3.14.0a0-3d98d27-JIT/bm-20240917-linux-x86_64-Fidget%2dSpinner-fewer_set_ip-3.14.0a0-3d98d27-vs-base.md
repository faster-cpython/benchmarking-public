# Results vs. base

- fork: Fidget-Spinner
- ref: fewer_set_ip
- machine: linux-x86_64
- commit hash: 3d98d27
- commit date: 2024-09-17
- overall geometric mean: 1.00x faster
- HPT reliability: 59.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 273 ms                                                                | 275 ms: 1.00x slower                                                    |
| html5lib       | 64.2 ms                                                               | 65.6 ms: 1.02x slower                                                   |
| tornado_http   | 94.3 ms                                                               | 94.8 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_generators | 456 ms                                                                | 453 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl  | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                  |
| coroutines       | 22.8 ms                                                               | 23.2 ms: 1.02x slower                                                   |
| asyncio_tcp      | 487 ms                                                                | 500 ms: 1.03x slower                                                    |
| Geometric mean   | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (9): async_tree_memoization_tg, asyncio_websockets, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 69.5 ms                                                               | 69.1 ms: 1.01x faster                                                   |
| pidigits       | 185 ms                                                                | 185 ms: 1.00x faster                                                    |
| nbody          | 80.5 ms                                                               | 82.1 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 142 ms                                                                | 141 ms: 1.01x faster                                                    |
| regex_v8       | 24.5 ms                                                               | 24.5 ms: 1.00x faster                                                   |
| regex_effbot   | 3.81 ms                                                               | 4.01 ms: 1.05x slower                                                   |
| regex_dna      | 216 ms                                                                | 228 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_dict          | 34.0 us                                                               | 33.0 us: 1.03x faster                                                   |
| tomli_loads          | 1.95 sec                                                              | 1.90 sec: 1.03x faster                                                  |
| json_loads           | 27.4 us                                                               | 27.0 us: 1.02x faster                                                   |
| xml_etree_iterparse  | 99.1 ms                                                               | 97.8 ms: 1.01x faster                                                   |
| unpickle_list        | 5.21 us                                                               | 5.18 us: 1.01x faster                                                   |
| pickle_list          | 5.05 us                                                               | 5.02 us: 1.01x faster                                                   |
| unpickle_pure_python | 213 us                                                                | 214 us: 1.00x slower                                                    |
| pickle               | 11.6 us                                                               | 11.6 us: 1.01x slower                                                   |
| xml_etree_generate   | 76.9 ms                                                               | 77.5 ms: 1.01x slower                                                   |
| json_dumps           | 10.1 ms                                                               | 10.3 ms: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (4): unpickle, xml_etree_parse, pickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.01x faster                                                   |
| python_startup_no_site | 7.08 ms                                                               | 7.04 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 25.5 ms                                                               | 24.3 ms: 1.05x faster                                                   |
| genshi_xml     | 58.8 ms                                                               | 57.3 ms: 1.03x faster                                                   |
| mako           | 9.95 ms                                                               | 9.80 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 4.55 ms                                                               | 4.14 ms: 1.10x faster                                                   |
| genshi_text              | 25.5 ms                                                               | 24.3 ms: 1.05x faster                                                   |
| scimark_fft              | 314 ms                                                                | 301 ms: 1.05x faster                                                    |
| gc_traversal             | 3.90 ms                                                               | 3.74 ms: 1.04x faster                                                   |
| pickle_dict              | 34.0 us                                                               | 33.0 us: 1.03x faster                                                   |
| tomli_loads              | 1.95 sec                                                              | 1.90 sec: 1.03x faster                                                  |
| typing_runtime_protocols | 165 us                                                                | 160 us: 1.03x faster                                                    |
| genshi_xml               | 58.8 ms                                                               | 57.3 ms: 1.03x faster                                                   |
| deepcopy_reduce          | 2.69 us                                                               | 2.63 us: 1.02x faster                                                   |
| pyflate                  | 456 ms                                                                | 448 ms: 1.02x faster                                                    |
| scimark_lu               | 110 ms                                                                | 109 ms: 1.02x faster                                                    |
| logging_silent           | 103 ns                                                                | 101 ns: 1.02x faster                                                    |
| mako                     | 9.95 ms                                                               | 9.80 ms: 1.02x faster                                                   |
| json_loads               | 27.4 us                                                               | 27.0 us: 1.02x faster                                                   |
| xml_etree_iterparse      | 99.1 ms                                                               | 97.8 ms: 1.01x faster                                                   |
| crypto_pyaes             | 66.1 ms                                                               | 65.4 ms: 1.01x faster                                                   |
| mdp                      | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                  |
| scimark_monte_carlo      | 62.5 ms                                                               | 61.9 ms: 1.01x faster                                                   |
| bpe_tokeniser            | 4.47 sec                                                              | 4.43 sec: 1.01x faster                                                  |
| comprehensions           | 16.6 us                                                               | 16.5 us: 1.01x faster                                                   |
| telco                    | 7.98 ms                                                               | 7.91 ms: 1.01x faster                                                   |
| coverage                 | 85.6 ms                                                               | 85.0 ms: 1.01x faster                                                   |
| logging_simple           | 5.56 us                                                               | 5.52 us: 1.01x faster                                                   |
| richards_super           | 45.3 ms                                                               | 45.0 ms: 1.01x faster                                                   |
| async_generators         | 456 ms                                                                | 453 ms: 1.01x faster                                                    |
| sympy_str                | 297 ms                                                                | 295 ms: 1.01x faster                                                    |
| regex_compile            | 142 ms                                                                | 141 ms: 1.01x faster                                                    |
| float                    | 69.5 ms                                                               | 69.1 ms: 1.01x faster                                                   |
| create_gc_cycles         | 1.76 ms                                                               | 1.75 ms: 1.01x faster                                                   |
| unpickle_list            | 5.21 us                                                               | 5.18 us: 1.01x faster                                                   |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.01x faster                                                   |
| pickle_list              | 5.05 us                                                               | 5.02 us: 1.01x faster                                                   |
| python_startup_no_site   | 7.08 ms                                                               | 7.04 ms: 1.00x faster                                                   |
| sympy_integrate          | 22.7 ms                                                               | 22.6 ms: 1.00x faster                                                   |
| bench_thread_pool        | 838 us                                                                | 836 us: 1.00x faster                                                    |
| regex_v8                 | 24.5 ms                                                               | 24.5 ms: 1.00x faster                                                   |
| pidigits                 | 185 ms                                                                | 185 ms: 1.00x faster                                                    |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                  |
| unpickle_pure_python     | 213 us                                                                | 214 us: 1.00x slower                                                    |
| sqlglot_optimize         | 57.7 ms                                                               | 57.9 ms: 1.00x slower                                                   |
| 2to3                     | 273 ms                                                                | 275 ms: 1.00x slower                                                    |
| tornado_http             | 94.3 ms                                                               | 94.8 ms: 1.01x slower                                                   |
| pickle                   | 11.6 us                                                               | 11.6 us: 1.01x slower                                                   |
| sqlglot_normalize        | 112 ms                                                                | 113 ms: 1.01x slower                                                    |
| sqlglot_transpile        | 1.68 ms                                                               | 1.69 ms: 1.01x slower                                                   |
| sqlglot_parse            | 1.34 ms                                                               | 1.35 ms: 1.01x slower                                                   |
| xml_etree_generate       | 76.9 ms                                                               | 77.5 ms: 1.01x slower                                                   |
| chaos                    | 58.2 ms                                                               | 58.6 ms: 1.01x slower                                                   |
| raytrace                 | 275 ms                                                                | 277 ms: 1.01x slower                                                    |
| spectral_norm            | 101 ms                                                                | 102 ms: 1.01x slower                                                    |
| pprint_safe_repr         | 733 ms                                                                | 743 ms: 1.01x slower                                                    |
| pprint_pformat           | 1.54 sec                                                              | 1.57 sec: 1.01x slower                                                  |
| generators               | 32.8 ms                                                               | 33.3 ms: 1.01x slower                                                   |
| nbody                    | 80.5 ms                                                               | 82.1 ms: 1.02x slower                                                   |
| sqlite_synth             | 2.76 us                                                               | 2.81 us: 1.02x slower                                                   |
| unpack_sequence          | 111 ns                                                                | 113 ns: 1.02x slower                                                    |
| coroutines               | 22.8 ms                                                               | 23.2 ms: 1.02x slower                                                   |
| json_dumps               | 10.1 ms                                                               | 10.3 ms: 1.02x slower                                                   |
| html5lib                 | 64.2 ms                                                               | 65.6 ms: 1.02x slower                                                   |
| asyncio_tcp              | 487 ms                                                                | 500 ms: 1.03x slower                                                    |
| regex_effbot             | 3.81 ms                                                               | 4.01 ms: 1.05x slower                                                   |
| regex_dna                | 216 ms                                                                | 228 ms: 1.06x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (35): unpickle, pylint, async_tree_memoization_tg, xml_etree_parse, nqueens, django_template, logging_format, sympy_sum, deltablue, asyncio_websockets, fannkuch, pycparser, richards, sympy_expand, pickle_pure_python, bench_mp_pool, deepcopy_memo, xml_etree_process, go, meteor_contest, pathlib, docutils, hexiom, thrift, dulwich_log, scimark_sor, async_tree_none_tg, async_tree_cpu_io_mixed, json, async_tree_cpu_io_mixed_tg, deepcopy, async_tree_memoization, async_tree_none, async_tree_io_tg, async_tree_io

# HPT report

- Reliability score: 59.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x