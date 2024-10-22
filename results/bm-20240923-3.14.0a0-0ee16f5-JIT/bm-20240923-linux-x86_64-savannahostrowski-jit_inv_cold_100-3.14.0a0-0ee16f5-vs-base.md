# Results vs. base

- fork: savannahostrowski
- ref: jit_inv_cold_100
- machine: linux-x86_64
- commit hash: 0ee16f5
- commit date: 2024-09-23
- overall geometric mean: 1.03x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 318 ms: 1.15x slower                                                         |
| docutils       | 2.96 sec                                                              | 2.72 sec: 1.09x faster                                                       |
| html5lib       | 65.1 ms                                                               | 65.4 ms: 1.01x slower                                                        |
| tornado_http   | 94.4 ms                                                               | 110 ms: 1.16x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|--------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines         | 23.6 ms                                                               | 23.2 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl    | 1.81 sec                                                              | 1.82 sec: 1.00x slower                                                       |
| asyncio_websockets | 556 ms                                                                | 560 ms: 1.01x slower                                                         |
| asyncio_tcp        | 497 ms                                                                | 505 ms: 1.02x slower                                                         |
| async_generators   | 451 ms                                                                | 460 ms: 1.02x slower                                                         |
| async_tree_io      | 856 ms                                                                | 892 ms: 1.04x slower                                                         |
| Geometric mean     | (ref)                                                                 | 1.01x slower                                                                 |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 188 ms: 1.01x slower                                                         |
| nbody          | 79.7 ms                                                               | 80.6 ms: 1.01x slower                                                        |
| float          | 69.9 ms                                                               | 70.9 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 142 ms                                                                | 132 ms: 1.08x faster                                                         |
| regex_effbot   | 3.82 ms                                                               | 3.65 ms: 1.05x faster                                                        |
| regex_dna      | 224 ms                                                                | 221 ms: 1.01x faster                                                         |
| regex_v8       | 24.6 ms                                                               | 27.3 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_list        | 5.40 us                                                               | 5.25 us: 1.03x faster                                                        |
| json_dumps           | 10.1 ms                                                               | 10.2 ms: 1.01x slower                                                        |
| pickle               | 11.4 us                                                               | 11.5 us: 1.01x slower                                                        |
| json_loads           | 26.9 us                                                               | 27.3 us: 1.02x slower                                                        |
| xml_etree_iterparse  | 98.2 ms                                                               | 100.0 ms: 1.02x slower                                                       |
| xml_etree_parse      | 146 ms                                                                | 149 ms: 1.02x slower                                                         |
| unpickle_pure_python | 215 us                                                                | 220 us: 1.02x slower                                                         |
| unpickle             | 14.8 us                                                               | 15.2 us: 1.03x slower                                                        |
| pickle_dict          | 34.1 us                                                               | 35.2 us: 1.03x slower                                                        |
| pickle_pure_python   | 307 us                                                                | 332 us: 1.08x slower                                                         |
| tomli_loads          | 1.95 sec                                                              | 2.14 sec: 1.10x slower                                                       |
| xml_etree_process    | 54.1 ms                                                               | 61.2 ms: 1.13x slower                                                        |
| xml_etree_generate   | 77.8 ms                                                               | 88.8 ms: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                                 |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.09 ms                                                               | 7.10 ms: 1.00x slower                                                        |
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                        |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 25.5 ms                                                               | 24.5 ms: 1.04x faster                                                        |
| genshi_xml      | 59.6 ms                                                               | 58.3 ms: 1.02x faster                                                        |
| django_template | 36.1 ms                                                               | 37.1 ms: 1.03x slower                                                        |
| mako            | 10.0 ms                                                               | 10.5 ms: 1.05x slower                                                        |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils                 | 2.96 sec                                                              | 2.72 sec: 1.09x faster                                                       |
| sympy_sum                | 172 ms                                                                | 159 ms: 1.09x faster                                                         |
| regex_compile            | 142 ms                                                                | 132 ms: 1.08x faster                                                         |
| go                       | 130 ms                                                                | 122 ms: 1.07x faster                                                         |
| sympy_expand             | 503 ms                                                                | 474 ms: 1.06x faster                                                         |
| regex_effbot             | 3.82 ms                                                               | 3.65 ms: 1.05x faster                                                        |
| pprint_pformat           | 1.57 sec                                                              | 1.50 sec: 1.05x faster                                                       |
| sympy_str                | 299 ms                                                                | 287 ms: 1.04x faster                                                         |
| genshi_text              | 25.5 ms                                                               | 24.5 ms: 1.04x faster                                                        |
| mdp                      | 2.66 sec                                                              | 2.57 sec: 1.04x faster                                                       |
| unpack_sequence          | 112 ns                                                                | 109 ns: 1.03x faster                                                         |
| pprint_safe_repr         | 753 ms                                                                | 732 ms: 1.03x faster                                                         |
| unpickle_list            | 5.40 us                                                               | 5.25 us: 1.03x faster                                                        |
| genshi_xml               | 59.6 ms                                                               | 58.3 ms: 1.02x faster                                                        |
| logging_silent           | 104 ns                                                                | 102 ns: 1.02x faster                                                         |
| coroutines               | 23.6 ms                                                               | 23.2 ms: 1.02x faster                                                        |
| create_gc_cycles         | 1.76 ms                                                               | 1.73 ms: 1.01x faster                                                        |
| regex_dna                | 224 ms                                                                | 221 ms: 1.01x faster                                                         |
| deepcopy_reduce          | 2.67 us                                                               | 2.64 us: 1.01x faster                                                        |
| sqlite_synth             | 2.76 us                                                               | 2.74 us: 1.01x faster                                                        |
| coverage                 | 85.2 ms                                                               | 84.6 ms: 1.01x faster                                                        |
| raytrace                 | 276 ms                                                                | 274 ms: 1.01x faster                                                         |
| hexiom                   | 6.88 ms                                                               | 6.84 ms: 1.01x faster                                                        |
| python_startup_no_site   | 7.09 ms                                                               | 7.10 ms: 1.00x slower                                                        |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                        |
| comprehensions           | 16.7 us                                                               | 16.8 us: 1.00x slower                                                        |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.82 sec: 1.00x slower                                                       |
| html5lib                 | 65.1 ms                                                               | 65.4 ms: 1.01x slower                                                        |
| asyncio_websockets       | 556 ms                                                                | 560 ms: 1.01x slower                                                         |
| gc_traversal             | 3.90 ms                                                               | 3.93 ms: 1.01x slower                                                        |
| pathlib                  | 16.2 ms                                                               | 16.3 ms: 1.01x slower                                                        |
| scimark_sor              | 116 ms                                                                | 117 ms: 1.01x slower                                                         |
| json_dumps               | 10.1 ms                                                               | 10.2 ms: 1.01x slower                                                        |
| pidigits                 | 186 ms                                                                | 188 ms: 1.01x slower                                                         |
| nbody                    | 79.7 ms                                                               | 80.6 ms: 1.01x slower                                                        |
| typing_runtime_protocols | 164 us                                                                | 166 us: 1.01x slower                                                         |
| pickle                   | 11.4 us                                                               | 11.5 us: 1.01x slower                                                        |
| scimark_sparse_mat_mult  | 4.39 ms                                                               | 4.45 ms: 1.01x slower                                                        |
| json                     | 5.02 ms                                                               | 5.09 ms: 1.01x slower                                                        |
| asyncio_tcp              | 497 ms                                                                | 505 ms: 1.02x slower                                                         |
| float                    | 69.9 ms                                                               | 70.9 ms: 1.02x slower                                                        |
| json_loads               | 26.9 us                                                               | 27.3 us: 1.02x slower                                                        |
| xml_etree_iterparse      | 98.2 ms                                                               | 100.0 ms: 1.02x slower                                                       |
| async_generators         | 451 ms                                                                | 460 ms: 1.02x slower                                                         |
| dulwich_log              | 67.6 ms                                                               | 69.1 ms: 1.02x slower                                                        |
| thrift                   | 781 us                                                                | 798 us: 1.02x slower                                                         |
| xml_etree_parse          | 146 ms                                                                | 149 ms: 1.02x slower                                                         |
| crypto_pyaes             | 66.2 ms                                                               | 67.7 ms: 1.02x slower                                                        |
| sqlglot_normalize        | 113 ms                                                                | 116 ms: 1.02x slower                                                         |
| unpickle_pure_python     | 215 us                                                                | 220 us: 1.02x slower                                                         |
| django_template          | 36.1 ms                                                               | 37.1 ms: 1.03x slower                                                        |
| logging_format           | 6.10 us                                                               | 6.27 us: 1.03x slower                                                        |
| deepcopy_memo            | 27.0 us                                                               | 27.8 us: 1.03x slower                                                        |
| scimark_monte_carlo      | 63.5 ms                                                               | 65.5 ms: 1.03x slower                                                        |
| unpickle                 | 14.8 us                                                               | 15.2 us: 1.03x slower                                                        |
| pickle_dict              | 34.1 us                                                               | 35.2 us: 1.03x slower                                                        |
| deepcopy                 | 263 us                                                                | 272 us: 1.04x slower                                                         |
| nqueens                  | 83.9 ms                                                               | 87.1 ms: 1.04x slower                                                        |
| scimark_lu               | 109 ms                                                                | 113 ms: 1.04x slower                                                         |
| logging_simple           | 5.57 us                                                               | 5.79 us: 1.04x slower                                                        |
| sqlglot_optimize         | 58.0 ms                                                               | 60.3 ms: 1.04x slower                                                        |
| async_tree_io            | 856 ms                                                                | 892 ms: 1.04x slower                                                         |
| pycparser                | 1.16 sec                                                              | 1.21 sec: 1.04x slower                                                       |
| mako                     | 10.0 ms                                                               | 10.5 ms: 1.05x slower                                                        |
| fannkuch                 | 373 ms                                                                | 390 ms: 1.05x slower                                                         |
| chaos                    | 58.8 ms                                                               | 61.6 ms: 1.05x slower                                                        |
| meteor_contest           | 106 ms                                                                | 113 ms: 1.07x slower                                                         |
| spectral_norm            | 102 ms                                                                | 110 ms: 1.07x slower                                                         |
| pickle_pure_python       | 307 us                                                                | 332 us: 1.08x slower                                                         |
| pyflate                  | 448 ms                                                                | 486 ms: 1.08x slower                                                         |
| generators               | 32.7 ms                                                               | 35.5 ms: 1.09x slower                                                        |
| sqlglot_transpile        | 1.69 ms                                                               | 1.85 ms: 1.09x slower                                                        |
| bpe_tokeniser            | 4.45 sec                                                              | 4.88 sec: 1.10x slower                                                       |
| tomli_loads              | 1.95 sec                                                              | 2.14 sec: 1.10x slower                                                       |
| regex_v8                 | 24.6 ms                                                               | 27.3 ms: 1.11x slower                                                        |
| bench_thread_pool        | 837 us                                                                | 932 us: 1.11x slower                                                         |
| deltablue                | 3.21 ms                                                               | 3.58 ms: 1.12x slower                                                        |
| xml_etree_process        | 54.1 ms                                                               | 61.2 ms: 1.13x slower                                                        |
| xml_etree_generate       | 77.8 ms                                                               | 88.8 ms: 1.14x slower                                                        |
| 2to3                     | 276 ms                                                                | 318 ms: 1.15x slower                                                         |
| richards_super           | 45.7 ms                                                               | 52.9 ms: 1.16x slower                                                        |
| tornado_http             | 94.4 ms                                                               | 110 ms: 1.16x slower                                                         |
| scimark_fft              | 312 ms                                                                | 365 ms: 1.17x slower                                                         |
| richards                 | 39.7 ms                                                               | 47.9 ms: 1.21x slower                                                        |
| sympy_integrate          | 22.8 ms                                                               | 28.1 ms: 1.23x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.03x slower                                                                 |

Benchmark hidden because not significant (12): sqlglot_parse, async_tree_cpu_io_mixed, bench_mp_pool, async_tree_cpu_io_mixed_tg, async_tree_none_tg, pickle_list, async_tree_io_tg, async_tree_memoization_tg, async_tree_none, telco, pylint, async_tree_memoization

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.96x