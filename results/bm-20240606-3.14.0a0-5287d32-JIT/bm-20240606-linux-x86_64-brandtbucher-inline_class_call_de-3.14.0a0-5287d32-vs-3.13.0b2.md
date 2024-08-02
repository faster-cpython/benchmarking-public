# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: inline_class_call_de
- machine: linux-x86_64
- commit hash: 5287d32
- commit date: 2024-06-06
- overall geometric mean: 1.00x faster
- HPT reliability: 94.11%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 280 ms: 1.02x slower                                                        |
| docutils       | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                      |
| html5lib       | 67.2 ms                                                    | 68.8 ms: 1.02x slower                                                       |
| tornado_http   | 94.6 ms                                                    | 98.7 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                      | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|-------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 611 ms                                                     | 633 ms: 1.04x slower                                                        |
| async_tree_io           | 939 ms                                                     | 981 ms: 1.05x slower                                                        |
| Geometric mean          | (ref)                                                      | 1.02x slower                                                                |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 80.4 ms: 1.10x faster                                                       |
| float          | 78.9 ms                                                    | 73.6 ms: 1.07x faster                                                       |
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                      | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 139 ms: 1.01x slower                                                        |
| regex_v8       | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                                       |
| regex_dna      | 221 ms                                                     | 229 ms: 1.04x slower                                                        |
| regex_effbot   | 3.67 ms                                                    | 4.00 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                      | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.09x faster                                                        |
| tomli_loads          | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.06x faster                                                        |
| xml_etree_generate   | 87.4 ms                                                    | 82.3 ms: 1.06x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 58.1 ms: 1.05x faster                                                       |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                       |
| pickle_pure_python   | 305 us                                                     | 303 us: 1.01x faster                                                        |
| unpickle_list        | 5.34 us                                                    | 5.41 us: 1.01x slower                                                       |
| unpickle_pure_python | 218 us                                                     | 222 us: 1.02x slower                                                        |
| pickle_dict          | 34.8 us                                                    | 35.7 us: 1.03x slower                                                       |
| pickle_list          | 5.11 us                                                    | 5.24 us: 1.03x slower                                                       |
| pickle               | 11.5 us                                                    | 12.1 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                                |

Benchmark hidden because not significant (2): unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.64 ms: 1.08x slower                                                       |
| Geometric mean         | (ref)                                                      | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.1 ms: 1.11x faster                                                       |
| django_template | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                                       |
| genshi_text     | 23.7 ms                                                    | 25.2 ms: 1.07x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 58.6 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|--------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| scimark_fft              | 392 ms                                                     | 315 ms: 1.25x faster                                                        |
| richards                 | 50.9 ms                                                    | 41.7 ms: 1.22x faster                                                       |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.39 ms: 1.20x faster                                                       |
| richards_super           | 57.4 ms                                                    | 47.8 ms: 1.20x faster                                                       |
| spectral_norm            | 116 ms                                                     | 100 ms: 1.16x faster                                                        |
| crypto_pyaes             | 77.5 ms                                                    | 67.5 ms: 1.15x faster                                                       |
| fannkuch                 | 402 ms                                                     | 354 ms: 1.14x faster                                                        |
| mako                     | 11.2 ms                                                    | 10.1 ms: 1.11x faster                                                       |
| scimark_monte_carlo      | 69.2 ms                                                    | 62.7 ms: 1.10x faster                                                       |
| pyflate                  | 484 ms                                                     | 439 ms: 1.10x faster                                                        |
| nbody                    | 88.3 ms                                                    | 80.4 ms: 1.10x faster                                                       |
| xml_etree_parse          | 162 ms                                                     | 148 ms: 1.09x faster                                                        |
| tomli_loads              | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                      |
| pprint_pformat           | 1.56 sec                                                   | 1.44 sec: 1.08x faster                                                      |
| float                    | 78.9 ms                                                    | 73.6 ms: 1.07x faster                                                       |
| pprint_safe_repr         | 758 ms                                                     | 711 ms: 1.07x faster                                                        |
| xml_etree_iterparse      | 107 ms                                                     | 101 ms: 1.06x faster                                                        |
| xml_etree_generate       | 87.4 ms                                                    | 82.3 ms: 1.06x faster                                                       |
| pathlib                  | 17.3 ms                                                    | 16.4 ms: 1.06x faster                                                       |
| mdp                      | 2.79 sec                                                   | 2.65 sec: 1.05x faster                                                      |
| xml_etree_process        | 61.2 ms                                                    | 58.1 ms: 1.05x faster                                                       |
| sqlite_synth             | 2.99 us                                                    | 2.84 us: 1.05x faster                                                       |
| telco                    | 8.41 ms                                                    | 8.04 ms: 1.05x faster                                                       |
| coroutines               | 23.2 ms                                                    | 22.5 ms: 1.03x faster                                                       |
| json_dumps               | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                       |
| chaos                    | 61.3 ms                                                    | 59.6 ms: 1.03x faster                                                       |
| logging_format           | 6.47 us                                                    | 6.30 us: 1.03x faster                                                       |
| deepcopy_memo            | 39.7 us                                                    | 38.8 us: 1.02x faster                                                       |
| logging_simple           | 5.74 us                                                    | 5.62 us: 1.02x faster                                                       |
| meteor_contest           | 110 ms                                                     | 108 ms: 1.02x faster                                                        |
| pidigits                 | 191 ms                                                     | 189 ms: 1.01x faster                                                        |
| deepcopy_reduce          | 3.35 us                                                    | 3.31 us: 1.01x faster                                                       |
| gc_traversal             | 3.98 ms                                                    | 3.94 ms: 1.01x faster                                                       |
| pickle_pure_python       | 305 us                                                     | 303 us: 1.01x faster                                                        |
| create_gc_cycles         | 1.82 ms                                                    | 1.81 ms: 1.01x faster                                                       |
| comprehensions           | 16.6 us                                                    | 16.7 us: 1.00x slower                                                       |
| sqlglot_transpile        | 1.63 ms                                                    | 1.65 ms: 1.01x slower                                                       |
| unpickle_list            | 5.34 us                                                    | 5.41 us: 1.01x slower                                                       |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                                      |
| regex_compile            | 137 ms                                                     | 139 ms: 1.01x slower                                                        |
| json                     | 5.31 ms                                                    | 5.39 ms: 1.02x slower                                                       |
| deepcopy                 | 367 us                                                     | 374 us: 1.02x slower                                                        |
| unpickle_pure_python     | 218 us                                                     | 222 us: 1.02x slower                                                        |
| 2to3                     | 274 ms                                                     | 280 ms: 1.02x slower                                                        |
| go                       | 145 ms                                                     | 148 ms: 1.02x slower                                                        |
| html5lib                 | 67.2 ms                                                    | 68.8 ms: 1.02x slower                                                       |
| scimark_lu               | 122 ms                                                     | 125 ms: 1.02x slower                                                        |
| pickle_dict              | 34.8 us                                                    | 35.7 us: 1.03x slower                                                       |
| pickle_list              | 5.11 us                                                    | 5.24 us: 1.03x slower                                                       |
| dask                     | 369 ms                                                     | 379 ms: 1.03x slower                                                        |
| asyncio_tcp              | 508 ms                                                     | 522 ms: 1.03x slower                                                        |
| sqlglot_optimize         | 55.5 ms                                                    | 57.2 ms: 1.03x slower                                                       |
| logging_silent           | 105 ns                                                     | 108 ns: 1.03x slower                                                        |
| regex_v8                 | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                                       |
| dulwich_log              | 67.2 ms                                                    | 69.5 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed  | 611 ms                                                     | 633 ms: 1.04x slower                                                        |
| typing_runtime_protocols | 165 us                                                     | 171 us: 1.04x slower                                                        |
| generators               | 29.6 ms                                                    | 30.7 ms: 1.04x slower                                                       |
| sqlglot_normalize        | 110 ms                                                     | 114 ms: 1.04x slower                                                        |
| regex_dna                | 221 ms                                                     | 229 ms: 1.04x slower                                                        |
| tornado_http             | 94.6 ms                                                    | 98.7 ms: 1.04x slower                                                       |
| python_startup           | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                                       |
| async_tree_io            | 939 ms                                                     | 981 ms: 1.05x slower                                                        |
| docutils                 | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                      |
| scimark_sor              | 127 ms                                                     | 134 ms: 1.05x slower                                                        |
| raytrace                 | 267 ms                                                     | 279 ms: 1.05x slower                                                        |
| django_template          | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                                       |
| pycparser                | 1.16 sec                                                   | 1.22 sec: 1.05x slower                                                      |
| pickle                   | 11.5 us                                                    | 12.1 us: 1.06x slower                                                       |
| bench_thread_pool        | 834 us                                                     | 883 us: 1.06x slower                                                        |
| hexiom                   | 6.30 ms                                                    | 6.67 ms: 1.06x slower                                                       |
| async_generators         | 442 ms                                                     | 468 ms: 1.06x slower                                                        |
| nqueens                  | 81.4 ms                                                    | 86.6 ms: 1.06x slower                                                       |
| genshi_text              | 23.7 ms                                                    | 25.2 ms: 1.07x slower                                                       |
| python_startup_no_site   | 7.11 ms                                                    | 7.64 ms: 1.08x slower                                                       |
| sympy_str                | 282 ms                                                     | 304 ms: 1.08x slower                                                        |
| sympy_expand             | 473 ms                                                     | 511 ms: 1.08x slower                                                        |
| regex_effbot             | 3.67 ms                                                    | 4.00 ms: 1.09x slower                                                       |
| sympy_integrate          | 20.5 ms                                                    | 22.6 ms: 1.10x slower                                                       |
| sympy_sum                | 156 ms                                                     | 174 ms: 1.12x slower                                                        |
| pylint                   | 317 ms                                                     | 354 ms: 1.12x slower                                                        |
| genshi_xml               | 51.6 ms                                                    | 58.6 ms: 1.14x slower                                                       |
| deltablue                | 3.25 ms                                                    | 3.71 ms: 1.14x slower                                                       |
| Geometric mean           | (ref)                                                      | 1.00x faster                                                                |

Benchmark hidden because not significant (13): async_tree_io_tg, thrift, unpickle, sqlglot_parse, asyncio_websockets, async_tree_none, json_loads, bench_mp_pool, coverage, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 94.11% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x