# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: optimizer_constant_p
- machine: linux-x86_64
- commit hash: 3330a62
- commit date: 2024-06-15
- overall geometric mean: 1.01x faster
- HPT reliability: 59.18%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 281 ms: 1.02x slower                                                            |
| docutils       | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                          |
| html5lib       | 67.2 ms                                                    | 68.1 ms: 1.01x slower                                                           |
| tornado_http   | 94.6 ms                                                    | 96.2 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                      | 1.02x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg     | 336 ms                                                     | 346 ms: 1.03x slower                                                            |
| async_tree_memoization | 463 ms                                                     | 492 ms: 1.06x slower                                                            |
| async_tree_io_tg       | 936 ms                                                     | 1.02 sec: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                      | 1.03x slower                                                                    |

Benchmark hidden because not significant (5): async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 80.4 ms: 1.10x faster                                                           |
| float          | 78.9 ms                                                    | 71.9 ms: 1.10x faster                                                           |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                      | 1.07x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 23.7 ms: 1.06x faster                                                           |
| regex_effbot   | 3.67 ms                                                    | 3.59 ms: 1.02x faster                                                           |
| regex_dna      | 221 ms                                                     | 226 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.98 sec: 1.07x faster                                                          |
| xml_etree_parse      | 162 ms                                                     | 152 ms: 1.07x faster                                                            |
| xml_etree_generate   | 87.4 ms                                                    | 82.5 ms: 1.06x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.06x faster                                                            |
| xml_etree_process    | 61.2 ms                                                    | 58.2 ms: 1.05x faster                                                           |
| pickle_pure_python   | 305 us                                                     | 295 us: 1.04x faster                                                            |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                           |
| unpickle_list        | 5.34 us                                                    | 5.25 us: 1.02x faster                                                           |
| unpickle_pure_python | 218 us                                                     | 221 us: 1.01x slower                                                            |
| pickle_list          | 5.11 us                                                    | 5.19 us: 1.02x slower                                                           |
| pickle_dict          | 34.8 us                                                    | 35.4 us: 1.02x slower                                                           |
| pickle               | 11.5 us                                                    | 12.2 us: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                                    |

Benchmark hidden because not significant (2): unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.65 ms: 1.08x slower                                                           |
| Geometric mean         | (ref)                                                      | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                           |
| genshi_text     | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                           |
| django_template | 34.8 ms                                                    | 37.0 ms: 1.06x slower                                                           |
| genshi_xml      | 51.6 ms                                                    | 58.8 ms: 1.14x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|--------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo            | 39.7 us                                                    | 28.9 us: 1.38x faster                                                           |
| deepcopy                 | 367 us                                                     | 272 us: 1.35x faster                                                            |
| scimark_fft              | 392 ms                                                     | 315 ms: 1.25x faster                                                            |
| deepcopy_reduce          | 3.35 us                                                    | 2.74 us: 1.22x faster                                                           |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.44 ms: 1.19x faster                                                           |
| richards                 | 50.9 ms                                                    | 42.9 ms: 1.19x faster                                                           |
| richards_super           | 57.4 ms                                                    | 48.8 ms: 1.18x faster                                                           |
| crypto_pyaes             | 77.5 ms                                                    | 68.2 ms: 1.14x faster                                                           |
| scimark_monte_carlo      | 69.2 ms                                                    | 61.7 ms: 1.12x faster                                                           |
| mako                     | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                           |
| spectral_norm            | 116 ms                                                     | 104 ms: 1.11x faster                                                            |
| fannkuch                 | 402 ms                                                     | 361 ms: 1.11x faster                                                            |
| pyflate                  | 484 ms                                                     | 437 ms: 1.11x faster                                                            |
| nbody                    | 88.3 ms                                                    | 80.4 ms: 1.10x faster                                                           |
| float                    | 78.9 ms                                                    | 71.9 ms: 1.10x faster                                                           |
| mdp                      | 2.79 sec                                                   | 2.58 sec: 1.08x faster                                                          |
| pprint_pformat           | 1.56 sec                                                   | 1.45 sec: 1.07x faster                                                          |
| tomli_loads              | 2.12 sec                                                   | 1.98 sec: 1.07x faster                                                          |
| pprint_safe_repr         | 758 ms                                                     | 711 ms: 1.07x faster                                                            |
| xml_etree_parse          | 162 ms                                                     | 152 ms: 1.07x faster                                                            |
| xml_etree_generate       | 87.4 ms                                                    | 82.5 ms: 1.06x faster                                                           |
| regex_v8                 | 25.1 ms                                                    | 23.7 ms: 1.06x faster                                                           |
| xml_etree_iterparse      | 107 ms                                                     | 101 ms: 1.06x faster                                                            |
| xml_etree_process        | 61.2 ms                                                    | 58.2 ms: 1.05x faster                                                           |
| pathlib                  | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                           |
| sqlite_synth             | 2.99 us                                                    | 2.86 us: 1.04x faster                                                           |
| telco                    | 8.41 ms                                                    | 8.09 ms: 1.04x faster                                                           |
| pickle_pure_python       | 305 us                                                     | 295 us: 1.04x faster                                                            |
| bpe_tokeniser            | 5.02 sec                                                   | 4.87 sec: 1.03x faster                                                          |
| meteor_contest           | 110 ms                                                     | 107 ms: 1.03x faster                                                            |
| logging_format           | 6.47 us                                                    | 6.30 us: 1.03x faster                                                           |
| json_dumps               | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                           |
| chaos                    | 61.3 ms                                                    | 59.8 ms: 1.03x faster                                                           |
| regex_effbot             | 3.67 ms                                                    | 3.59 ms: 1.02x faster                                                           |
| gc_traversal             | 3.98 ms                                                    | 3.90 ms: 1.02x faster                                                           |
| logging_simple           | 5.74 us                                                    | 5.63 us: 1.02x faster                                                           |
| unpickle_list            | 5.34 us                                                    | 5.25 us: 1.02x faster                                                           |
| pidigits                 | 191 ms                                                     | 188 ms: 1.02x faster                                                            |
| create_gc_cycles         | 1.82 ms                                                    | 1.80 ms: 1.01x faster                                                           |
| thrift                   | 823 us                                                     | 815 us: 1.01x faster                                                            |
| sqlglot_transpile        | 1.63 ms                                                    | 1.64 ms: 1.01x slower                                                           |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                                          |
| html5lib                 | 67.2 ms                                                    | 68.1 ms: 1.01x slower                                                           |
| unpickle_pure_python     | 218 us                                                     | 221 us: 1.01x slower                                                            |
| coroutines               | 23.2 ms                                                    | 23.5 ms: 1.02x slower                                                           |
| pickle_list              | 5.11 us                                                    | 5.19 us: 1.02x slower                                                           |
| tornado_http             | 94.6 ms                                                    | 96.2 ms: 1.02x slower                                                           |
| pickle_dict              | 34.8 us                                                    | 35.4 us: 1.02x slower                                                           |
| go                       | 145 ms                                                     | 147 ms: 1.02x slower                                                            |
| logging_silent           | 105 ns                                                     | 107 ns: 1.02x slower                                                            |
| regex_dna                | 221 ms                                                     | 226 ms: 1.02x slower                                                            |
| coverage                 | 93.1 ms                                                    | 95.0 ms: 1.02x slower                                                           |
| generators               | 29.6 ms                                                    | 30.2 ms: 1.02x slower                                                           |
| dulwich_log              | 67.2 ms                                                    | 68.7 ms: 1.02x slower                                                           |
| 2to3                     | 274 ms                                                     | 281 ms: 1.02x slower                                                            |
| asyncio_tcp              | 508 ms                                                     | 520 ms: 1.02x slower                                                            |
| sqlglot_optimize         | 55.5 ms                                                    | 56.9 ms: 1.02x slower                                                           |
| async_tree_none_tg       | 336 ms                                                     | 346 ms: 1.03x slower                                                            |
| dask                     | 369 ms                                                     | 380 ms: 1.03x slower                                                            |
| json                     | 5.31 ms                                                    | 5.46 ms: 1.03x slower                                                           |
| docutils                 | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                          |
| scimark_lu               | 122 ms                                                     | 126 ms: 1.03x slower                                                            |
| typing_runtime_protocols | 165 us                                                     | 170 us: 1.03x slower                                                            |
| raytrace                 | 267 ms                                                     | 276 ms: 1.03x slower                                                            |
| pycparser                | 1.16 sec                                                   | 1.20 sec: 1.04x slower                                                          |
| sqlglot_normalize        | 110 ms                                                     | 114 ms: 1.04x slower                                                            |
| python_startup           | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                                           |
| bench_thread_pool        | 834 us                                                     | 873 us: 1.05x slower                                                            |
| scimark_sor              | 127 ms                                                     | 134 ms: 1.05x slower                                                            |
| hexiom                   | 6.30 ms                                                    | 6.63 ms: 1.05x slower                                                           |
| genshi_text              | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                           |
| async_generators         | 442 ms                                                     | 469 ms: 1.06x slower                                                            |
| pickle                   | 11.5 us                                                    | 12.2 us: 1.06x slower                                                           |
| async_tree_memoization   | 463 ms                                                     | 492 ms: 1.06x slower                                                            |
| django_template          | 34.8 ms                                                    | 37.0 ms: 1.06x slower                                                           |
| sympy_str                | 282 ms                                                     | 300 ms: 1.06x slower                                                            |
| nqueens                  | 81.4 ms                                                    | 86.7 ms: 1.06x slower                                                           |
| sympy_expand             | 473 ms                                                     | 509 ms: 1.08x slower                                                            |
| python_startup_no_site   | 7.11 ms                                                    | 7.65 ms: 1.08x slower                                                           |
| sympy_sum                | 156 ms                                                     | 170 ms: 1.09x slower                                                            |
| sympy_integrate          | 20.5 ms                                                    | 22.4 ms: 1.09x slower                                                           |
| async_tree_io_tg         | 936 ms                                                     | 1.02 sec: 1.09x slower                                                          |
| pylint                   | 317 ms                                                     | 349 ms: 1.10x slower                                                            |
| deltablue                | 3.25 ms                                                    | 3.61 ms: 1.11x slower                                                           |
| genshi_xml               | 51.6 ms                                                    | 58.8 ms: 1.14x slower                                                           |
| Geometric mean           | (ref)                                                      | 1.01x faster                                                                    |

Benchmark hidden because not significant (12): async_tree_none, async_tree_cpu_io_mixed_tg, sqlglot_parse, unpickle, asyncio_websockets, regex_compile, json_loads, comprehensions, bench_mp_pool, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization_tg
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 59.18% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x