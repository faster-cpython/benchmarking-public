# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: c3cb6dd
- commit date: 2024-05-22
- overall geometric mean: 1.01x faster
- HPT reliability: 87.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 275 ms: 1.00x slower                                                  |
| chameleon      | 7.22 ms                                                    | 7.14 ms: 1.01x faster                                                 |
| docutils       | 2.83 sec                                                   | 2.90 sec: 1.02x slower                                                |
| html5lib       | 67.2 ms                                                    | 66.3 ms: 1.01x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 96.7 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 79.3 ms: 1.11x faster                                                 |
| float          | 78.9 ms                                                    | 72.2 ms: 1.09x faster                                                 |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                      | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 23.7 ms: 1.06x faster                                                 |
| regex_compile  | 137 ms                                                     | 135 ms: 1.01x faster                                                  |
| regex_dna      | 221 ms                                                     | 225 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 151 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.07x faster                                                  |
| xml_etree_generate   | 87.4 ms                                                    | 82.5 ms: 1.06x faster                                                 |
| tomli_loads          | 2.12 sec                                                   | 2.01 sec: 1.06x faster                                                |
| xml_etree_process    | 61.2 ms                                                    | 58.3 ms: 1.05x faster                                                 |
| unpickle_list        | 5.34 us                                                    | 5.10 us: 1.05x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.05x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                                  |
| json_loads           | 28.9 us                                                    | 28.5 us: 1.01x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 227 us: 1.04x slower                                                  |
| pickle               | 11.5 us                                                    | 12.2 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (3): unpickle, pickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.9 ms: 1.01x slower                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.58 ms: 1.07x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.04x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.1 ms: 1.11x faster                                                 |
| genshi_text     | 23.7 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| django_template | 34.8 ms                                                    | 36.0 ms: 1.03x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 54.3 ms: 1.05x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.00x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|--------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| richards                 | 50.9 ms                                                    | 40.2 ms: 1.26x faster                                                 |
| scimark_fft              | 392 ms                                                     | 319 ms: 1.23x faster                                                  |
| richards_super           | 57.4 ms                                                    | 46.8 ms: 1.23x faster                                                 |
| crypto_pyaes             | 77.5 ms                                                    | 68.2 ms: 1.14x faster                                                 |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.66 ms: 1.13x faster                                                 |
| nbody                    | 88.3 ms                                                    | 79.3 ms: 1.11x faster                                                 |
| mako                     | 11.2 ms                                                    | 10.1 ms: 1.11x faster                                                 |
| fannkuch                 | 402 ms                                                     | 363 ms: 1.11x faster                                                  |
| pyflate                  | 484 ms                                                     | 439 ms: 1.10x faster                                                  |
| spectral_norm            | 116 ms                                                     | 105 ms: 1.10x faster                                                  |
| scimark_monte_carlo      | 69.2 ms                                                    | 63.1 ms: 1.10x faster                                                 |
| float                    | 78.9 ms                                                    | 72.2 ms: 1.09x faster                                                 |
| pprint_safe_repr         | 758 ms                                                     | 703 ms: 1.08x faster                                                  |
| pprint_pformat           | 1.56 sec                                                   | 1.44 sec: 1.08x faster                                                |
| xml_etree_parse          | 162 ms                                                     | 151 ms: 1.07x faster                                                  |
| xml_etree_iterparse      | 107 ms                                                     | 101 ms: 1.07x faster                                                  |
| regex_v8                 | 25.1 ms                                                    | 23.7 ms: 1.06x faster                                                 |
| deepcopy_memo            | 39.7 us                                                    | 37.5 us: 1.06x faster                                                 |
| gc_traversal             | 3.98 ms                                                    | 3.75 ms: 1.06x faster                                                 |
| xml_etree_generate       | 87.4 ms                                                    | 82.5 ms: 1.06x faster                                                 |
| tomli_loads              | 2.12 sec                                                   | 2.01 sec: 1.06x faster                                                |
| pathlib                  | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                 |
| xml_etree_process        | 61.2 ms                                                    | 58.3 ms: 1.05x faster                                                 |
| unpickle_list            | 5.34 us                                                    | 5.10 us: 1.05x faster                                                 |
| json_dumps               | 10.7 ms                                                    | 10.3 ms: 1.05x faster                                                 |
| sqlglot_parse            | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                                 |
| sqlite_synth             | 2.99 us                                                    | 2.89 us: 1.04x faster                                                 |
| telco                    | 8.41 ms                                                    | 8.13 ms: 1.04x faster                                                 |
| chaos                    | 61.3 ms                                                    | 59.4 ms: 1.03x faster                                                 |
| json                     | 5.31 ms                                                    | 5.16 ms: 1.03x faster                                                 |
| sqlglot_transpile        | 1.63 ms                                                    | 1.59 ms: 1.03x faster                                                 |
| meteor_contest           | 110 ms                                                     | 108 ms: 1.02x faster                                                  |
| deepcopy_reduce          | 3.35 us                                                    | 3.29 us: 1.02x faster                                                 |
| thrift                   | 823 us                                                     | 808 us: 1.02x faster                                                  |
| pidigits                 | 191 ms                                                     | 188 ms: 1.02x faster                                                  |
| pickle_pure_python       | 305 us                                                     | 300 us: 1.02x faster                                                  |
| comprehensions           | 16.6 us                                                    | 16.4 us: 1.01x faster                                                 |
| html5lib                 | 67.2 ms                                                    | 66.3 ms: 1.01x faster                                                 |
| regex_compile            | 137 ms                                                     | 135 ms: 1.01x faster                                                  |
| create_gc_cycles         | 1.82 ms                                                    | 1.79 ms: 1.01x faster                                                 |
| json_loads               | 28.9 us                                                    | 28.5 us: 1.01x faster                                                 |
| chameleon                | 7.22 ms                                                    | 7.14 ms: 1.01x faster                                                 |
| mdp                      | 2.79 sec                                                   | 2.76 sec: 1.01x faster                                                |
| 2to3                     | 274 ms                                                     | 275 ms: 1.00x slower                                                  |
| sqlglot_optimize         | 55.5 ms                                                    | 55.8 ms: 1.00x slower                                                 |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.85 sec: 1.01x slower                                                |
| bench_mp_pool            | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| python_startup           | 10.8 ms                                                    | 10.9 ms: 1.01x slower                                                 |
| genshi_text              | 23.7 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| dask                     | 369 ms                                                     | 375 ms: 1.01x slower                                                  |
| regex_dna                | 221 ms                                                     | 225 ms: 1.02x slower                                                  |
| generators               | 29.6 ms                                                    | 30.2 ms: 1.02x slower                                                 |
| sqlglot_normalize        | 110 ms                                                     | 112 ms: 1.02x slower                                                  |
| asyncio_tcp              | 508 ms                                                     | 519 ms: 1.02x slower                                                  |
| tornado_http             | 94.6 ms                                                    | 96.7 ms: 1.02x slower                                                 |
| docutils                 | 2.83 sec                                                   | 2.90 sec: 1.02x slower                                                |
| flaskblogging            | 9.01 ms                                                    | 9.24 ms: 1.03x slower                                                 |
| dulwich_log              | 67.2 ms                                                    | 68.9 ms: 1.03x slower                                                 |
| raytrace                 | 267 ms                                                     | 274 ms: 1.03x slower                                                  |
| bench_thread_pool        | 834 us                                                     | 859 us: 1.03x slower                                                  |
| typing_runtime_protocols | 165 us                                                     | 170 us: 1.03x slower                                                  |
| coroutines               | 23.2 ms                                                    | 24.0 ms: 1.03x slower                                                 |
| django_template          | 34.8 ms                                                    | 36.0 ms: 1.03x slower                                                 |
| hexiom                   | 6.30 ms                                                    | 6.52 ms: 1.03x slower                                                 |
| unpickle_pure_python     | 218 us                                                     | 227 us: 1.04x slower                                                  |
| scimark_lu               | 122 ms                                                     | 127 ms: 1.04x slower                                                  |
| logging_silent           | 105 ns                                                     | 109 ns: 1.04x slower                                                  |
| nqueens                  | 81.4 ms                                                    | 85.1 ms: 1.04x slower                                                 |
| genshi_xml               | 51.6 ms                                                    | 54.3 ms: 1.05x slower                                                 |
| sympy_str                | 282 ms                                                     | 297 ms: 1.05x slower                                                  |
| pickle                   | 11.5 us                                                    | 12.2 us: 1.06x slower                                                 |
| sympy_expand             | 473 ms                                                     | 503 ms: 1.06x slower                                                  |
| async_generators         | 442 ms                                                     | 471 ms: 1.06x slower                                                  |
| python_startup_no_site   | 7.11 ms                                                    | 7.58 ms: 1.07x slower                                                 |
| scimark_sor              | 127 ms                                                     | 136 ms: 1.07x slower                                                  |
| sympy_sum                | 156 ms                                                     | 168 ms: 1.08x slower                                                  |
| sympy_integrate          | 20.5 ms                                                    | 22.2 ms: 1.08x slower                                                 |
| pylint                   | 317 ms                                                     | 351 ms: 1.11x slower                                                  |
| deltablue                | 3.25 ms                                                    | 3.77 ms: 1.16x slower                                                 |
| Geometric mean           | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (19): async_tree_none_tg, async_tree_memoization, pycparser, unpickle, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization_tg, async_tree_none, deepcopy, asyncio_websockets, logging_format, pickle_list, logging_simple, pickle_dict, go, coverage, regex_effbot, async_tree_cpu_io_mixed, async_tree_io_tg
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2

# HPT report

- Reliability score: 87.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x