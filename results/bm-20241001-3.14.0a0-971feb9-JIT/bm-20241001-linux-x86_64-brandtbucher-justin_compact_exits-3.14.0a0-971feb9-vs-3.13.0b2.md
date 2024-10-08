# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: 971feb9
- commit date: 2024-10-01
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 277 ms: 1.01x slower                                                        |
| html5lib       | 67.2 ms                                                    | 62.7 ms: 1.07x faster                                                       |
| tornado_http   | 94.6 ms                                                    | 94.1 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 405 ms: 1.14x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 314 ms: 1.07x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 883 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 558 ms: 1.05x faster                                                        |
| async_tree_io              | 939 ms                                                     | 892 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.4 ms: 1.11x faster                                                       |
| nbody          | 88.3 ms                                                    | 82.8 ms: 1.07x faster                                                       |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 217 ms: 1.02x faster                                                        |
| regex_effbot   | 3.67 ms                                                    | 3.61 ms: 1.02x faster                                                       |
| regex_compile  | 137 ms                                                     | 140 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                      | 1.00x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 76.7 ms: 1.14x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 54.1 ms: 1.13x faster                                                       |
| tomli_loads          | 2.12 sec                                                   | 1.88 sec: 1.13x faster                                                      |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                     | 98.7 ms: 1.09x faster                                                       |
| json_loads           | 28.9 us                                                    | 26.8 us: 1.08x faster                                                       |
| json_dumps           | 10.7 ms                                                    | 10.1 ms: 1.07x faster                                                       |
| unpickle             | 15.1 us                                                    | 14.6 us: 1.04x faster                                                       |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                                        |
| pickle_dict          | 34.8 us                                                    | 34.1 us: 1.02x faster                                                       |
| unpickle_list        | 5.34 us                                                    | 5.25 us: 1.02x faster                                                       |
| pickle_list          | 5.11 us                                                    | 5.06 us: 1.01x faster                                                       |
| pickle_pure_python   | 305 us                                                     | 307 us: 1.00x slower                                                        |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.79 ms: 1.15x faster                                                       |
| django_template | 34.8 ms                                                    | 35.4 ms: 1.02x slower                                                       |
| genshi_text     | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 57.7 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| richards                   | 50.9 ms                                                    | 32.7 ms: 1.55x faster                                                       |
| richards_super             | 57.4 ms                                                    | 38.5 ms: 1.49x faster                                                       |
| deepcopy_memo              | 39.7 us                                                    | 26.8 us: 1.48x faster                                                       |
| deepcopy                   | 367 us                                                     | 261 us: 1.40x faster                                                        |
| scimark_fft                | 392 ms                                                     | 307 ms: 1.28x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                    | 2.66 us: 1.26x faster                                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.40 ms: 1.20x faster                                                       |
| crypto_pyaes               | 77.5 ms                                                    | 64.9 ms: 1.19x faster                                                       |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                        |
| mako                       | 11.2 ms                                                    | 9.79 ms: 1.15x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 405 ms: 1.14x faster                                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.39 sec: 1.14x faster                                                      |
| xml_etree_generate         | 87.4 ms                                                    | 76.7 ms: 1.14x faster                                                       |
| go                         | 145 ms                                                     | 127 ms: 1.13x faster                                                        |
| xml_etree_process          | 61.2 ms                                                    | 54.1 ms: 1.13x faster                                                       |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.13x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                        |
| tomli_loads                | 2.12 sec                                                   | 1.88 sec: 1.13x faster                                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.2 ms: 1.11x faster                                                       |
| pathlib                    | 17.3 ms                                                    | 15.6 ms: 1.11x faster                                                       |
| float                      | 78.9 ms                                                    | 71.4 ms: 1.11x faster                                                       |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.10x faster                                                        |
| telco                      | 8.41 ms                                                    | 7.63 ms: 1.10x faster                                                       |
| mdp                        | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                                      |
| pyflate                    | 484 ms                                                     | 441 ms: 1.10x faster                                                        |
| fannkuch                   | 402 ms                                                     | 366 ms: 1.10x faster                                                        |
| pprint_safe_repr           | 758 ms                                                     | 691 ms: 1.10x faster                                                        |
| sqlite_synth               | 2.99 us                                                    | 2.74 us: 1.09x faster                                                       |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.09x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                     | 98.7 ms: 1.09x faster                                                       |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                        |
| coverage                   | 93.1 ms                                                    | 85.9 ms: 1.08x faster                                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.44 sec: 1.08x faster                                                      |
| json_loads                 | 28.9 us                                                    | 26.8 us: 1.08x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                        |
| html5lib                   | 67.2 ms                                                    | 62.7 ms: 1.07x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 314 ms: 1.07x faster                                                        |
| nbody                      | 88.3 ms                                                    | 82.8 ms: 1.07x faster                                                       |
| json_dumps                 | 10.7 ms                                                    | 10.1 ms: 1.07x faster                                                       |
| async_tree_io_tg           | 936 ms                                                     | 883 ms: 1.06x faster                                                        |
| logging_format             | 6.47 us                                                    | 6.11 us: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 558 ms: 1.05x faster                                                        |
| async_tree_io              | 939 ms                                                     | 892 ms: 1.05x faster                                                        |
| asyncio_tcp                | 508 ms                                                     | 484 ms: 1.05x faster                                                        |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                                       |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.05x faster                                                        |
| json                       | 5.31 ms                                                    | 5.10 ms: 1.04x faster                                                       |
| thrift                     | 823 us                                                     | 791 us: 1.04x faster                                                        |
| deltablue                  | 3.25 ms                                                    | 3.13 ms: 1.04x faster                                                       |
| unpickle                   | 15.1 us                                                    | 14.6 us: 1.04x faster                                                       |
| chaos                      | 61.3 ms                                                    | 59.3 ms: 1.03x faster                                                       |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                        |
| comprehensions             | 16.6 us                                                    | 16.2 us: 1.03x faster                                                       |
| gc_traversal               | 3.98 ms                                                    | 3.88 ms: 1.02x faster                                                       |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                                        |
| logging_simple             | 5.74 us                                                    | 5.62 us: 1.02x faster                                                       |
| regex_dna                  | 221 ms                                                     | 217 ms: 1.02x faster                                                        |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                        |
| pickle_dict                | 34.8 us                                                    | 34.1 us: 1.02x faster                                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                       |
| unpickle_list              | 5.34 us                                                    | 5.25 us: 1.02x faster                                                       |
| regex_effbot               | 3.67 ms                                                    | 3.61 ms: 1.02x faster                                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                       |
| pickle_list                | 5.11 us                                                    | 5.06 us: 1.01x faster                                                       |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                                       |
| tornado_http               | 94.6 ms                                                    | 94.1 ms: 1.01x faster                                                       |
| python_startup_no_site     | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                       |
| pickle_pure_python         | 305 us                                                     | 307 us: 1.00x slower                                                        |
| dulwich_log                | 67.2 ms                                                    | 67.6 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.65 ms: 1.01x slower                                                       |
| 2to3                       | 274 ms                                                     | 277 ms: 1.01x slower                                                        |
| django_template            | 34.8 ms                                                    | 35.4 ms: 1.02x slower                                                       |
| regex_compile              | 137 ms                                                     | 140 ms: 1.02x slower                                                        |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.02x slower                                                        |
| raytrace                   | 267 ms                                                     | 274 ms: 1.03x slower                                                        |
| pickle                     | 11.5 us                                                    | 11.8 us: 1.03x slower                                                       |
| async_generators           | 442 ms                                                     | 461 ms: 1.04x slower                                                        |
| sympy_str                  | 282 ms                                                     | 298 ms: 1.05x slower                                                        |
| genshi_text                | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                                       |
| sympy_expand               | 473 ms                                                     | 500 ms: 1.06x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 6.67 ms: 1.06x slower                                                       |
| bench_thread_pool          | 834 us                                                     | 891 us: 1.07x slower                                                        |
| nqueens                    | 81.4 ms                                                    | 89.6 ms: 1.10x slower                                                       |
| sympy_integrate            | 20.5 ms                                                    | 22.6 ms: 1.10x slower                                                       |
| genshi_xml                 | 51.6 ms                                                    | 57.7 ms: 1.12x slower                                                       |
| sympy_sum                  | 156 ms                                                     | 177 ms: 1.14x slower                                                        |
| pylint                     | 317 ms                                                     | 364 ms: 1.15x slower                                                        |
| generators                 | 29.6 ms                                                    | 34.1 ms: 1.15x slower                                                       |
| bench_mp_pool              | 23.9 ms                                                    | 60.8 ms: 2.54x slower                                                       |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                |

Benchmark hidden because not significant (4): pycparser, typing_runtime_protocols, logging_silent, regex_v8
Ignored benchmarks (9) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, docutils, flaskblogging, gunicorn, mypy2, sqlglot_optimize
Ignored benchmarks (1) of results/bm-20241001-3.14.0a0-971feb9-JIT/bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x