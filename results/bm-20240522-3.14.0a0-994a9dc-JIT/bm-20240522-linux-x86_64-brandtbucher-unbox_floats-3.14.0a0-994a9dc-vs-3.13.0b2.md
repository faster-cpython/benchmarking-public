# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: unbox_floats
- machine: linux-x86_64
- commit hash: 994a9dc
- commit date: 2024-05-22
- overall geometric mean: 1.00x slower
- HPT reliability: 96.96%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 279 ms: 1.02x slower                                                |
| chameleon      | 7.22 ms                                                    | 7.13 ms: 1.01x faster                                               |
| docutils       | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                              |
| html5lib       | 67.2 ms                                                    | 68.0 ms: 1.01x slower                                               |
| tornado_http   | 94.6 ms                                                    | 96.8 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                      | 1.02x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io  | 939 ms                                                     | 977 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                      | 1.01x slower                                                        |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 76.0 ms: 1.04x faster                                               |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                |
| nbody          | 88.3 ms                                                    | 110 ms: 1.24x slower                                                |
| Geometric mean | (ref)                                                      | 1.06x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 25.3 ms: 1.01x slower                                               |
| regex_compile  | 137 ms                                                     | 139 ms: 1.01x slower                                                |
| regex_dna      | 221 ms                                                     | 227 ms: 1.03x slower                                                |
| regex_effbot   | 3.67 ms                                                    | 3.80 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                      | 1.02x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                              |
| xml_etree_parse      | 162 ms                                                     | 149 ms: 1.08x faster                                                |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.07x faster                                                |
| xml_etree_generate   | 87.4 ms                                                    | 83.1 ms: 1.05x faster                                               |
| xml_etree_process    | 61.2 ms                                                    | 58.4 ms: 1.05x faster                                               |
| unpickle_list        | 5.34 us                                                    | 5.18 us: 1.03x faster                                               |
| pickle_pure_python   | 305 us                                                     | 298 us: 1.03x faster                                                |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                               |
| pickle_dict          | 34.8 us                                                    | 35.0 us: 1.01x slower                                               |
| json_loads           | 28.9 us                                                    | 29.1 us: 1.01x slower                                               |
| unpickle_pure_python | 218 us                                                     | 222 us: 1.02x slower                                                |
| pickle_list          | 5.11 us                                                    | 5.23 us: 1.02x slower                                               |
| unpickle             | 15.1 us                                                    | 15.8 us: 1.04x slower                                               |
| pickle               | 11.5 us                                                    | 12.1 us: 1.05x slower                                               |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.9 ms: 1.02x slower                                               |
| python_startup_no_site | 7.11 ms                                                    | 7.61 ms: 1.07x slower                                               |
| Geometric mean         | (ref)                                                      | 1.04x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.92 ms: 1.13x faster                                               |
| django_template | 34.8 ms                                                    | 36.4 ms: 1.05x slower                                               |
| genshi_text     | 23.7 ms                                                    | 25.2 ms: 1.06x slower                                               |
| genshi_xml      | 51.6 ms                                                    | 57.8 ms: 1.12x slower                                               |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                        |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|--------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| richards                 | 50.9 ms                                                    | 42.0 ms: 1.21x faster                                               |
| richards_super           | 57.4 ms                                                    | 48.2 ms: 1.19x faster                                               |
| fannkuch                 | 402 ms                                                     | 351 ms: 1.15x faster                                                |
| crypto_pyaes             | 77.5 ms                                                    | 68.0 ms: 1.14x faster                                               |
| scimark_fft              | 392 ms                                                     | 345 ms: 1.14x faster                                                |
| mako                     | 11.2 ms                                                    | 9.92 ms: 1.13x faster                                               |
| pyflate                  | 484 ms                                                     | 439 ms: 1.10x faster                                                |
| tomli_loads              | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                              |
| spectral_norm            | 116 ms                                                     | 106 ms: 1.10x faster                                                |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.80 ms: 1.10x faster                                               |
| scimark_monte_carlo      | 69.2 ms                                                    | 63.7 ms: 1.09x faster                                               |
| xml_etree_parse          | 162 ms                                                     | 149 ms: 1.08x faster                                                |
| mdp                      | 2.79 sec                                                   | 2.60 sec: 1.07x faster                                              |
| xml_etree_iterparse      | 107 ms                                                     | 101 ms: 1.07x faster                                                |
| pprint_safe_repr         | 758 ms                                                     | 714 ms: 1.06x faster                                                |
| pprint_pformat           | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                              |
| xml_etree_generate       | 87.4 ms                                                    | 83.1 ms: 1.05x faster                                               |
| deepcopy_memo            | 39.7 us                                                    | 37.8 us: 1.05x faster                                               |
| xml_etree_process        | 61.2 ms                                                    | 58.4 ms: 1.05x faster                                               |
| pathlib                  | 17.3 ms                                                    | 16.7 ms: 1.04x faster                                               |
| float                    | 78.9 ms                                                    | 76.0 ms: 1.04x faster                                               |
| unpickle_list            | 5.34 us                                                    | 5.18 us: 1.03x faster                                               |
| sqlite_synth             | 2.99 us                                                    | 2.91 us: 1.03x faster                                               |
| pickle_pure_python       | 305 us                                                     | 298 us: 1.03x faster                                                |
| json_dumps               | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                               |
| telco                    | 8.41 ms                                                    | 8.23 ms: 1.02x faster                                               |
| pidigits                 | 191 ms                                                     | 188 ms: 1.02x faster                                                |
| logging_format           | 6.47 us                                                    | 6.36 us: 1.02x faster                                               |
| deepcopy_reduce          | 3.35 us                                                    | 3.31 us: 1.01x faster                                               |
| chameleon                | 7.22 ms                                                    | 7.13 ms: 1.01x faster                                               |
| meteor_contest           | 110 ms                                                     | 109 ms: 1.01x faster                                                |
| sqlglot_parse            | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                               |
| regex_v8                 | 25.1 ms                                                    | 25.3 ms: 1.01x slower                                               |
| pickle_dict              | 34.8 us                                                    | 35.0 us: 1.01x slower                                               |
| logging_simple           | 5.74 us                                                    | 5.78 us: 1.01x slower                                               |
| json_loads               | 28.9 us                                                    | 29.1 us: 1.01x slower                                               |
| bench_mp_pool            | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                               |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                              |
| html5lib                 | 67.2 ms                                                    | 68.0 ms: 1.01x slower                                               |
| regex_compile            | 137 ms                                                     | 139 ms: 1.01x slower                                                |
| logging_silent           | 105 ns                                                     | 106 ns: 1.01x slower                                                |
| python_startup           | 10.8 ms                                                    | 10.9 ms: 1.02x slower                                               |
| coverage                 | 93.1 ms                                                    | 94.8 ms: 1.02x slower                                               |
| 2to3                     | 274 ms                                                     | 279 ms: 1.02x slower                                                |
| unpickle_pure_python     | 218 us                                                     | 222 us: 1.02x slower                                                |
| sqlglot_optimize         | 55.5 ms                                                    | 56.7 ms: 1.02x slower                                               |
| sqlglot_normalize        | 110 ms                                                     | 113 ms: 1.02x slower                                                |
| tornado_http             | 94.6 ms                                                    | 96.8 ms: 1.02x slower                                               |
| asyncio_tcp              | 508 ms                                                     | 520 ms: 1.02x slower                                                |
| pickle_list              | 5.11 us                                                    | 5.23 us: 1.02x slower                                               |
| dask                     | 369 ms                                                     | 378 ms: 1.02x slower                                                |
| gc_traversal             | 3.98 ms                                                    | 4.08 ms: 1.03x slower                                               |
| dulwich_log              | 67.2 ms                                                    | 68.9 ms: 1.03x slower                                               |
| regex_dna                | 221 ms                                                     | 227 ms: 1.03x slower                                                |
| flaskblogging            | 9.01 ms                                                    | 9.28 ms: 1.03x slower                                               |
| chaos                    | 61.3 ms                                                    | 63.2 ms: 1.03x slower                                               |
| go                       | 145 ms                                                     | 149 ms: 1.03x slower                                                |
| regex_effbot             | 3.67 ms                                                    | 3.80 ms: 1.03x slower                                               |
| scimark_lu               | 122 ms                                                     | 126 ms: 1.04x slower                                                |
| pycparser                | 1.16 sec                                                   | 1.20 sec: 1.04x slower                                              |
| generators               | 29.6 ms                                                    | 30.8 ms: 1.04x slower                                               |
| bench_thread_pool        | 834 us                                                     | 866 us: 1.04x slower                                                |
| async_tree_io            | 939 ms                                                     | 977 ms: 1.04x slower                                                |
| unpickle                 | 15.1 us                                                    | 15.8 us: 1.04x slower                                               |
| django_template          | 34.8 ms                                                    | 36.4 ms: 1.05x slower                                               |
| docutils                 | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                              |
| hexiom                   | 6.30 ms                                                    | 6.62 ms: 1.05x slower                                               |
| pickle                   | 11.5 us                                                    | 12.1 us: 1.05x slower                                               |
| typing_runtime_protocols | 165 us                                                     | 174 us: 1.05x slower                                                |
| async_generators         | 442 ms                                                     | 467 ms: 1.06x slower                                                |
| genshi_text              | 23.7 ms                                                    | 25.2 ms: 1.06x slower                                               |
| raytrace                 | 267 ms                                                     | 284 ms: 1.07x slower                                                |
| scimark_sor              | 127 ms                                                     | 136 ms: 1.07x slower                                                |
| sympy_str                | 282 ms                                                     | 302 ms: 1.07x slower                                                |
| nqueens                  | 81.4 ms                                                    | 87.0 ms: 1.07x slower                                               |
| python_startup_no_site   | 7.11 ms                                                    | 7.61 ms: 1.07x slower                                               |
| sympy_expand             | 473 ms                                                     | 511 ms: 1.08x slower                                                |
| sympy_integrate          | 20.5 ms                                                    | 22.6 ms: 1.10x slower                                               |
| sympy_sum                | 156 ms                                                     | 173 ms: 1.11x slower                                                |
| pylint                   | 317 ms                                                     | 354 ms: 1.12x slower                                                |
| genshi_xml               | 51.6 ms                                                    | 57.8 ms: 1.12x slower                                               |
| deltablue                | 3.25 ms                                                    | 3.72 ms: 1.14x slower                                               |
| nbody                    | 88.3 ms                                                    | 110 ms: 1.24x slower                                                |
| Geometric mean           | (ref)                                                      | 1.00x slower                                                        |

Benchmark hidden because not significant (13): coroutines, async_tree_cpu_io_mixed_tg, async_tree_none_tg, comprehensions, create_gc_cycles, asyncio_websockets, sqlglot_transpile, async_tree_memoization, async_tree_memoization_tg, deepcopy, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, gunicorn, json, mypy2, thrift

# HPT report

- Reliability score: 96.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x