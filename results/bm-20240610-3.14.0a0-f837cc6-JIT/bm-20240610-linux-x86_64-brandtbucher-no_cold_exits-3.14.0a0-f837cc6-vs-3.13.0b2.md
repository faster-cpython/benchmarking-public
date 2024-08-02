# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-x86_64
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.01x faster
- HPT reliability: 56.82%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 277 ms: 1.01x slower                                                 |
| docutils       | 2.83 sec                                                   | 2.93 sec: 1.04x slower                                               |
| html5lib       | 67.2 ms                                                    | 68.5 ms: 1.02x slower                                                |
| tornado_http   | 94.6 ms                                                    | 96.9 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                      | 1.02x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 611 ms                                                     | 631 ms: 1.03x slower                                                 |
| async_tree_io           | 939 ms                                                     | 972 ms: 1.04x slower                                                 |
| async_tree_memoization  | 463 ms                                                     | 482 ms: 1.04x slower                                                 |
| Geometric mean          | (ref)                                                      | 1.01x slower                                                         |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 72.3 ms: 1.09x faster                                                |
| nbody          | 88.3 ms                                                    | 82.5 ms: 1.07x faster                                                |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.06x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.55 ms: 1.03x faster                                                |
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                |
| regex_dna      | 221 ms                                                     | 226 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                         |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                               |
| xml_etree_parse      | 162 ms                                                     | 150 ms: 1.08x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.07x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 82.2 ms: 1.06x faster                                                |
| xml_etree_process    | 61.2 ms                                                    | 59.0 ms: 1.04x faster                                                |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                |
| pickle_pure_python   | 305 us                                                     | 297 us: 1.03x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 222 us: 1.02x slower                                                 |
| unpickle_list        | 5.34 us                                                    | 5.44 us: 1.02x slower                                                |
| unpickle             | 15.1 us                                                    | 15.5 us: 1.03x slower                                                |
| pickle_dict          | 34.8 us                                                    | 36.4 us: 1.05x slower                                                |
| pickle               | 11.5 us                                                    | 12.0 us: 1.05x slower                                                |
| pickle_list          | 5.11 us                                                    | 5.39 us: 1.06x slower                                                |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                         |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.8 ms: 1.00x slower                                                |
| python_startup_no_site | 7.11 ms                                                    | 7.20 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                      | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.83 ms: 1.14x faster                                                |
| genshi_text     | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                |
| django_template | 34.8 ms                                                    | 36.5 ms: 1.05x slower                                                |
| genshi_xml      | 51.6 ms                                                    | 58.2 ms: 1.13x slower                                                |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                         |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|--------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| scimark_fft              | 392 ms                                                     | 318 ms: 1.24x faster                                                 |
| richards                 | 50.9 ms                                                    | 41.8 ms: 1.22x faster                                                |
| richards_super           | 57.4 ms                                                    | 47.3 ms: 1.21x faster                                                |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.41 ms: 1.19x faster                                                |
| spectral_norm            | 116 ms                                                     | 101 ms: 1.15x faster                                                 |
| crypto_pyaes             | 77.5 ms                                                    | 67.7 ms: 1.14x faster                                                |
| mako                     | 11.2 ms                                                    | 9.83 ms: 1.14x faster                                                |
| fannkuch                 | 402 ms                                                     | 358 ms: 1.12x faster                                                 |
| tomli_loads              | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                               |
| scimark_monte_carlo      | 69.2 ms                                                    | 62.8 ms: 1.10x faster                                                |
| float                    | 78.9 ms                                                    | 72.3 ms: 1.09x faster                                                |
| mdp                      | 2.79 sec                                                   | 2.58 sec: 1.08x faster                                               |
| xml_etree_parse          | 162 ms                                                     | 150 ms: 1.08x faster                                                 |
| pprint_pformat           | 1.56 sec                                                   | 1.45 sec: 1.07x faster                                               |
| pprint_safe_repr         | 758 ms                                                     | 709 ms: 1.07x faster                                                 |
| nbody                    | 88.3 ms                                                    | 82.5 ms: 1.07x faster                                                |
| xml_etree_iterparse      | 107 ms                                                     | 101 ms: 1.07x faster                                                 |
| pathlib                  | 17.3 ms                                                    | 16.3 ms: 1.06x faster                                                |
| xml_etree_generate       | 87.4 ms                                                    | 82.2 ms: 1.06x faster                                                |
| pyflate                  | 484 ms                                                     | 456 ms: 1.06x faster                                                 |
| deepcopy_memo            | 39.7 us                                                    | 37.8 us: 1.05x faster                                                |
| sqlite_synth             | 2.99 us                                                    | 2.86 us: 1.05x faster                                                |
| xml_etree_process        | 61.2 ms                                                    | 59.0 ms: 1.04x faster                                                |
| telco                    | 8.41 ms                                                    | 8.12 ms: 1.04x faster                                                |
| json_dumps               | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                |
| regex_effbot             | 3.67 ms                                                    | 3.55 ms: 1.03x faster                                                |
| pickle_pure_python       | 305 us                                                     | 297 us: 1.03x faster                                                 |
| logging_format           | 6.47 us                                                    | 6.29 us: 1.03x faster                                                |
| regex_v8                 | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                |
| chaos                    | 61.3 ms                                                    | 60.0 ms: 1.02x faster                                                |
| coroutines               | 23.2 ms                                                    | 22.8 ms: 1.02x faster                                                |
| pidigits                 | 191 ms                                                     | 188 ms: 1.02x faster                                                 |
| deepcopy_reduce          | 3.35 us                                                    | 3.30 us: 1.02x faster                                                |
| meteor_contest           | 110 ms                                                     | 108 ms: 1.01x faster                                                 |
| logging_simple           | 5.74 us                                                    | 5.67 us: 1.01x faster                                                |
| pycparser                | 1.16 sec                                                   | 1.14 sec: 1.01x faster                                               |
| sqlglot_parse            | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                |
| thrift                   | 823 us                                                     | 819 us: 1.01x faster                                                 |
| create_gc_cycles         | 1.82 ms                                                    | 1.81 ms: 1.00x faster                                                |
| python_startup           | 10.8 ms                                                    | 10.8 ms: 1.00x slower                                                |
| sqlglot_transpile        | 1.63 ms                                                    | 1.64 ms: 1.01x slower                                                |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                               |
| 2to3                     | 274 ms                                                     | 277 ms: 1.01x slower                                                 |
| python_startup_no_site   | 7.11 ms                                                    | 7.20 ms: 1.01x slower                                                |
| logging_silent           | 105 ns                                                     | 106 ns: 1.01x slower                                                 |
| dask                     | 369 ms                                                     | 376 ms: 1.02x slower                                                 |
| html5lib                 | 67.2 ms                                                    | 68.5 ms: 1.02x slower                                                |
| unpickle_pure_python     | 218 us                                                     | 222 us: 1.02x slower                                                 |
| unpickle_list            | 5.34 us                                                    | 5.44 us: 1.02x slower                                                |
| go                       | 145 ms                                                     | 147 ms: 1.02x slower                                                 |
| regex_dna                | 221 ms                                                     | 226 ms: 1.02x slower                                                 |
| dulwich_log              | 67.2 ms                                                    | 68.6 ms: 1.02x slower                                                |
| asyncio_tcp              | 508 ms                                                     | 519 ms: 1.02x slower                                                 |
| gc_traversal             | 3.98 ms                                                    | 4.06 ms: 1.02x slower                                                |
| sqlglot_optimize         | 55.5 ms                                                    | 56.8 ms: 1.02x slower                                                |
| tornado_http             | 94.6 ms                                                    | 96.9 ms: 1.02x slower                                                |
| sqlglot_normalize        | 110 ms                                                     | 113 ms: 1.02x slower                                                 |
| unpickle                 | 15.1 us                                                    | 15.5 us: 1.03x slower                                                |
| scimark_lu               | 122 ms                                                     | 125 ms: 1.03x slower                                                 |
| async_tree_cpu_io_mixed  | 611 ms                                                     | 631 ms: 1.03x slower                                                 |
| docutils                 | 2.83 sec                                                   | 2.93 sec: 1.04x slower                                               |
| async_tree_io            | 939 ms                                                     | 972 ms: 1.04x slower                                                 |
| generators               | 29.6 ms                                                    | 30.8 ms: 1.04x slower                                                |
| raytrace                 | 267 ms                                                     | 277 ms: 1.04x slower                                                 |
| async_tree_memoization   | 463 ms                                                     | 482 ms: 1.04x slower                                                 |
| pickle_dict              | 34.8 us                                                    | 36.4 us: 1.05x slower                                                |
| pickle                   | 11.5 us                                                    | 12.0 us: 1.05x slower                                                |
| genshi_text              | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                |
| typing_runtime_protocols | 165 us                                                     | 173 us: 1.05x slower                                                 |
| django_template          | 34.8 ms                                                    | 36.5 ms: 1.05x slower                                                |
| async_generators         | 442 ms                                                     | 464 ms: 1.05x slower                                                 |
| bench_thread_pool        | 834 us                                                     | 876 us: 1.05x slower                                                 |
| hexiom                   | 6.30 ms                                                    | 6.63 ms: 1.05x slower                                                |
| pickle_list              | 5.11 us                                                    | 5.39 us: 1.06x slower                                                |
| nqueens                  | 81.4 ms                                                    | 86.2 ms: 1.06x slower                                                |
| sympy_str                | 282 ms                                                     | 299 ms: 1.06x slower                                                 |
| sympy_expand             | 473 ms                                                     | 507 ms: 1.07x slower                                                 |
| scimark_sor              | 127 ms                                                     | 137 ms: 1.07x slower                                                 |
| sympy_sum                | 156 ms                                                     | 171 ms: 1.10x slower                                                 |
| sympy_integrate          | 20.5 ms                                                    | 22.5 ms: 1.10x slower                                                |
| pylint                   | 317 ms                                                     | 352 ms: 1.11x slower                                                 |
| genshi_xml               | 51.6 ms                                                    | 58.2 ms: 1.13x slower                                                |
| deltablue                | 3.25 ms                                                    | 3.73 ms: 1.15x slower                                                |
| Geometric mean           | (ref)                                                      | 1.01x faster                                                         |

Benchmark hidden because not significant (13): async_tree_io_tg, coverage, regex_compile, async_tree_none, async_tree_memoization_tg, asyncio_websockets, comprehensions, json_loads, deepcopy, json, bench_mp_pool, async_tree_cpu_io_mixed_tg, async_tree_none_tg
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 56.82% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x