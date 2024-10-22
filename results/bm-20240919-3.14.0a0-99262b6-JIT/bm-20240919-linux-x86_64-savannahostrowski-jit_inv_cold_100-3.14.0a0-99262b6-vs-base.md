# Results vs. base

- fork: savannahostrowski
- ref: jit_inv_cold_100
- machine: linux-x86_64
- commit hash: 99262b6
- commit date: 2024-09-19
- overall geometric mean: 1.02x slower
- HPT reliability: 99.86%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 318 ms: 1.15x slower                                                         |
| docutils       | 2.96 sec                                                              | 2.70 sec: 1.10x faster                                                       |
| html5lib       | 65.1 ms                                                               | 63.2 ms: 1.03x faster                                                        |
| tornado_http   | 94.4 ms                                                               | 110 ms: 1.16x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines       | 23.6 ms                                                               | 23.3 ms: 1.01x faster                                                        |
| async_generators | 451 ms                                                                | 454 ms: 1.01x slower                                                         |
| asyncio_tcp_ssl  | 1.81 sec                                                              | 1.82 sec: 1.01x slower                                                       |
| asyncio_tcp      | 497 ms                                                                | 504 ms: 1.01x slower                                                         |
| async_tree_io    | 856 ms                                                                | 892 ms: 1.04x slower                                                         |
| Geometric mean   | (ref)                                                                 | 1.01x slower                                                                 |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 69.9 ms                                                               | 71.3 ms: 1.02x slower                                                        |
| nbody          | 79.7 ms                                                               | 85.5 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 142 ms                                                                | 130 ms: 1.09x faster                                                         |
| regex_effbot   | 3.82 ms                                                               | 3.62 ms: 1.06x faster                                                        |
| regex_dna      | 224 ms                                                                | 215 ms: 1.04x faster                                                         |
| regex_v8       | 24.6 ms                                                               | 26.4 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_list        | 5.40 us                                                               | 5.26 us: 1.03x faster                                                        |
| unpickle             | 14.8 us                                                               | 14.5 us: 1.02x faster                                                        |
| json_dumps           | 10.1 ms                                                               | 10.2 ms: 1.01x slower                                                        |
| xml_etree_iterparse  | 98.2 ms                                                               | 99.7 ms: 1.02x slower                                                        |
| pickle_list          | 5.09 us                                                               | 5.17 us: 1.02x slower                                                        |
| unpickle_pure_python | 215 us                                                                | 220 us: 1.02x slower                                                         |
| pickle               | 11.4 us                                                               | 11.8 us: 1.03x slower                                                        |
| pickle_dict          | 34.1 us                                                               | 35.4 us: 1.04x slower                                                        |
| pickle_pure_python   | 307 us                                                                | 331 us: 1.08x slower                                                         |
| tomli_loads          | 1.95 sec                                                              | 2.11 sec: 1.08x slower                                                       |
| xml_etree_process    | 54.1 ms                                                               | 59.3 ms: 1.10x slower                                                        |
| xml_etree_generate   | 77.8 ms                                                               | 85.6 ms: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                                 |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                        |
| python_startup_no_site | 7.09 ms                                                               | 7.05 ms: 1.01x faster                                                        |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 25.5 ms                                                               | 24.3 ms: 1.05x faster                                                        |
| genshi_xml      | 59.6 ms                                                               | 57.8 ms: 1.03x faster                                                        |
| django_template | 36.1 ms                                                               | 38.4 ms: 1.06x slower                                                        |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| sympy_sum                | 172 ms                                                                | 157 ms: 1.10x faster                                                         |
| docutils                 | 2.96 sec                                                              | 2.70 sec: 1.10x faster                                                       |
| regex_compile            | 142 ms                                                                | 130 ms: 1.09x faster                                                         |
| sympy_expand             | 503 ms                                                                | 470 ms: 1.07x faster                                                         |
| go                       | 130 ms                                                                | 122 ms: 1.07x faster                                                         |
| regex_effbot             | 3.82 ms                                                               | 3.62 ms: 1.06x faster                                                        |
| sympy_str                | 299 ms                                                                | 284 ms: 1.05x faster                                                         |
| pprint_pformat           | 1.57 sec                                                              | 1.49 sec: 1.05x faster                                                       |
| genshi_text              | 25.5 ms                                                               | 24.3 ms: 1.05x faster                                                        |
| regex_dna                | 224 ms                                                                | 215 ms: 1.04x faster                                                         |
| genshi_xml               | 59.6 ms                                                               | 57.8 ms: 1.03x faster                                                        |
| html5lib                 | 65.1 ms                                                               | 63.2 ms: 1.03x faster                                                        |
| pprint_safe_repr         | 753 ms                                                                | 732 ms: 1.03x faster                                                         |
| unpickle_list            | 5.40 us                                                               | 5.26 us: 1.03x faster                                                        |
| unpack_sequence          | 112 ns                                                                | 110 ns: 1.02x faster                                                         |
| sqlglot_parse            | 1.34 ms                                                               | 1.32 ms: 1.02x faster                                                        |
| unpickle                 | 14.8 us                                                               | 14.5 us: 1.02x faster                                                        |
| json                     | 5.02 ms                                                               | 4.94 ms: 1.02x faster                                                        |
| logging_silent           | 104 ns                                                                | 102 ns: 1.02x faster                                                         |
| create_gc_cycles         | 1.76 ms                                                               | 1.74 ms: 1.01x faster                                                        |
| comprehensions           | 16.7 us                                                               | 16.5 us: 1.01x faster                                                        |
| coroutines               | 23.6 ms                                                               | 23.3 ms: 1.01x faster                                                        |
| hexiom                   | 6.88 ms                                                               | 6.81 ms: 1.01x faster                                                        |
| deepcopy_reduce          | 2.67 us                                                               | 2.64 us: 1.01x faster                                                        |
| python_startup           | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                        |
| python_startup_no_site   | 7.09 ms                                                               | 7.05 ms: 1.01x faster                                                        |
| pathlib                  | 16.2 ms                                                               | 16.3 ms: 1.01x slower                                                        |
| async_generators         | 451 ms                                                                | 454 ms: 1.01x slower                                                         |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.82 sec: 1.01x slower                                                       |
| telco                    | 8.01 ms                                                               | 8.08 ms: 1.01x slower                                                        |
| thrift                   | 781 us                                                                | 788 us: 1.01x slower                                                         |
| json_dumps               | 10.1 ms                                                               | 10.2 ms: 1.01x slower                                                        |
| asyncio_tcp              | 497 ms                                                                | 504 ms: 1.01x slower                                                         |
| mdp                      | 2.66 sec                                                              | 2.70 sec: 1.01x slower                                                       |
| gc_traversal             | 3.90 ms                                                               | 3.96 ms: 1.01x slower                                                        |
| xml_etree_iterparse      | 98.2 ms                                                               | 99.7 ms: 1.02x slower                                                        |
| scimark_sor              | 116 ms                                                                | 118 ms: 1.02x slower                                                         |
| pickle_list              | 5.09 us                                                               | 5.17 us: 1.02x slower                                                        |
| typing_runtime_protocols | 164 us                                                                | 167 us: 1.02x slower                                                         |
| deepcopy_memo            | 27.0 us                                                               | 27.5 us: 1.02x slower                                                        |
| pycparser                | 1.16 sec                                                              | 1.18 sec: 1.02x slower                                                       |
| scimark_sparse_mat_mult  | 4.39 ms                                                               | 4.47 ms: 1.02x slower                                                        |
| crypto_pyaes             | 66.2 ms                                                               | 67.5 ms: 1.02x slower                                                        |
| float                    | 69.9 ms                                                               | 71.3 ms: 1.02x slower                                                        |
| dulwich_log              | 67.6 ms                                                               | 69.2 ms: 1.02x slower                                                        |
| unpickle_pure_python     | 215 us                                                                | 220 us: 1.02x slower                                                         |
| sqlglot_normalize        | 113 ms                                                                | 116 ms: 1.02x slower                                                         |
| logging_format           | 6.10 us                                                               | 6.25 us: 1.02x slower                                                        |
| deepcopy                 | 263 us                                                                | 270 us: 1.03x slower                                                         |
| logging_simple           | 5.57 us                                                               | 5.74 us: 1.03x slower                                                        |
| pickle                   | 11.4 us                                                               | 11.8 us: 1.03x slower                                                        |
| scimark_lu               | 109 ms                                                                | 113 ms: 1.03x slower                                                         |
| sqlglot_optimize         | 58.0 ms                                                               | 60.1 ms: 1.04x slower                                                        |
| pickle_dict              | 34.1 us                                                               | 35.4 us: 1.04x slower                                                        |
| scimark_monte_carlo      | 63.5 ms                                                               | 65.9 ms: 1.04x slower                                                        |
| pyflate                  | 448 ms                                                                | 466 ms: 1.04x slower                                                         |
| async_tree_io            | 856 ms                                                                | 892 ms: 1.04x slower                                                         |
| nqueens                  | 83.9 ms                                                               | 87.5 ms: 1.04x slower                                                        |
| fannkuch                 | 373 ms                                                                | 389 ms: 1.04x slower                                                         |
| meteor_contest           | 106 ms                                                                | 113 ms: 1.06x slower                                                         |
| django_template          | 36.1 ms                                                               | 38.4 ms: 1.06x slower                                                        |
| chaos                    | 58.8 ms                                                               | 62.5 ms: 1.06x slower                                                        |
| spectral_norm            | 102 ms                                                                | 110 ms: 1.07x slower                                                         |
| regex_v8                 | 24.6 ms                                                               | 26.4 ms: 1.07x slower                                                        |
| nbody                    | 79.7 ms                                                               | 85.5 ms: 1.07x slower                                                        |
| pickle_pure_python       | 307 us                                                                | 331 us: 1.08x slower                                                         |
| sqlglot_transpile        | 1.69 ms                                                               | 1.83 ms: 1.08x slower                                                        |
| tomli_loads              | 1.95 sec                                                              | 2.11 sec: 1.08x slower                                                       |
| bpe_tokeniser            | 4.45 sec                                                              | 4.86 sec: 1.09x slower                                                       |
| xml_etree_process        | 54.1 ms                                                               | 59.3 ms: 1.10x slower                                                        |
| xml_etree_generate       | 77.8 ms                                                               | 85.6 ms: 1.10x slower                                                        |
| bench_thread_pool        | 837 us                                                                | 928 us: 1.11x slower                                                         |
| deltablue                | 3.21 ms                                                               | 3.58 ms: 1.12x slower                                                        |
| generators               | 32.7 ms                                                               | 36.8 ms: 1.12x slower                                                        |
| 2to3                     | 276 ms                                                                | 318 ms: 1.15x slower                                                         |
| tornado_http             | 94.4 ms                                                               | 110 ms: 1.16x slower                                                         |
| richards_super           | 45.7 ms                                                               | 53.2 ms: 1.16x slower                                                        |
| scimark_fft              | 312 ms                                                                | 366 ms: 1.17x slower                                                         |
| richards                 | 39.7 ms                                                               | 48.2 ms: 1.22x slower                                                        |
| sympy_integrate          | 22.8 ms                                                               | 28.0 ms: 1.23x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.02x slower                                                                 |

Benchmark hidden because not significant (17): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_websockets, coverage, raytrace, async_tree_none_tg, json_loads, sqlite_synth, pidigits, xml_etree_parse, bench_mp_pool, async_tree_io_tg, async_tree_memoization_tg, mako, async_tree_memoization, pylint, async_tree_none

# HPT report

- Reliability score: 99.86% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.96x