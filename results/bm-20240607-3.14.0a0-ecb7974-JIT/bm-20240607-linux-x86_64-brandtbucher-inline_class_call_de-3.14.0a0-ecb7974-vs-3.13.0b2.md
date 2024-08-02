# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: inline_class_call_de
- machine: linux-x86_64
- commit hash: ecb7974
- commit date: 2024-06-07
- overall geometric mean: 1.00x faster
- HPT reliability: 78.40%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 280 ms: 1.02x slower                                                        |
| docutils       | 2.83 sec                                                   | 2.93 sec: 1.04x slower                                                      |
| html5lib       | 67.2 ms                                                    | 68.3 ms: 1.02x slower                                                       |
| tornado_http   | 94.6 ms                                                    | 98.0 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                      | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|-------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 611 ms                                                     | 634 ms: 1.04x slower                                                        |
| async_tree_memoization  | 463 ms                                                     | 483 ms: 1.04x slower                                                        |
| Geometric mean          | (ref)                                                      | 1.01x slower                                                                |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_none, async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 80.1 ms: 1.10x faster                                                       |
| float          | 78.9 ms                                                    | 72.5 ms: 1.09x faster                                                       |
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                      | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.3 ms: 1.03x faster                                                       |
| regex_effbot   | 3.67 ms                                                    | 3.65 ms: 1.01x faster                                                       |
| regex_dna      | 221 ms                                                     | 224 ms: 1.01x slower                                                        |
| regex_compile  | 137 ms                                                     | 139 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                      | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 149 ms: 1.09x faster                                                        |
| tomli_loads          | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.07x faster                                                        |
| xml_etree_generate   | 87.4 ms                                                    | 82.5 ms: 1.06x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 58.7 ms: 1.04x faster                                                       |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                                        |
| unpickle_list        | 5.34 us                                                    | 5.43 us: 1.02x slower                                                       |
| unpickle_pure_python | 218 us                                                     | 225 us: 1.03x slower                                                        |
| pickle_list          | 5.11 us                                                    | 5.33 us: 1.04x slower                                                       |
| pickle_dict          | 34.8 us                                                    | 36.3 us: 1.04x slower                                                       |
| pickle               | 11.5 us                                                    | 12.3 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                                |

Benchmark hidden because not significant (2): unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.64 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                      | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.1 ms: 1.12x faster                                                       |
| django_template | 34.8 ms                                                    | 36.1 ms: 1.04x slower                                                       |
| genshi_text     | 23.7 ms                                                    | 25.3 ms: 1.07x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 57.7 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|--------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| scimark_fft              | 392 ms                                                     | 312 ms: 1.26x faster                                                        |
| richards                 | 50.9 ms                                                    | 41.8 ms: 1.22x faster                                                       |
| richards_super           | 57.4 ms                                                    | 47.6 ms: 1.21x faster                                                       |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.51 ms: 1.17x faster                                                       |
| crypto_pyaes             | 77.5 ms                                                    | 68.4 ms: 1.13x faster                                                       |
| fannkuch                 | 402 ms                                                     | 356 ms: 1.13x faster                                                        |
| spectral_norm            | 116 ms                                                     | 103 ms: 1.13x faster                                                        |
| mako                     | 11.2 ms                                                    | 10.1 ms: 1.12x faster                                                       |
| gc_traversal             | 3.98 ms                                                    | 3.59 ms: 1.11x faster                                                       |
| scimark_monte_carlo      | 69.2 ms                                                    | 62.5 ms: 1.11x faster                                                       |
| nbody                    | 88.3 ms                                                    | 80.1 ms: 1.10x faster                                                       |
| float                    | 78.9 ms                                                    | 72.5 ms: 1.09x faster                                                       |
| xml_etree_parse          | 162 ms                                                     | 149 ms: 1.09x faster                                                        |
| tomli_loads              | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                      |
| xml_etree_iterparse      | 107 ms                                                     | 101 ms: 1.07x faster                                                        |
| xml_etree_generate       | 87.4 ms                                                    | 82.5 ms: 1.06x faster                                                       |
| pprint_safe_repr         | 758 ms                                                     | 716 ms: 1.06x faster                                                        |
| pathlib                  | 17.3 ms                                                    | 16.4 ms: 1.05x faster                                                       |
| pprint_pformat           | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                                      |
| pyflate                  | 484 ms                                                     | 463 ms: 1.05x faster                                                        |
| sqlite_synth             | 2.99 us                                                    | 2.86 us: 1.04x faster                                                       |
| xml_etree_process        | 61.2 ms                                                    | 58.7 ms: 1.04x faster                                                       |
| deepcopy_memo            | 39.7 us                                                    | 38.3 us: 1.04x faster                                                       |
| regex_v8                 | 25.1 ms                                                    | 24.3 ms: 1.03x faster                                                       |
| telco                    | 8.41 ms                                                    | 8.16 ms: 1.03x faster                                                       |
| coroutines               | 23.2 ms                                                    | 22.6 ms: 1.02x faster                                                       |
| chaos                    | 61.3 ms                                                    | 60.1 ms: 1.02x faster                                                       |
| logging_format           | 6.47 us                                                    | 6.35 us: 1.02x faster                                                       |
| json_dumps               | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| pickle_pure_python       | 305 us                                                     | 300 us: 1.02x faster                                                        |
| thrift                   | 823 us                                                     | 811 us: 1.01x faster                                                        |
| pidigits                 | 191 ms                                                     | 189 ms: 1.01x faster                                                        |
| logging_simple           | 5.74 us                                                    | 5.69 us: 1.01x faster                                                       |
| create_gc_cycles         | 1.82 ms                                                    | 1.80 ms: 1.01x faster                                                       |
| deepcopy_reduce          | 3.35 us                                                    | 3.32 us: 1.01x faster                                                       |
| sqlglot_parse            | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                       |
| meteor_contest           | 110 ms                                                     | 109 ms: 1.01x faster                                                        |
| regex_effbot             | 3.67 ms                                                    | 3.65 ms: 1.01x faster                                                       |
| mdp                      | 2.79 sec                                                   | 2.79 sec: 1.00x slower                                                      |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.85 sec: 1.01x slower                                                      |
| scimark_sor              | 127 ms                                                     | 128 ms: 1.01x slower                                                        |
| asyncio_tcp              | 508 ms                                                     | 512 ms: 1.01x slower                                                        |
| sqlglot_transpile        | 1.63 ms                                                    | 1.65 ms: 1.01x slower                                                       |
| regex_dna                | 221 ms                                                     | 224 ms: 1.01x slower                                                        |
| coverage                 | 93.1 ms                                                    | 94.4 ms: 1.01x slower                                                       |
| unpickle_list            | 5.34 us                                                    | 5.43 us: 1.02x slower                                                       |
| html5lib                 | 67.2 ms                                                    | 68.3 ms: 1.02x slower                                                       |
| regex_compile            | 137 ms                                                     | 139 ms: 1.02x slower                                                        |
| json                     | 5.31 ms                                                    | 5.40 ms: 1.02x slower                                                       |
| 2to3                     | 274 ms                                                     | 280 ms: 1.02x slower                                                        |
| dask                     | 369 ms                                                     | 379 ms: 1.02x slower                                                        |
| generators               | 29.6 ms                                                    | 30.4 ms: 1.03x slower                                                       |
| comprehensions           | 16.6 us                                                    | 17.1 us: 1.03x slower                                                       |
| sqlglot_optimize         | 55.5 ms                                                    | 57.1 ms: 1.03x slower                                                       |
| dulwich_log              | 67.2 ms                                                    | 69.2 ms: 1.03x slower                                                       |
| sqlglot_normalize        | 110 ms                                                     | 114 ms: 1.03x slower                                                        |
| logging_silent           | 105 ns                                                     | 108 ns: 1.03x slower                                                        |
| unpickle_pure_python     | 218 us                                                     | 225 us: 1.03x slower                                                        |
| tornado_http             | 94.6 ms                                                    | 98.0 ms: 1.04x slower                                                       |
| docutils                 | 2.83 sec                                                   | 2.93 sec: 1.04x slower                                                      |
| async_tree_cpu_io_mixed  | 611 ms                                                     | 634 ms: 1.04x slower                                                        |
| django_template          | 34.8 ms                                                    | 36.1 ms: 1.04x slower                                                       |
| scimark_lu               | 122 ms                                                     | 126 ms: 1.04x slower                                                        |
| go                       | 145 ms                                                     | 151 ms: 1.04x slower                                                        |
| python_startup           | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                                       |
| async_tree_memoization   | 463 ms                                                     | 483 ms: 1.04x slower                                                        |
| pickle_list              | 5.11 us                                                    | 5.33 us: 1.04x slower                                                       |
| pickle_dict              | 34.8 us                                                    | 36.3 us: 1.04x slower                                                       |
| raytrace                 | 267 ms                                                     | 279 ms: 1.04x slower                                                        |
| typing_runtime_protocols | 165 us                                                     | 173 us: 1.05x slower                                                        |
| bench_thread_pool        | 834 us                                                     | 878 us: 1.05x slower                                                        |
| async_generators         | 442 ms                                                     | 470 ms: 1.06x slower                                                        |
| hexiom                   | 6.30 ms                                                    | 6.70 ms: 1.06x slower                                                       |
| genshi_text              | 23.7 ms                                                    | 25.3 ms: 1.07x slower                                                       |
| pickle                   | 11.5 us                                                    | 12.3 us: 1.07x slower                                                       |
| sympy_str                | 282 ms                                                     | 303 ms: 1.07x slower                                                        |
| nqueens                  | 81.4 ms                                                    | 87.3 ms: 1.07x slower                                                       |
| python_startup_no_site   | 7.11 ms                                                    | 7.64 ms: 1.07x slower                                                       |
| sympy_expand             | 473 ms                                                     | 514 ms: 1.09x slower                                                        |
| sympy_integrate          | 20.5 ms                                                    | 22.7 ms: 1.11x slower                                                       |
| pylint                   | 317 ms                                                     | 353 ms: 1.11x slower                                                        |
| genshi_xml               | 51.6 ms                                                    | 57.7 ms: 1.12x slower                                                       |
| sympy_sum                | 156 ms                                                     | 174 ms: 1.12x slower                                                        |
| deltablue                | 3.25 ms                                                    | 3.74 ms: 1.15x slower                                                       |
| Geometric mean           | (ref)                                                      | 1.00x faster                                                                |

Benchmark hidden because not significant (12): async_tree_io_tg, unpickle, async_tree_none, asyncio_websockets, bench_mp_pool, async_tree_memoization_tg, json_loads, pycparser, deepcopy, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none_tg
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 78.40% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x