# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: hoist
- machine: linux-x86_64
- commit hash: bc99ede
- commit date: 2024-05-08
- overall geometric mean: 1.03x slower
- HPT reliability: 62.54%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 279 ms: 1.02x slower                                         |
| chameleon      | 7.22 ms                                                    | 7.07 ms: 1.02x faster                                        |
| docutils       | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                       |
| html5lib       | 67.2 ms                                                    | 69.7 ms: 1.04x slower                                        |
| tornado_http   | 94.6 ms                                                    | 97.4 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                      | 1.02x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none  | 378 ms                                                     | 364 ms: 1.04x faster                                         |
| async_tree_io_tg | 936 ms                                                     | 1.02 sec: 1.09x slower                                       |
| Geometric mean   | (ref)                                                      | 1.01x slower                                                 |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.8 ms: 1.11x faster                                        |
| nbody          | 88.3 ms                                                    | 86.0 ms: 1.03x faster                                        |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                      | 1.05x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                        |
| regex_effbot   | 3.67 ms                                                    | 3.66 ms: 1.00x faster                                        |
| regex_compile  | 137 ms                                                     | 140 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                      | 1.00x slower                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.99 sec: 1.07x faster                                       |
| xml_etree_generate   | 87.4 ms                                                    | 82.5 ms: 1.06x faster                                        |
| xml_etree_parse      | 162 ms                                                     | 153 ms: 1.06x faster                                         |
| xml_etree_process    | 61.2 ms                                                    | 57.9 ms: 1.06x faster                                        |
| xml_etree_iterparse  | 107 ms                                                     | 102 ms: 1.05x faster                                         |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.04x faster                                        |
| pickle_dict          | 34.8 us                                                    | 33.9 us: 1.03x faster                                        |
| pickle_list          | 5.11 us                                                    | 5.14 us: 1.01x slower                                        |
| pickle_pure_python   | 305 us                                                     | 308 us: 1.01x slower                                         |
| unpickle_list        | 5.34 us                                                    | 5.40 us: 1.01x slower                                        |
| unpickle_pure_python | 218 us                                                     | 221 us: 1.01x slower                                         |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                        |
| unpickle             | 15.1 us                                                    | 16.2 us: 1.07x slower                                        |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                 |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.1 ms: 1.03x slower                                        |
| python_startup_no_site | 7.11 ms                                                    | 7.67 ms: 1.08x slower                                        |
| Geometric mean         | (ref)                                                      | 1.06x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.52 ms: 1.18x faster                                        |
| django_template | 34.8 ms                                                    | 36.0 ms: 1.03x slower                                        |
| genshi_text     | 23.7 ms                                                    | 24.7 ms: 1.05x slower                                        |
| genshi_xml      | 51.6 ms                                                    | 58.5 ms: 1.13x slower                                        |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|--------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| scimark_fft              | 392 ms                                                     | 321 ms: 1.22x faster                                         |
| richards                 | 50.9 ms                                                    | 42.7 ms: 1.19x faster                                        |
| mako                     | 11.2 ms                                                    | 9.52 ms: 1.18x faster                                        |
| richards_super           | 57.4 ms                                                    | 48.8 ms: 1.18x faster                                        |
| spectral_norm            | 116 ms                                                     | 99.0 ms: 1.17x faster                                        |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.55 ms: 1.16x faster                                        |
| crypto_pyaes             | 77.5 ms                                                    | 69.1 ms: 1.12x faster                                        |
| float                    | 78.9 ms                                                    | 70.8 ms: 1.11x faster                                        |
| fannkuch                 | 402 ms                                                     | 368 ms: 1.09x faster                                         |
| pyflate                  | 484 ms                                                     | 449 ms: 1.08x faster                                         |
| scimark_monte_carlo      | 69.2 ms                                                    | 64.1 ms: 1.08x faster                                        |
| mdp                      | 2.79 sec                                                   | 2.61 sec: 1.07x faster                                       |
| tomli_loads              | 2.12 sec                                                   | 1.99 sec: 1.07x faster                                       |
| xml_etree_generate       | 87.4 ms                                                    | 82.5 ms: 1.06x faster                                        |
| xml_etree_parse          | 162 ms                                                     | 153 ms: 1.06x faster                                         |
| xml_etree_process        | 61.2 ms                                                    | 57.9 ms: 1.06x faster                                        |
| xml_etree_iterparse      | 107 ms                                                     | 102 ms: 1.05x faster                                         |
| deepcopy_memo            | 39.7 us                                                    | 37.7 us: 1.05x faster                                        |
| coverage                 | 93.1 ms                                                    | 88.7 ms: 1.05x faster                                        |
| sqlite_synth             | 2.99 us                                                    | 2.87 us: 1.04x faster                                        |
| pprint_safe_repr         | 758 ms                                                     | 727 ms: 1.04x faster                                         |
| async_tree_none          | 378 ms                                                     | 364 ms: 1.04x faster                                         |
| chaos                    | 61.3 ms                                                    | 59.0 ms: 1.04x faster                                        |
| gc_traversal             | 3.98 ms                                                    | 3.84 ms: 1.04x faster                                        |
| json_dumps               | 10.7 ms                                                    | 10.4 ms: 1.04x faster                                        |
| pprint_pformat           | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                       |
| nbody                    | 88.3 ms                                                    | 86.0 ms: 1.03x faster                                        |
| pickle_dict              | 34.8 us                                                    | 33.9 us: 1.03x faster                                        |
| coroutines               | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                        |
| chameleon                | 7.22 ms                                                    | 7.07 ms: 1.02x faster                                        |
| regex_v8                 | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                        |
| thrift                   | 823 us                                                     | 809 us: 1.02x faster                                         |
| pidigits                 | 191 ms                                                     | 188 ms: 1.02x faster                                         |
| deepcopy_reduce          | 3.35 us                                                    | 3.31 us: 1.01x faster                                        |
| logging_format           | 6.47 us                                                    | 6.41 us: 1.01x faster                                        |
| create_gc_cycles         | 1.82 ms                                                    | 1.81 ms: 1.00x faster                                        |
| regex_effbot             | 3.67 ms                                                    | 3.66 ms: 1.00x faster                                        |
| meteor_contest           | 110 ms                                                     | 110 ms: 1.00x slower                                         |
| generators               | 29.6 ms                                                    | 29.7 ms: 1.00x slower                                        |
| pickle_list              | 5.11 us                                                    | 5.14 us: 1.01x slower                                        |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.85 sec: 1.01x slower                                       |
| json                     | 5.31 ms                                                    | 5.34 ms: 1.01x slower                                        |
| sqlglot_transpile        | 1.63 ms                                                    | 1.65 ms: 1.01x slower                                        |
| pickle_pure_python       | 305 us                                                     | 308 us: 1.01x slower                                         |
| bench_mp_pool            | 23.9 ms                                                    | 24.1 ms: 1.01x slower                                        |
| logging_silent           | 105 ns                                                     | 106 ns: 1.01x slower                                         |
| unpickle_list            | 5.34 us                                                    | 5.40 us: 1.01x slower                                        |
| unpickle_pure_python     | 218 us                                                     | 221 us: 1.01x slower                                         |
| scimark_sor              | 127 ms                                                     | 129 ms: 1.01x slower                                         |
| asyncio_tcp              | 508 ms                                                     | 515 ms: 1.01x slower                                         |
| go                       | 145 ms                                                     | 147 ms: 1.02x slower                                         |
| 2to3                     | 274 ms                                                     | 279 ms: 1.02x slower                                         |
| flaskblogging            | 9.01 ms                                                    | 9.23 ms: 1.02x slower                                        |
| pathlib                  | 17.3 ms                                                    | 17.8 ms: 1.03x slower                                        |
| dask                     | 369 ms                                                     | 379 ms: 1.03x slower                                         |
| regex_compile            | 137 ms                                                     | 140 ms: 1.03x slower                                         |
| sqlglot_normalize        | 110 ms                                                     | 113 ms: 1.03x slower                                         |
| sqlglot_optimize         | 55.5 ms                                                    | 57.1 ms: 1.03x slower                                        |
| tornado_http             | 94.6 ms                                                    | 97.4 ms: 1.03x slower                                        |
| deepcopy                 | 367 us                                                     | 378 us: 1.03x slower                                         |
| pickle                   | 11.5 us                                                    | 11.8 us: 1.03x slower                                        |
| scimark_lu               | 122 ms                                                     | 125 ms: 1.03x slower                                         |
| python_startup           | 10.8 ms                                                    | 11.1 ms: 1.03x slower                                        |
| django_template          | 34.8 ms                                                    | 36.0 ms: 1.03x slower                                        |
| html5lib                 | 67.2 ms                                                    | 69.7 ms: 1.04x slower                                        |
| bench_thread_pool        | 834 us                                                     | 868 us: 1.04x slower                                         |
| dulwich_log              | 67.2 ms                                                    | 70.1 ms: 1.04x slower                                        |
| genshi_text              | 23.7 ms                                                    | 24.7 ms: 1.05x slower                                        |
| docutils                 | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                       |
| async_generators         | 442 ms                                                     | 465 ms: 1.05x slower                                         |
| gunicorn                 | 1.28 ms                                                    | 1.35 ms: 1.06x slower                                        |
| raytrace                 | 267 ms                                                     | 283 ms: 1.06x slower                                         |
| aiohttp                  | 1.18 ms                                                    | 1.26 ms: 1.07x slower                                        |
| hexiom                   | 6.30 ms                                                    | 6.73 ms: 1.07x slower                                        |
| unpickle                 | 15.1 us                                                    | 16.2 us: 1.07x slower                                        |
| typing_runtime_protocols | 165 us                                                     | 177 us: 1.08x slower                                         |
| sympy_str                | 282 ms                                                     | 304 ms: 1.08x slower                                         |
| nqueens                  | 81.4 ms                                                    | 87.8 ms: 1.08x slower                                        |
| python_startup_no_site   | 7.11 ms                                                    | 7.67 ms: 1.08x slower                                        |
| sympy_expand             | 473 ms                                                     | 511 ms: 1.08x slower                                         |
| async_tree_io_tg         | 936 ms                                                     | 1.02 sec: 1.09x slower                                       |
| sympy_integrate          | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                        |
| sympy_sum                | 156 ms                                                     | 174 ms: 1.12x slower                                         |
| pylint                   | 317 ms                                                     | 357 ms: 1.13x slower                                         |
| genshi_xml               | 51.6 ms                                                    | 58.5 ms: 1.13x slower                                        |
| deltablue                | 3.25 ms                                                    | 3.73 ms: 1.15x slower                                        |
| telco                    | 8.41 ms                                                    | 171 ms: 20.37x slower                                        |
| Geometric mean           | (ref)                                                      | 1.03x slower                                                 |

Benchmark hidden because not significant (13): pycparser, async_tree_cpu_io_mixed_tg, async_tree_io, sqlglot_parse, logging_simple, comprehensions, regex_dna, asyncio_websockets, json_loads, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization
Ignored benchmarks (3) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, djangocms, mypy2

# HPT report

- Reliability score: 62.54% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x