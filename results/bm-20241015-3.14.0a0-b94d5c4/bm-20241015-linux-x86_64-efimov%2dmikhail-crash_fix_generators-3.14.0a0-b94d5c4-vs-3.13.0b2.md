# Results vs. 3.13.0b2

- fork: efimov-mikhail
- ref: crash_fix_generators
- machine: linux-x86_64
- commit hash: b94d5c4
- commit date: 2024-10-15
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 253 ms: 1.08x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.62 sec: 1.08x faster                                                          |
| html5lib       | 67.2 ms                                                    | 61.1 ms: 1.10x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 90.6 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                            |
| float          | 78.9 ms                                                    | 78.0 ms: 1.01x faster                                                           |
| nbody          | 88.3 ms                                                    | 89.4 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 129 ms: 1.06x faster                                                            |
| regex_effbot   | 3.67 ms                                                    | 3.49 ms: 1.05x faster                                                           |
| regex_dna      | 221 ms                                                     | 212 ms: 1.04x faster                                                            |
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                      | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 26.8 us: 1.08x faster                                                           |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.04x faster                                                            |
| unpickle_list        | 5.34 us                                                    | 5.16 us: 1.04x faster                                                           |
| unpickle             | 15.1 us                                                    | 14.7 us: 1.03x faster                                                           |
| xml_etree_process    | 61.2 ms                                                    | 59.3 ms: 1.03x faster                                                           |
| xml_etree_generate   | 87.4 ms                                                    | 85.5 ms: 1.02x faster                                                           |
| tomli_loads          | 2.12 sec                                                   | 2.10 sec: 1.01x faster                                                          |
| pickle_list          | 5.11 us                                                    | 5.06 us: 1.01x faster                                                           |
| unpickle_pure_python | 218 us                                                     | 217 us: 1.01x faster                                                            |
| pickle_dict          | 34.8 us                                                    | 35.0 us: 1.01x slower                                                           |
| pickle_pure_python   | 305 us                                                     | 308 us: 1.01x slower                                                            |
| pickle               | 11.5 us                                                    | 11.9 us: 1.04x slower                                                           |
| json_dumps           | 10.7 ms                                                    | 11.2 ms: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.03 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.8 ms: 1.04x faster                                                           |
| genshi_xml      | 51.6 ms                                                    | 50.0 ms: 1.03x faster                                                           |
| django_template | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                                           |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|--------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                 | 367 us                                                     | 264 us: 1.39x faster                                                            |
| deepcopy_memo            | 39.7 us                                                    | 31.2 us: 1.27x faster                                                           |
| deepcopy_reduce          | 3.35 us                                                    | 2.70 us: 1.24x faster                                                           |
| go                       | 145 ms                                                     | 120 ms: 1.21x faster                                                            |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.70 ms: 1.12x faster                                                           |
| mdp                      | 2.79 sec                                                   | 2.49 sec: 1.12x faster                                                          |
| richards                 | 50.9 ms                                                    | 45.9 ms: 1.11x faster                                                           |
| coverage                 | 93.1 ms                                                    | 84.2 ms: 1.11x faster                                                           |
| richards_super           | 57.4 ms                                                    | 52.1 ms: 1.10x faster                                                           |
| html5lib                 | 67.2 ms                                                    | 61.1 ms: 1.10x faster                                                           |
| scimark_fft              | 392 ms                                                     | 360 ms: 1.09x faster                                                            |
| pathlib                  | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                           |
| 2to3                     | 274 ms                                                     | 253 ms: 1.08x faster                                                            |
| docutils                 | 2.83 sec                                                   | 2.62 sec: 1.08x faster                                                          |
| json_loads               | 28.9 us                                                    | 26.8 us: 1.08x faster                                                           |
| thrift                   | 823 us                                                     | 770 us: 1.07x faster                                                            |
| generators               | 29.6 ms                                                    | 27.8 ms: 1.07x faster                                                           |
| bpe_tokeniser            | 5.02 sec                                                   | 4.71 sec: 1.07x faster                                                          |
| regex_compile            | 137 ms                                                     | 129 ms: 1.06x faster                                                            |
| scimark_lu               | 122 ms                                                     | 115 ms: 1.06x faster                                                            |
| pyflate                  | 484 ms                                                     | 457 ms: 1.06x faster                                                            |
| asyncio_tcp              | 508 ms                                                     | 480 ms: 1.06x faster                                                            |
| crypto_pyaes             | 77.5 ms                                                    | 73.2 ms: 1.06x faster                                                           |
| sympy_sum                | 156 ms                                                     | 148 ms: 1.06x faster                                                            |
| telco                    | 8.41 ms                                                    | 7.98 ms: 1.05x faster                                                           |
| pprint_safe_repr         | 758 ms                                                     | 720 ms: 1.05x faster                                                            |
| sympy_str                | 282 ms                                                     | 268 ms: 1.05x faster                                                            |
| regex_effbot             | 3.67 ms                                                    | 3.49 ms: 1.05x faster                                                           |
| pprint_pformat           | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                                          |
| sqlglot_optimize         | 55.5 ms                                                    | 53.1 ms: 1.05x faster                                                           |
| sqlglot_normalize        | 110 ms                                                     | 105 ms: 1.05x faster                                                            |
| tornado_http             | 94.6 ms                                                    | 90.6 ms: 1.05x faster                                                           |
| regex_dna                | 221 ms                                                     | 212 ms: 1.04x faster                                                            |
| sqlite_synth             | 2.99 us                                                    | 2.87 us: 1.04x faster                                                           |
| meteor_contest           | 110 ms                                                     | 105 ms: 1.04x faster                                                            |
| xml_etree_parse          | 162 ms                                                     | 156 ms: 1.04x faster                                                            |
| dulwich_log              | 67.2 ms                                                    | 64.7 ms: 1.04x faster                                                           |
| genshi_text              | 23.7 ms                                                    | 22.8 ms: 1.04x faster                                                           |
| xml_etree_iterparse      | 107 ms                                                     | 104 ms: 1.04x faster                                                            |
| unpickle_list            | 5.34 us                                                    | 5.16 us: 1.04x faster                                                           |
| json                     | 5.31 ms                                                    | 5.12 ms: 1.04x faster                                                           |
| logging_simple           | 5.74 us                                                    | 5.55 us: 1.04x faster                                                           |
| logging_format           | 6.47 us                                                    | 6.25 us: 1.04x faster                                                           |
| sympy_integrate          | 20.5 ms                                                    | 19.8 ms: 1.03x faster                                                           |
| genshi_xml               | 51.6 ms                                                    | 50.0 ms: 1.03x faster                                                           |
| unpickle                 | 15.1 us                                                    | 14.7 us: 1.03x faster                                                           |
| sympy_expand             | 473 ms                                                     | 458 ms: 1.03x faster                                                            |
| xml_etree_process        | 61.2 ms                                                    | 59.3 ms: 1.03x faster                                                           |
| regex_v8                 | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                           |
| django_template          | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                          |
| asyncio_websockets       | 567 ms                                                     | 553 ms: 1.02x faster                                                            |
| typing_runtime_protocols | 165 us                                                     | 161 us: 1.02x faster                                                            |
| xml_etree_generate       | 87.4 ms                                                    | 85.5 ms: 1.02x faster                                                           |
| sqlglot_transpile        | 1.63 ms                                                    | 1.60 ms: 1.02x faster                                                           |
| scimark_monte_carlo      | 69.2 ms                                                    | 67.8 ms: 1.02x faster                                                           |
| pidigits                 | 191 ms                                                     | 187 ms: 1.02x faster                                                            |
| python_startup           | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| sqlglot_parse            | 1.32 ms                                                    | 1.30 ms: 1.02x faster                                                           |
| create_gc_cycles         | 1.82 ms                                                    | 1.79 ms: 1.01x faster                                                           |
| nqueens                  | 81.4 ms                                                    | 80.5 ms: 1.01x faster                                                           |
| float                    | 78.9 ms                                                    | 78.0 ms: 1.01x faster                                                           |
| python_startup_no_site   | 7.11 ms                                                    | 7.03 ms: 1.01x faster                                                           |
| tomli_loads              | 2.12 sec                                                   | 2.10 sec: 1.01x faster                                                          |
| pickle_list              | 5.11 us                                                    | 5.06 us: 1.01x faster                                                           |
| logging_silent           | 105 ns                                                     | 104 ns: 1.01x faster                                                            |
| chaos                    | 61.3 ms                                                    | 60.9 ms: 1.01x faster                                                           |
| unpickle_pure_python     | 218 us                                                     | 217 us: 1.01x faster                                                            |
| async_generators         | 442 ms                                                     | 440 ms: 1.00x faster                                                            |
| scimark_sor              | 127 ms                                                     | 127 ms: 1.00x faster                                                            |
| hexiom                   | 6.30 ms                                                    | 6.31 ms: 1.00x slower                                                           |
| bench_thread_pool        | 834 us                                                     | 837 us: 1.00x slower                                                            |
| raytrace                 | 267 ms                                                     | 268 ms: 1.00x slower                                                            |
| deltablue                | 3.25 ms                                                    | 3.27 ms: 1.01x slower                                                           |
| pickle_dict              | 34.8 us                                                    | 35.0 us: 1.01x slower                                                           |
| comprehensions           | 16.6 us                                                    | 16.7 us: 1.01x slower                                                           |
| spectral_norm            | 116 ms                                                     | 117 ms: 1.01x slower                                                            |
| pickle_pure_python       | 305 us                                                     | 308 us: 1.01x slower                                                            |
| gc_traversal             | 3.98 ms                                                    | 4.02 ms: 1.01x slower                                                           |
| nbody                    | 88.3 ms                                                    | 89.4 ms: 1.01x slower                                                           |
| coroutines               | 23.2 ms                                                    | 24.0 ms: 1.04x slower                                                           |
| pickle                   | 11.5 us                                                    | 11.9 us: 1.04x slower                                                           |
| json_dumps               | 10.7 ms                                                    | 11.2 ms: 1.04x slower                                                           |
| bench_mp_pool            | 23.9 ms                                                    | 56.0 ms: 2.34x slower                                                           |
| Geometric mean           | (ref)                                                      | 1.03x faster                                                                    |

Benchmark hidden because not significant (4): fannkuch, pylint, mako, pycparser
Ignored benchmarks (15) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241015-3.14.0a0-b94d5c4/bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x