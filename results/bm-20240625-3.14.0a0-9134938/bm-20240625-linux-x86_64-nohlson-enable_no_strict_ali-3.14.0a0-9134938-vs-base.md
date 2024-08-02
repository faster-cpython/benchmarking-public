# Results vs. base

- fork: nohlson
- ref: enable_no_strict_ali
- machine: linux-x86_64
- commit hash: 9134938
- commit date: 2024-06-25
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 2.70 sec                                                              | 2.72 sec: 1.01x slower                                                 |
| html5lib       | 64.7 ms                                                               | 65.9 ms: 1.02x slower                                                  |
| tornado_http   | 90.6 ms                                                               | 90.0 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 188 ms: 1.00x slower                                                   |
| float          | 76.8 ms                                                               | 78.5 ms: 1.02x slower                                                  |
| nbody          | 85.4 ms                                                               | 92.0 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.3 ms                                                               | 25.2 ms: 1.04x faster                                                  |
| regex_dna      | 231 ms                                                                | 222 ms: 1.04x faster                                                   |
| regex_effbot   | 3.78 ms                                                               | 3.70 ms: 1.02x faster                                                  |
| regex_compile  | 130 ms                                                                | 133 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                  |
| pickle               | 11.9 us                                                               | 11.8 us: 1.01x faster                                                  |
| unpickle_pure_python | 212 us                                                                | 213 us: 1.01x slower                                                   |
| xml_etree_process    | 60.0 ms                                                               | 60.3 ms: 1.01x slower                                                  |
| xml_etree_generate   | 85.4 ms                                                               | 86.4 ms: 1.01x slower                                                  |
| pickle_pure_python   | 301 us                                                                | 305 us: 1.01x slower                                                   |
| pickle_dict          | 34.4 us                                                               | 35.3 us: 1.02x slower                                                  |
| pickle_list          | 5.07 us                                                               | 5.19 us: 1.02x slower                                                  |
| json_loads           | 27.5 us                                                               | 28.2 us: 1.03x slower                                                  |
| unpickle_list        | 5.13 us                                                               | 5.28 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_iterparse, unpickle, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.02 ms                                                               | 7.04 ms: 1.00x slower                                                  |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml     | 50.9 ms                                                               | 51.4 ms: 1.01x slower                                                  |
| genshi_text    | 22.8 ms                                                               | 23.6 ms: 1.04x slower                                                  |
| mako           | 10.9 ms                                                               | 11.4 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| scimark_sor             | 131 ms                                                                | 124 ms: 1.06x faster                                                   |
| regex_v8                | 26.3 ms                                                               | 25.2 ms: 1.04x faster                                                  |
| regex_dna               | 231 ms                                                                | 222 ms: 1.04x faster                                                   |
| regex_effbot            | 3.78 ms                                                               | 3.70 ms: 1.02x faster                                                  |
| mdp                     | 2.52 sec                                                              | 2.49 sec: 1.01x faster                                                 |
| json_dumps              | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                  |
| comprehensions          | 16.8 us                                                               | 16.6 us: 1.01x faster                                                  |
| pathlib                 | 16.0 ms                                                               | 15.8 ms: 1.01x faster                                                  |
| dulwich_log             | 64.9 ms                                                               | 64.4 ms: 1.01x faster                                                  |
| scimark_sparse_mat_mult | 5.00 ms                                                               | 4.96 ms: 1.01x faster                                                  |
| pickle                  | 11.9 us                                                               | 11.8 us: 1.01x faster                                                  |
| tornado_http            | 90.6 ms                                                               | 90.0 ms: 1.01x faster                                                  |
| chaos                   | 59.3 ms                                                               | 59.0 ms: 1.01x faster                                                  |
| asyncio_tcp             | 477 ms                                                                | 475 ms: 1.00x faster                                                   |
| nqueens                 | 79.7 ms                                                               | 79.4 ms: 1.00x faster                                                  |
| async_generators        | 430 ms                                                                | 429 ms: 1.00x faster                                                   |
| bench_thread_pool       | 787 us                                                                | 788 us: 1.00x slower                                                   |
| python_startup_no_site  | 7.02 ms                                                               | 7.04 ms: 1.00x slower                                                  |
| create_gc_cycles        | 1.73 ms                                                               | 1.74 ms: 1.00x slower                                                  |
| python_startup          | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                  |
| raytrace                | 267 ms                                                                | 268 ms: 1.00x slower                                                   |
| pidigits                | 187 ms                                                                | 188 ms: 1.00x slower                                                   |
| richards                | 47.5 ms                                                               | 47.7 ms: 1.00x slower                                                  |
| fannkuch                | 396 ms                                                                | 398 ms: 1.00x slower                                                   |
| asyncio_websockets      | 554 ms                                                                | 557 ms: 1.00x slower                                                   |
| unpickle_pure_python    | 212 us                                                                | 213 us: 1.01x slower                                                   |
| sympy_integrate         | 19.9 ms                                                               | 20.0 ms: 1.01x slower                                                  |
| xml_etree_process       | 60.0 ms                                                               | 60.3 ms: 1.01x slower                                                  |
| docutils                | 2.70 sec                                                              | 2.72 sec: 1.01x slower                                                 |
| sqlglot_parse           | 1.29 ms                                                               | 1.30 ms: 1.01x slower                                                  |
| genshi_xml              | 50.9 ms                                                               | 51.4 ms: 1.01x slower                                                  |
| sympy_sum               | 151 ms                                                                | 152 ms: 1.01x slower                                                   |
| scimark_monte_carlo     | 66.5 ms                                                               | 67.1 ms: 1.01x slower                                                  |
| sqlglot_transpile       | 1.58 ms                                                               | 1.60 ms: 1.01x slower                                                  |
| richards_super          | 53.3 ms                                                               | 53.9 ms: 1.01x slower                                                  |
| meteor_contest          | 106 ms                                                                | 107 ms: 1.01x slower                                                   |
| xml_etree_generate      | 85.4 ms                                                               | 86.4 ms: 1.01x slower                                                  |
| bpe_tokeniser           | 4.89 sec                                                              | 4.95 sec: 1.01x slower                                                 |
| telco                   | 8.23 ms                                                               | 8.33 ms: 1.01x slower                                                  |
| pickle_pure_python      | 301 us                                                                | 305 us: 1.01x slower                                                   |
| crypto_pyaes            | 72.2 ms                                                               | 73.3 ms: 1.02x slower                                                  |
| deepcopy_reduce         | 2.70 us                                                               | 2.74 us: 1.02x slower                                                  |
| coroutines              | 22.8 ms                                                               | 23.2 ms: 1.02x slower                                                  |
| html5lib                | 64.7 ms                                                               | 65.9 ms: 1.02x slower                                                  |
| deepcopy                | 261 us                                                                | 265 us: 1.02x slower                                                   |
| sqlglot_optimize        | 53.5 ms                                                               | 54.5 ms: 1.02x slower                                                  |
| json                    | 5.14 ms                                                               | 5.25 ms: 1.02x slower                                                  |
| hexiom                  | 6.13 ms                                                               | 6.26 ms: 1.02x slower                                                  |
| regex_compile           | 130 ms                                                                | 133 ms: 1.02x slower                                                   |
| float                   | 76.8 ms                                                               | 78.5 ms: 1.02x slower                                                  |
| sqlglot_normalize       | 106 ms                                                                | 109 ms: 1.02x slower                                                   |
| pickle_dict             | 34.4 us                                                               | 35.3 us: 1.02x slower                                                  |
| pickle_list             | 5.07 us                                                               | 5.19 us: 1.02x slower                                                  |
| json_loads              | 27.5 us                                                               | 28.2 us: 1.03x slower                                                  |
| unpickle_list           | 5.13 us                                                               | 5.28 us: 1.03x slower                                                  |
| deltablue               | 3.16 ms                                                               | 3.27 ms: 1.03x slower                                                  |
| pprint_safe_repr        | 735 ms                                                                | 761 ms: 1.04x slower                                                   |
| genshi_text             | 22.8 ms                                                               | 23.6 ms: 1.04x slower                                                  |
| logging_silent          | 98.4 ns                                                               | 102 ns: 1.04x slower                                                   |
| scimark_lu              | 112 ms                                                                | 116 ms: 1.04x slower                                                   |
| scimark_fft             | 360 ms                                                                | 374 ms: 1.04x slower                                                   |
| deepcopy_memo           | 29.3 us                                                               | 30.5 us: 1.04x slower                                                  |
| gc_traversal            | 3.57 ms                                                               | 3.72 ms: 1.04x slower                                                  |
| mako                    | 10.9 ms                                                               | 11.4 ms: 1.04x slower                                                  |
| pprint_pformat          | 1.49 sec                                                              | 1.56 sec: 1.04x slower                                                 |
| nbody                   | 85.4 ms                                                               | 92.0 ms: 1.08x slower                                                  |
| Geometric mean          | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (31): xml_etree_parse, xml_etree_iterparse, unpickle, sqlite_synth, typing_runtime_protocols, spectral_norm, logging_format, tomli_loads, dask, coverage, bench_mp_pool, go, pyflate, async_tree_memoization_tg, async_tree_none_tg, generators, 2to3, asyncio_tcp_ssl, logging_simple, async_tree_cpu_io_mixed_tg, sympy_str, thrift, async_tree_memoization, django_template, async_tree_none, async_tree_cpu_io_mixed, async_tree_io_tg, pylint, sympy_expand, pycparser, async_tree_io

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x