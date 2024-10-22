# Results vs. base

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: linux-x86_64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.02x slower
- HPT reliability: 56.90%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json | results/bm-20240912-3.14.0a0-6e06e01-JIT/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                                                          | 276 ms: 1.09x slower                                                                                                |
| docutils       | 2.66 sec                                                                                                        | 2.96 sec: 1.11x slower                                                                                              |
| html5lib       | 62.4 ms                                                                                                         | 64.5 ms: 1.03x slower                                                                                               |
| tornado_http   | 89.9 ms                                                                                                         | 94.6 ms: 1.05x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.07x slower                                                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json | results/bm-20240912-3.14.0a0-6e06e01-JIT/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json |
|--------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| coroutines         | 23.2 ms                                                                                                         | 22.9 ms: 1.02x faster                                                                                               |
| asyncio_websockets | 559 ms                                                                                                          | 555 ms: 1.01x faster                                                                                                |
| asyncio_tcp_ssl    | 1.78 sec                                                                                                        | 1.81 sec: 1.02x slower                                                                                              |
| async_generators   | 437 ms                                                                                                          | 461 ms: 1.05x slower                                                                                                |
| asyncio_tcp        | 471 ms                                                                                                          | 498 ms: 1.06x slower                                                                                                |
| Geometric mean     | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (8): async_tree_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json | results/bm-20240912-3.14.0a0-6e06e01-JIT/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| nbody          | 89.5 ms                                                                                                         | 80.2 ms: 1.12x faster                                                                                               |
| float          | 76.7 ms                                                                                                         | 70.0 ms: 1.10x faster                                                                                               |
| pidigits       | 187 ms                                                                                                          | 185 ms: 1.01x faster                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.07x faster                                                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json | results/bm-20240912-3.14.0a0-6e06e01-JIT/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 216 ms                                                                                                          | 216 ms: 1.00x faster                                                                                                |
| regex_v8       | 24.6 ms                                                                                                         | 24.7 ms: 1.00x slower                                                                                               |
| regex_effbot   | 3.65 ms                                                                                                         | 3.80 ms: 1.04x slower                                                                                               |
| regex_compile  | 129 ms                                                                                                          | 141 ms: 1.10x slower                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.03x slower                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json | results/bm-20240912-3.14.0a0-6e06e01-JIT/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| xml_etree_generate   | 85.4 ms                                                                                                         | 78.7 ms: 1.08x faster                                                                                               |
| xml_etree_parse      | 156 ms                                                                                                          | 145 ms: 1.07x faster                                                                                                |
| xml_etree_iterparse  | 105 ms                                                                                                          | 97.9 ms: 1.07x faster                                                                                               |
| xml_etree_process    | 59.0 ms                                                                                                         | 55.6 ms: 1.06x faster                                                                                               |
| tomli_loads          | 2.04 sec                                                                                                        | 1.93 sec: 1.06x faster                                                                                              |
| unpickle_list        | 5.36 us                                                                                                         | 5.17 us: 1.04x faster                                                                                               |
| unpickle             | 14.9 us                                                                                                         | 14.6 us: 1.03x faster                                                                                               |
| json_dumps           | 10.3 ms                                                                                                         | 10.1 ms: 1.02x faster                                                                                               |
| json_loads           | 27.0 us                                                                                                         | 26.7 us: 1.01x faster                                                                                               |
| unpickle_pure_python | 213 us                                                                                                          | 216 us: 1.01x slower                                                                                                |
| pickle_pure_python   | 302 us                                                                                                          | 305 us: 1.01x slower                                                                                                |
| pickle               | 11.4 us                                                                                                         | 11.6 us: 1.01x slower                                                                                               |
| pickle_dict          | 33.8 us                                                                                                         | 34.5 us: 1.02x slower                                                                                               |
| pickle_list          | 4.87 us                                                                                                         | 5.17 us: 1.06x slower                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.02x faster                                                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json | results/bm-20240912-3.14.0a0-6e06e01-JIT/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                                                                         | 10.5 ms: 1.01x slower                                                                                               |
| python_startup_no_site | 6.99 ms                                                                                                         | 7.07 ms: 1.01x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json | results/bm-20240912-3.14.0a0-6e06e01-JIT/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                                                                         | 9.88 ms: 1.12x faster                                                                                               |
| django_template | 34.6 ms                                                                                                         | 35.3 ms: 1.02x slower                                                                                               |
| genshi_text     | 21.7 ms                                                                                                         | 25.4 ms: 1.17x slower                                                                                               |
| genshi_xml      | 48.6 ms                                                                                                         | 60.0 ms: 1.24x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.07x slower                                                                                                        |

All benchmarks:
===============

| Benchmark                | results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json | results/bm-20240912-3.14.0a0-6e06e01-JIT/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json |
|--------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| scimark_fft              | 363 ms                                                                                                          | 308 ms: 1.18x faster                                                                                                |
| richards                 | 45.8 ms                                                                                                         | 39.9 ms: 1.15x faster                                                                                               |
| spectral_norm            | 113 ms                                                                                                          | 98.4 ms: 1.15x faster                                                                                               |
| richards_super           | 51.7 ms                                                                                                         | 45.6 ms: 1.13x faster                                                                                               |
| mako                     | 11.1 ms                                                                                                         | 9.88 ms: 1.12x faster                                                                                               |
| nbody                    | 89.5 ms                                                                                                         | 80.2 ms: 1.12x faster                                                                                               |
| float                    | 76.7 ms                                                                                                         | 70.0 ms: 1.10x faster                                                                                               |
| bpe_tokeniser            | 4.86 sec                                                                                                        | 4.44 sec: 1.09x faster                                                                                              |
| scimark_sparse_mat_mult  | 4.60 ms                                                                                                         | 4.21 ms: 1.09x faster                                                                                               |
| deepcopy_memo            | 29.5 us                                                                                                         | 27.2 us: 1.09x faster                                                                                               |
| xml_etree_generate       | 85.4 ms                                                                                                         | 78.7 ms: 1.08x faster                                                                                               |
| crypto_pyaes             | 71.1 ms                                                                                                         | 65.8 ms: 1.08x faster                                                                                               |
| fannkuch                 | 403 ms                                                                                                          | 375 ms: 1.08x faster                                                                                                |
| xml_etree_parse          | 156 ms                                                                                                          | 145 ms: 1.07x faster                                                                                                |
| xml_etree_iterparse      | 105 ms                                                                                                          | 97.9 ms: 1.07x faster                                                                                               |
| scimark_monte_carlo      | 67.1 ms                                                                                                         | 63.0 ms: 1.07x faster                                                                                               |
| pyflate                  | 476 ms                                                                                                          | 448 ms: 1.06x faster                                                                                                |
| xml_etree_process        | 59.0 ms                                                                                                         | 55.6 ms: 1.06x faster                                                                                               |
| tomli_loads              | 2.04 sec                                                                                                        | 1.93 sec: 1.06x faster                                                                                              |
| telco                    | 8.46 ms                                                                                                         | 8.05 ms: 1.05x faster                                                                                               |
| json                     | 5.15 ms                                                                                                         | 4.94 ms: 1.04x faster                                                                                               |
| scimark_sor              | 122 ms                                                                                                          | 117 ms: 1.04x faster                                                                                                |
| unpickle_list            | 5.36 us                                                                                                         | 5.17 us: 1.04x faster                                                                                               |
| sqlite_synth             | 2.83 us                                                                                                         | 2.74 us: 1.03x faster                                                                                               |
| unpickle                 | 14.9 us                                                                                                         | 14.6 us: 1.03x faster                                                                                               |
| scimark_lu               | 113 ms                                                                                                          | 110 ms: 1.02x faster                                                                                                |
| json_dumps               | 10.3 ms                                                                                                         | 10.1 ms: 1.02x faster                                                                                               |
| coroutines               | 23.2 ms                                                                                                         | 22.9 ms: 1.02x faster                                                                                               |
| mdp                      | 2.69 sec                                                                                                        | 2.66 sec: 1.01x faster                                                                                              |
| json_loads               | 27.0 us                                                                                                         | 26.7 us: 1.01x faster                                                                                               |
| comprehensions           | 16.8 us                                                                                                         | 16.6 us: 1.01x faster                                                                                               |
| meteor_contest           | 108 ms                                                                                                          | 107 ms: 1.01x faster                                                                                                |
| pidigits                 | 187 ms                                                                                                          | 185 ms: 1.01x faster                                                                                                |
| asyncio_websockets       | 559 ms                                                                                                          | 555 ms: 1.01x faster                                                                                                |
| coverage                 | 85.7 ms                                                                                                         | 85.2 ms: 1.01x faster                                                                                               |
| chaos                    | 58.3 ms                                                                                                         | 58.0 ms: 1.00x faster                                                                                               |
| regex_dna                | 216 ms                                                                                                          | 216 ms: 1.00x faster                                                                                                |
| regex_v8                 | 24.6 ms                                                                                                         | 24.7 ms: 1.00x slower                                                                                               |
| pathlib                  | 15.9 ms                                                                                                         | 15.9 ms: 1.00x slower                                                                                               |
| create_gc_cycles         | 1.73 ms                                                                                                         | 1.74 ms: 1.01x slower                                                                                               |
| python_startup           | 10.5 ms                                                                                                         | 10.5 ms: 1.01x slower                                                                                               |
| deepcopy                 | 255 us                                                                                                          | 258 us: 1.01x slower                                                                                                |
| gc_traversal             | 3.90 ms                                                                                                         | 3.94 ms: 1.01x slower                                                                                               |
| python_startup_no_site   | 6.99 ms                                                                                                         | 7.07 ms: 1.01x slower                                                                                               |
| unpickle_pure_python     | 213 us                                                                                                          | 216 us: 1.01x slower                                                                                                |
| pickle_pure_python       | 302 us                                                                                                          | 305 us: 1.01x slower                                                                                                |
| pickle                   | 11.4 us                                                                                                         | 11.6 us: 1.01x slower                                                                                               |
| thrift                   | 779 us                                                                                                          | 790 us: 1.01x slower                                                                                                |
| asyncio_tcp_ssl          | 1.78 sec                                                                                                        | 1.81 sec: 1.02x slower                                                                                              |
| deepcopy_reduce          | 2.63 us                                                                                                         | 2.68 us: 1.02x slower                                                                                               |
| logging_format           | 6.12 us                                                                                                         | 6.24 us: 1.02x slower                                                                                               |
| deltablue                | 3.14 ms                                                                                                         | 3.21 ms: 1.02x slower                                                                                               |
| pickle_dict              | 33.8 us                                                                                                         | 34.5 us: 1.02x slower                                                                                               |
| django_template          | 34.6 ms                                                                                                         | 35.3 ms: 1.02x slower                                                                                               |
| pycparser                | 1.12 sec                                                                                                        | 1.15 sec: 1.03x slower                                                                                              |
| html5lib                 | 62.4 ms                                                                                                         | 64.5 ms: 1.03x slower                                                                                               |
| regex_effbot             | 3.65 ms                                                                                                         | 3.80 ms: 1.04x slower                                                                                               |
| logging_silent           | 99.9 ns                                                                                                         | 104 ns: 1.04x slower                                                                                                |
| logging_simple           | 5.49 us                                                                                                         | 5.75 us: 1.05x slower                                                                                               |
| pprint_safe_repr         | 714 ms                                                                                                          | 748 ms: 1.05x slower                                                                                                |
| typing_runtime_protocols | 158 us                                                                                                          | 166 us: 1.05x slower                                                                                                |
| sqlglot_normalize        | 108 ms                                                                                                          | 113 ms: 1.05x slower                                                                                                |
| dulwich_log              | 64.5 ms                                                                                                         | 67.8 ms: 1.05x slower                                                                                               |
| tornado_http             | 89.9 ms                                                                                                         | 94.6 ms: 1.05x slower                                                                                               |
| sqlglot_parse            | 1.28 ms                                                                                                         | 1.35 ms: 1.05x slower                                                                                               |
| async_generators         | 437 ms                                                                                                          | 461 ms: 1.05x slower                                                                                                |
| asyncio_tcp              | 471 ms                                                                                                          | 498 ms: 1.06x slower                                                                                                |
| pickle_list              | 4.87 us                                                                                                         | 5.17 us: 1.06x slower                                                                                               |
| nqueens                  | 80.4 ms                                                                                                         | 85.5 ms: 1.06x slower                                                                                               |
| bench_thread_pool        | 787 us                                                                                                          | 839 us: 1.07x slower                                                                                                |
| raytrace                 | 262 ms                                                                                                          | 281 ms: 1.07x slower                                                                                                |
| sqlglot_transpile        | 1.58 ms                                                                                                         | 1.69 ms: 1.07x slower                                                                                               |
| pprint_pformat           | 1.47 sec                                                                                                        | 1.60 sec: 1.09x slower                                                                                              |
| 2to3                     | 253 ms                                                                                                          | 276 ms: 1.09x slower                                                                                                |
| sqlglot_optimize         | 53.2 ms                                                                                                         | 58.2 ms: 1.09x slower                                                                                               |
| regex_compile            | 129 ms                                                                                                          | 141 ms: 1.10x slower                                                                                                |
| docutils                 | 2.66 sec                                                                                                        | 2.96 sec: 1.11x slower                                                                                              |
| sympy_expand             | 456 ms                                                                                                          | 506 ms: 1.11x slower                                                                                                |
| hexiom                   | 6.16 ms                                                                                                         | 6.86 ms: 1.11x slower                                                                                               |
| go                       | 117 ms                                                                                                          | 131 ms: 1.12x slower                                                                                                |
| sympy_str                | 267 ms                                                                                                          | 299 ms: 1.12x slower                                                                                                |
| generators               | 28.2 ms                                                                                                         | 32.8 ms: 1.16x slower                                                                                               |
| sympy_integrate          | 19.5 ms                                                                                                         | 22.8 ms: 1.17x slower                                                                                               |
| genshi_text              | 21.7 ms                                                                                                         | 25.4 ms: 1.17x slower                                                                                               |
| pylint                   | 319 ms                                                                                                          | 375 ms: 1.18x slower                                                                                                |
| sympy_sum                | 147 ms                                                                                                          | 173 ms: 1.18x slower                                                                                                |
| genshi_xml               | 48.6 ms                                                                                                         | 60.0 ms: 1.24x slower                                                                                               |
| unpack_sequence          | 46.3 ns                                                                                                         | 112 ns: 2.42x slower                                                                                                |
| Geometric mean           | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmark hidden because not significant (9): async_tree_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, bench_mp_pool, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none

# HPT report

- Reliability score: 56.90% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x