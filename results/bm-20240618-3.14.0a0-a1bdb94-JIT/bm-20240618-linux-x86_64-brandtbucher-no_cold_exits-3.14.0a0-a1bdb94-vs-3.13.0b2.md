# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-x86_64
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.01x faster
- HPT reliability: 51.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 279 ms: 1.02x slower                                                 |
| html5lib       | 67.2 ms                                                    | 68.9 ms: 1.02x slower                                                |
| tornado_http   | 94.6 ms                                                    | 96.3 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                      | 1.02x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|---------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_cpu_io_mixed   | 611 ms                                                     | 629 ms: 1.03x slower                                                 |
| async_tree_memoization_tg | 444 ms                                                     | 461 ms: 1.04x slower                                                 |
| async_tree_memoization    | 463 ms                                                     | 486 ms: 1.05x slower                                                 |
| async_tree_io_tg          | 936 ms                                                     | 1.00 sec: 1.07x slower                                               |
| Geometric mean            | (ref)                                                      | 1.02x slower                                                         |

Benchmark hidden because not significant (4): async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.8 ms: 1.10x faster                                                |
| nbody          | 88.3 ms                                                    | 82.2 ms: 1.07x faster                                                |
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.06x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                                 |
| regex_v8       | 25.1 ms                                                    | 26.4 ms: 1.05x slower                                                |
| regex_dna      | 221 ms                                                     | 236 ms: 1.07x slower                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.99 ms: 1.09x slower                                                |
| Geometric mean | (ref)                                                      | 1.05x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.09x faster                                                 |
| tomli_loads          | 2.12 sec                                                   | 1.97 sec: 1.08x faster                                               |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.07x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 82.7 ms: 1.06x faster                                                |
| xml_etree_process    | 61.2 ms                                                    | 59.3 ms: 1.03x faster                                                |
| unpickle_list        | 5.34 us                                                    | 5.20 us: 1.03x faster                                                |
| pickle_pure_python   | 305 us                                                     | 297 us: 1.03x faster                                                 |
| unpickle             | 15.1 us                                                    | 14.8 us: 1.02x faster                                                |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                |
| unpickle_pure_python | 218 us                                                     | 222 us: 1.02x slower                                                 |
| pickle_list          | 5.11 us                                                    | 5.29 us: 1.04x slower                                                |
| pickle               | 11.5 us                                                    | 11.9 us: 1.04x slower                                                |
| pickle_dict          | 34.8 us                                                    | 36.1 us: 1.04x slower                                                |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                         |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.8 ms: 1.00x slower                                                |
| python_startup_no_site | 7.11 ms                                                    | 7.25 ms: 1.02x slower                                                |
| Geometric mean         | (ref)                                                      | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.92 ms: 1.13x faster                                                |
| genshi_text     | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                |
| django_template | 34.8 ms                                                    | 37.0 ms: 1.06x slower                                                |
| genshi_xml      | 51.6 ms                                                    | 58.2 ms: 1.13x slower                                                |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                         |

All benchmarks:
===============

| Benchmark                 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|---------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo             | 39.7 us                                                    | 29.0 us: 1.37x faster                                                |
| deepcopy                  | 367 us                                                     | 276 us: 1.33x faster                                                 |
| deepcopy_reduce           | 3.35 us                                                    | 2.73 us: 1.23x faster                                                |
| scimark_fft               | 392 ms                                                     | 326 ms: 1.21x faster                                                 |
| richards                  | 50.9 ms                                                    | 42.6 ms: 1.20x faster                                                |
| richards_super            | 57.4 ms                                                    | 48.3 ms: 1.19x faster                                                |
| scimark_sparse_mat_mult   | 5.27 ms                                                    | 4.57 ms: 1.15x faster                                                |
| mako                      | 11.2 ms                                                    | 9.92 ms: 1.13x faster                                                |
| crypto_pyaes              | 77.5 ms                                                    | 68.5 ms: 1.13x faster                                                |
| fannkuch                  | 402 ms                                                     | 359 ms: 1.12x faster                                                 |
| scimark_monte_carlo       | 69.2 ms                                                    | 62.6 ms: 1.11x faster                                                |
| float                     | 78.9 ms                                                    | 71.8 ms: 1.10x faster                                                |
| spectral_norm             | 116 ms                                                     | 106 ms: 1.10x faster                                                 |
| xml_etree_parse           | 162 ms                                                     | 148 ms: 1.09x faster                                                 |
| mdp                       | 2.79 sec                                                   | 2.58 sec: 1.08x faster                                               |
| tomli_loads               | 2.12 sec                                                   | 1.97 sec: 1.08x faster                                               |
| nbody                     | 88.3 ms                                                    | 82.2 ms: 1.07x faster                                                |
| xml_etree_iterparse       | 107 ms                                                     | 101 ms: 1.07x faster                                                 |
| pprint_pformat            | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                               |
| xml_etree_generate        | 87.4 ms                                                    | 82.7 ms: 1.06x faster                                                |
| pathlib                   | 17.3 ms                                                    | 16.4 ms: 1.06x faster                                                |
| pyflate                   | 484 ms                                                     | 459 ms: 1.05x faster                                                 |
| pprint_safe_repr          | 758 ms                                                     | 720 ms: 1.05x faster                                                 |
| sqlite_synth              | 2.99 us                                                    | 2.85 us: 1.05x faster                                                |
| telco                     | 8.41 ms                                                    | 8.04 ms: 1.05x faster                                                |
| logging_format            | 6.47 us                                                    | 6.23 us: 1.04x faster                                                |
| logging_simple            | 5.74 us                                                    | 5.54 us: 1.04x faster                                                |
| bpe_tokeniser             | 5.02 sec                                                   | 4.86 sec: 1.03x faster                                               |
| xml_etree_process         | 61.2 ms                                                    | 59.3 ms: 1.03x faster                                                |
| unpickle_list             | 5.34 us                                                    | 5.20 us: 1.03x faster                                                |
| pickle_pure_python        | 305 us                                                     | 297 us: 1.03x faster                                                 |
| chaos                     | 61.3 ms                                                    | 60.0 ms: 1.02x faster                                                |
| unpickle                  | 15.1 us                                                    | 14.8 us: 1.02x faster                                                |
| json_dumps                | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                |
| create_gc_cycles          | 1.82 ms                                                    | 1.79 ms: 1.02x faster                                                |
| coroutines                | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                |
| gc_traversal              | 3.98 ms                                                    | 3.92 ms: 1.01x faster                                                |
| pidigits                  | 191 ms                                                     | 189 ms: 1.01x faster                                                 |
| meteor_contest            | 110 ms                                                     | 109 ms: 1.00x faster                                                 |
| python_startup            | 10.8 ms                                                    | 10.8 ms: 1.00x slower                                                |
| asyncio_tcp_ssl           | 1.84 sec                                                   | 1.85 sec: 1.01x slower                                               |
| regex_compile             | 137 ms                                                     | 138 ms: 1.01x slower                                                 |
| thrift                    | 823 us                                                     | 830 us: 1.01x slower                                                 |
| comprehensions            | 16.6 us                                                    | 16.8 us: 1.01x slower                                                |
| sqlglot_transpile         | 1.63 ms                                                    | 1.65 ms: 1.01x slower                                                |
| pycparser                 | 1.16 sec                                                   | 1.17 sec: 1.01x slower                                               |
| generators                | 29.6 ms                                                    | 30.0 ms: 1.01x slower                                                |
| tornado_http              | 94.6 ms                                                    | 96.3 ms: 1.02x slower                                                |
| asyncio_tcp               | 508 ms                                                     | 517 ms: 1.02x slower                                                 |
| dask                      | 369 ms                                                     | 376 ms: 1.02x slower                                                 |
| unpickle_pure_python      | 218 us                                                     | 222 us: 1.02x slower                                                 |
| bench_thread_pool         | 834 us                                                     | 850 us: 1.02x slower                                                 |
| 2to3                      | 274 ms                                                     | 279 ms: 1.02x slower                                                 |
| python_startup_no_site    | 7.11 ms                                                    | 7.25 ms: 1.02x slower                                                |
| typing_runtime_protocols  | 165 us                                                     | 168 us: 1.02x slower                                                 |
| coverage                  | 93.1 ms                                                    | 95.2 ms: 1.02x slower                                                |
| dulwich_log               | 67.2 ms                                                    | 68.8 ms: 1.02x slower                                                |
| html5lib                  | 67.2 ms                                                    | 68.9 ms: 1.02x slower                                                |
| go                        | 145 ms                                                     | 148 ms: 1.02x slower                                                 |
| sqlglot_optimize          | 55.5 ms                                                    | 57.1 ms: 1.03x slower                                                |
| async_tree_cpu_io_mixed   | 611 ms                                                     | 629 ms: 1.03x slower                                                 |
| scimark_lu                | 122 ms                                                     | 125 ms: 1.03x slower                                                 |
| logging_silent            | 105 ns                                                     | 108 ns: 1.03x slower                                                 |
| raytrace                  | 267 ms                                                     | 275 ms: 1.03x slower                                                 |
| nqueens                   | 81.4 ms                                                    | 84.3 ms: 1.04x slower                                                |
| pickle_list               | 5.11 us                                                    | 5.29 us: 1.04x slower                                                |
| pickle                    | 11.5 us                                                    | 11.9 us: 1.04x slower                                                |
| async_tree_memoization_tg | 444 ms                                                     | 461 ms: 1.04x slower                                                 |
| pickle_dict               | 34.8 us                                                    | 36.1 us: 1.04x slower                                                |
| sqlglot_normalize         | 110 ms                                                     | 115 ms: 1.04x slower                                                 |
| async_tree_memoization    | 463 ms                                                     | 486 ms: 1.05x slower                                                 |
| regex_v8                  | 25.1 ms                                                    | 26.4 ms: 1.05x slower                                                |
| async_generators          | 442 ms                                                     | 465 ms: 1.05x slower                                                 |
| genshi_text               | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                |
| django_template           | 34.8 ms                                                    | 37.0 ms: 1.06x slower                                                |
| hexiom                    | 6.30 ms                                                    | 6.72 ms: 1.07x slower                                                |
| regex_dna                 | 221 ms                                                     | 236 ms: 1.07x slower                                                 |
| async_tree_io_tg          | 936 ms                                                     | 1.00 sec: 1.07x slower                                               |
| sympy_str                 | 282 ms                                                     | 303 ms: 1.07x slower                                                 |
| sympy_expand              | 473 ms                                                     | 512 ms: 1.08x slower                                                 |
| regex_effbot              | 3.67 ms                                                    | 3.99 ms: 1.09x slower                                                |
| sympy_sum                 | 156 ms                                                     | 171 ms: 1.10x slower                                                 |
| scimark_sor               | 127 ms                                                     | 140 ms: 1.10x slower                                                 |
| sympy_integrate           | 20.5 ms                                                    | 22.7 ms: 1.11x slower                                                |
| pylint                    | 317 ms                                                     | 353 ms: 1.11x slower                                                 |
| deltablue                 | 3.25 ms                                                    | 3.63 ms: 1.12x slower                                                |
| genshi_xml                | 51.6 ms                                                    | 58.2 ms: 1.13x slower                                                |
| Geometric mean            | (ref)                                                      | 1.01x faster                                                         |

Benchmark hidden because not significant (9): async_tree_none, json_loads, sqlglot_parse, asyncio_websockets, async_tree_cpu_io_mixed_tg, bench_mp_pool, async_tree_io, json, async_tree_none_tg
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, docutils, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 51.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x