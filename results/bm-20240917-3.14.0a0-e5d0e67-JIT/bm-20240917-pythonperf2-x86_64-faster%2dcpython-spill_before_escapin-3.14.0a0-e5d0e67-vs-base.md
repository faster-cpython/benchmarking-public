# Results vs. base

- fork: faster-cpython
- ref: spill_before_escapin
- machine: linux-x86_64
- commit hash: e5d0e67
- commit date: 2024-09-17
- overall geometric mean: 1.00x slower
- HPT reliability: 67.16%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 309 ms                                                                      | 310 ms: 1.00x slower                                                                  |
| docutils       | 3.15 sec                                                                    | 3.17 sec: 1.01x slower                                                                |
| html5lib       | 71.1 ms                                                                     | 72.0 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|--------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io_tg   | 828 ms                                                                      | 791 ms: 1.05x faster                                                                  |
| async_generators   | 393 ms                                                                      | 386 ms: 1.02x faster                                                                  |
| asyncio_websockets | 395 ms                                                                      | 393 ms: 1.01x faster                                                                  |
| asyncio_tcp_ssl    | 1.58 sec                                                                    | 1.58 sec: 1.00x faster                                                                |
| coroutines         | 21.5 ms                                                                     | 21.6 ms: 1.00x slower                                                                 |
| Geometric mean     | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 81.8 ms                                                                     | 78.2 ms: 1.05x faster                                                                 |
| pidigits       | 250 ms                                                                      | 250 ms: 1.00x slower                                                                  |
| float          | 74.6 ms                                                                     | 76.7 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 147 ms                                                                      | 148 ms: 1.00x slower                                                                  |
| regex_effbot   | 3.49 ms                                                                     | 3.58 ms: 1.03x slower                                                                 |
| regex_dna      | 233 ms                                                                      | 252 ms: 1.09x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.03x slower                                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 220 us                                                                      | 215 us: 1.03x faster                                                                  |
| unpickle             | 15.1 us                                                                     | 14.9 us: 1.02x faster                                                                 |
| unpickle_list        | 4.72 us                                                                     | 4.66 us: 1.01x faster                                                                 |
| json_dumps           | 10.6 ms                                                                     | 10.5 ms: 1.01x faster                                                                 |
| xml_etree_parse      | 143 ms                                                                      | 142 ms: 1.01x faster                                                                  |
| xml_etree_iterparse  | 98.9 ms                                                                     | 97.8 ms: 1.01x faster                                                                 |
| xml_etree_generate   | 80.1 ms                                                                     | 80.7 ms: 1.01x slower                                                                 |
| pickle               | 10.4 us                                                                     | 10.6 us: 1.02x slower                                                                 |
| pickle_list          | 4.18 us                                                                     | 4.52 us: 1.08x slower                                                                 |
| pickle_dict          | 29.5 us                                                                     | 31.9 us: 1.08x slower                                                                 |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (4): xml_etree_process, pickle_pure_python, json_loads, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 9.00 ms                                                                     | 8.99 ms: 1.00x faster                                                                 |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|-----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml      | 66.0 ms                                                                     | 65.0 ms: 1.02x faster                                                                 |
| genshi_text     | 29.5 ms                                                                     | 29.9 ms: 1.01x slower                                                                 |
| django_template | 42.8 ms                                                                     | 43.6 ms: 1.02x slower                                                                 |
| Geometric mean  | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| gc_traversal             | 4.87 ms                                                                     | 4.36 ms: 1.12x faster                                                                 |
| richards_super           | 52.1 ms                                                                     | 49.7 ms: 1.05x faster                                                                 |
| async_tree_io_tg         | 828 ms                                                                      | 791 ms: 1.05x faster                                                                  |
| nbody                    | 81.8 ms                                                                     | 78.2 ms: 1.05x faster                                                                 |
| richards                 | 44.5 ms                                                                     | 42.8 ms: 1.04x faster                                                                 |
| telco                    | 8.28 ms                                                                     | 8.01 ms: 1.03x faster                                                                 |
| scimark_lu               | 99.3 ms                                                                     | 96.3 ms: 1.03x faster                                                                 |
| create_gc_cycles         | 1.94 ms                                                                     | 1.89 ms: 1.03x faster                                                                 |
| unpickle_pure_python     | 220 us                                                                      | 215 us: 1.03x faster                                                                  |
| async_generators         | 393 ms                                                                      | 386 ms: 1.02x faster                                                                  |
| scimark_monte_carlo      | 68.9 ms                                                                     | 67.7 ms: 1.02x faster                                                                 |
| sqlglot_optimize         | 65.7 ms                                                                     | 64.5 ms: 1.02x faster                                                                 |
| scimark_sor              | 105 ms                                                                      | 103 ms: 1.02x faster                                                                  |
| unpickle                 | 15.1 us                                                                     | 14.9 us: 1.02x faster                                                                 |
| unpack_sequence          | 89.4 ns                                                                     | 88.0 ns: 1.02x faster                                                                 |
| genshi_xml               | 66.0 ms                                                                     | 65.0 ms: 1.02x faster                                                                 |
| sympy_expand             | 533 ms                                                                      | 525 ms: 1.02x faster                                                                  |
| spectral_norm            | 81.6 ms                                                                     | 80.4 ms: 1.01x faster                                                                 |
| unpickle_list            | 4.72 us                                                                     | 4.66 us: 1.01x faster                                                                 |
| json_dumps               | 10.6 ms                                                                     | 10.5 ms: 1.01x faster                                                                 |
| pathlib                  | 16.0 ms                                                                     | 15.8 ms: 1.01x faster                                                                 |
| sqlglot_normalize        | 129 ms                                                                      | 127 ms: 1.01x faster                                                                  |
| xml_etree_parse          | 143 ms                                                                      | 142 ms: 1.01x faster                                                                  |
| xml_etree_iterparse      | 98.9 ms                                                                     | 97.8 ms: 1.01x faster                                                                 |
| scimark_fft              | 290 ms                                                                      | 288 ms: 1.01x faster                                                                  |
| generators               | 37.6 ms                                                                     | 37.3 ms: 1.01x faster                                                                 |
| crypto_pyaes             | 69.3 ms                                                                     | 68.8 ms: 1.01x faster                                                                 |
| mdp                      | 2.57 sec                                                                    | 2.55 sec: 1.01x faster                                                                |
| meteor_contest           | 131 ms                                                                      | 130 ms: 1.01x faster                                                                  |
| asyncio_websockets       | 395 ms                                                                      | 393 ms: 1.01x faster                                                                  |
| asyncio_tcp_ssl          | 1.58 sec                                                                    | 1.58 sec: 1.00x faster                                                                |
| python_startup_no_site   | 9.00 ms                                                                     | 8.99 ms: 1.00x faster                                                                 |
| pidigits                 | 250 ms                                                                      | 250 ms: 1.00x slower                                                                  |
| 2to3                     | 309 ms                                                                      | 310 ms: 1.00x slower                                                                  |
| sqlite_synth             | 2.69 us                                                                     | 2.70 us: 1.00x slower                                                                 |
| regex_compile            | 147 ms                                                                      | 148 ms: 1.00x slower                                                                  |
| sympy_integrate          | 26.6 ms                                                                     | 26.7 ms: 1.00x slower                                                                 |
| coroutines               | 21.5 ms                                                                     | 21.6 ms: 1.00x slower                                                                 |
| dulwich_log              | 64.6 ms                                                                     | 65.0 ms: 1.01x slower                                                                 |
| sympy_sum                | 169 ms                                                                      | 170 ms: 1.01x slower                                                                  |
| docutils                 | 3.15 sec                                                                    | 3.17 sec: 1.01x slower                                                                |
| xml_etree_generate       | 80.1 ms                                                                     | 80.7 ms: 1.01x slower                                                                 |
| thrift                   | 885 us                                                                      | 892 us: 1.01x slower                                                                  |
| logging_format           | 7.15 us                                                                     | 7.21 us: 1.01x slower                                                                 |
| bpe_tokeniser            | 4.75 sec                                                                    | 4.80 sec: 1.01x slower                                                                |
| chaos                    | 65.7 ms                                                                     | 66.4 ms: 1.01x slower                                                                 |
| html5lib                 | 71.1 ms                                                                     | 72.0 ms: 1.01x slower                                                                 |
| genshi_text              | 29.5 ms                                                                     | 29.9 ms: 1.01x slower                                                                 |
| go                       | 149 ms                                                                      | 151 ms: 1.01x slower                                                                  |
| pycparser                | 1.25 sec                                                                    | 1.27 sec: 1.02x slower                                                                |
| nqueens                  | 99.1 ms                                                                     | 101 ms: 1.02x slower                                                                  |
| json                     | 5.14 ms                                                                     | 5.22 ms: 1.02x slower                                                                 |
| typing_runtime_protocols | 181 us                                                                      | 184 us: 1.02x slower                                                                  |
| logging_silent           | 100 ns                                                                      | 102 ns: 1.02x slower                                                                  |
| pickle                   | 10.4 us                                                                     | 10.6 us: 1.02x slower                                                                 |
| django_template          | 42.8 ms                                                                     | 43.6 ms: 1.02x slower                                                                 |
| scimark_sparse_mat_mult  | 4.10 ms                                                                     | 4.20 ms: 1.02x slower                                                                 |
| deepcopy_reduce          | 2.92 us                                                                     | 2.99 us: 1.03x slower                                                                 |
| regex_effbot             | 3.49 ms                                                                     | 3.58 ms: 1.03x slower                                                                 |
| float                    | 74.6 ms                                                                     | 76.7 ms: 1.03x slower                                                                 |
| deepcopy                 | 289 us                                                                      | 300 us: 1.04x slower                                                                  |
| deepcopy_memo            | 27.1 us                                                                     | 28.3 us: 1.05x slower                                                                 |
| raytrace                 | 310 ms                                                                      | 328 ms: 1.06x slower                                                                  |
| pyflate                  | 449 ms                                                                      | 476 ms: 1.06x slower                                                                  |
| pickle_list              | 4.18 us                                                                     | 4.52 us: 1.08x slower                                                                 |
| pickle_dict              | 29.5 us                                                                     | 31.9 us: 1.08x slower                                                                 |
| regex_dna                | 233 ms                                                                      | 252 ms: 1.09x slower                                                                  |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (30): bench_mp_pool, deltablue, async_tree_memoization_tg, async_tree_none_tg, logging_simple, asyncio_tcp, comprehensions, xml_etree_process, pickle_pure_python, sympy_str, fannkuch, async_tree_cpu_io_mixed_tg, coverage, bench_thread_pool, json_loads, tornado_http, sqlglot_transpile, python_startup, sqlglot_parse, hexiom, mako, pprint_safe_repr, pprint_pformat, tomli_loads, async_tree_io, pylint, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, regex_v8

# HPT report

- Reliability score: 67.16% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x