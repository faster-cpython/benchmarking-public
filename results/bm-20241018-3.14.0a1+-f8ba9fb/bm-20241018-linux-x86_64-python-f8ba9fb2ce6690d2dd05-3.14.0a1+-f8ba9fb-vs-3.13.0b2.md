# Results vs. 3.13.0b2

- fork: python
- ref: f8ba9fb2ce6690d2dd05
- machine: linux-x86_64
- commit hash: f8ba9fb
- commit date: 2024-10-18
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 254 ms: 1.08x faster                                                   |
| docutils       | 2.83 sec                                                   | 2.68 sec: 1.06x faster                                                 |
| html5lib       | 67.2 ms                                                    | 63.6 ms: 1.06x faster                                                  |
| tornado_http   | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                      | 1.06x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 376 ms: 1.18x faster                                                   |
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 415 ms: 1.12x faster                                                   |
| async_tree_io              | 939 ms                                                     | 851 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 575 ms: 1.06x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 320 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 563 ms: 1.04x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 975 ms: 1.04x slower                                                   |
| Geometric mean             | (ref)                                                      | 1.08x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                   |
| float          | 78.9 ms                                                    | 79.9 ms: 1.01x slower                                                  |
| nbody          | 88.3 ms                                                    | 93.0 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 130 ms: 1.05x faster                                                   |
| regex_dna      | 221 ms                                                     | 218 ms: 1.01x faster                                                   |
| regex_effbot   | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 26.4 us: 1.10x faster                                                  |
| xml_etree_parse      | 162 ms                                                     | 155 ms: 1.04x faster                                                   |
| unpickle             | 15.1 us                                                    | 14.6 us: 1.04x faster                                                  |
| pickle_dict          | 34.8 us                                                    | 33.9 us: 1.03x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.02x faster                                                   |
| xml_etree_process    | 61.2 ms                                                    | 59.7 ms: 1.02x faster                                                  |
| xml_etree_generate   | 87.4 ms                                                    | 86.1 ms: 1.02x faster                                                  |
| unpickle_pure_python | 218 us                                                     | 218 us: 1.00x faster                                                   |
| pickle_list          | 5.11 us                                                    | 5.21 us: 1.02x slower                                                  |
| pickle_pure_python   | 305 us                                                     | 313 us: 1.02x slower                                                   |
| unpickle_list        | 5.34 us                                                    | 5.57 us: 1.04x slower                                                  |
| json_dumps           | 10.7 ms                                                    | 11.3 ms: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (2): tomli_loads, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                    | 7.03 ms: 1.01x faster                                                  |
| python_startup         | 10.8 ms                                                    | 11.8 ms: 1.10x slower                                                  |
| Geometric mean         | (ref)                                                      | 1.04x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                                  |
| genshi_text     | 23.7 ms                                                    | 23.2 ms: 1.02x faster                                                  |
| genshi_xml      | 51.6 ms                                                    | 51.2 ms: 1.01x faster                                                  |
| mako            | 11.2 ms                                                    | 11.7 ms: 1.04x slower                                                  |
| Geometric mean  | (ref)                                                      | 1.00x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 264 us: 1.39x faster                                                   |
| deepcopy_memo              | 39.7 us                                                    | 31.1 us: 1.28x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 2.74 us: 1.22x faster                                                  |
| go                         | 145 ms                                                     | 120 ms: 1.20x faster                                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 376 ms: 1.18x faster                                                   |
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 415 ms: 1.12x faster                                                   |
| richards                   | 50.9 ms                                                    | 45.7 ms: 1.11x faster                                                  |
| richards_super             | 57.4 ms                                                    | 52.0 ms: 1.10x faster                                                  |
| async_tree_io              | 939 ms                                                     | 851 ms: 1.10x faster                                                   |
| coverage                   | 93.1 ms                                                    | 84.8 ms: 1.10x faster                                                  |
| json_loads                 | 28.9 us                                                    | 26.4 us: 1.10x faster                                                  |
| json                       | 5.31 ms                                                    | 4.87 ms: 1.09x faster                                                  |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                  |
| 2to3                       | 274 ms                                                     | 254 ms: 1.08x faster                                                   |
| generators                 | 29.6 ms                                                    | 27.8 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 575 ms: 1.06x faster                                                   |
| thrift                     | 823 us                                                     | 775 us: 1.06x faster                                                   |
| sympy_str                  | 282 ms                                                     | 266 ms: 1.06x faster                                                   |
| sympy_sum                  | 156 ms                                                     | 147 ms: 1.06x faster                                                   |
| dulwich_log                | 67.2 ms                                                    | 63.4 ms: 1.06x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.63 sec: 1.06x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 63.6 ms: 1.06x faster                                                  |
| docutils                   | 2.83 sec                                                   | 2.68 sec: 1.06x faster                                                 |
| regex_compile              | 137 ms                                                     | 130 ms: 1.05x faster                                                   |
| asyncio_tcp                | 508 ms                                                     | 484 ms: 1.05x faster                                                   |
| scimark_lu                 | 122 ms                                                     | 116 ms: 1.05x faster                                                   |
| crypto_pyaes               | 77.5 ms                                                    | 73.8 ms: 1.05x faster                                                  |
| telco                      | 8.41 ms                                                    | 8.02 ms: 1.05x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 320 ms: 1.05x faster                                                   |
| tornado_http               | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                                  |
| scimark_fft                | 392 ms                                                     | 374 ms: 1.05x faster                                                   |
| pprint_pformat             | 1.56 sec                                                   | 1.49 sec: 1.05x faster                                                 |
| sympy_expand               | 473 ms                                                     | 452 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 563 ms: 1.04x faster                                                   |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.05 ms: 1.04x faster                                                  |
| xml_etree_parse            | 162 ms                                                     | 155 ms: 1.04x faster                                                   |
| sqlglot_optimize           | 55.5 ms                                                    | 53.2 ms: 1.04x faster                                                  |
| logging_format             | 6.47 us                                                    | 6.21 us: 1.04x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.82 sec: 1.04x faster                                                 |
| pprint_safe_repr           | 758 ms                                                     | 729 ms: 1.04x faster                                                   |
| sqlglot_normalize          | 110 ms                                                     | 106 ms: 1.04x faster                                                   |
| unpickle                   | 15.1 us                                                    | 14.6 us: 1.04x faster                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.03x faster                                                  |
| sympy_integrate            | 20.5 ms                                                    | 19.8 ms: 1.03x faster                                                  |
| logging_simple             | 5.74 us                                                    | 5.57 us: 1.03x faster                                                  |
| pyflate                    | 484 ms                                                     | 470 ms: 1.03x faster                                                   |
| django_template            | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                                  |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                  |
| sqlite_synth               | 2.99 us                                                    | 2.91 us: 1.03x faster                                                  |
| pickle_dict                | 34.8 us                                                    | 33.9 us: 1.03x faster                                                  |
| async_generators           | 442 ms                                                     | 431 ms: 1.03x faster                                                   |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.02x faster                                                   |
| xml_etree_process          | 61.2 ms                                                    | 59.7 ms: 1.02x faster                                                  |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                   |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                   |
| genshi_text                | 23.7 ms                                                    | 23.2 ms: 1.02x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                   |
| xml_etree_generate         | 87.4 ms                                                    | 86.1 ms: 1.02x faster                                                  |
| typing_runtime_protocols   | 165 us                                                     | 163 us: 1.01x faster                                                   |
| regex_dna                  | 221 ms                                                     | 218 ms: 1.01x faster                                                   |
| python_startup_no_site     | 7.11 ms                                                    | 7.03 ms: 1.01x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.6 ms: 1.01x faster                                                  |
| genshi_xml                 | 51.6 ms                                                    | 51.2 ms: 1.01x faster                                                  |
| logging_silent             | 105 ns                                                     | 104 ns: 1.01x faster                                                   |
| chaos                      | 61.3 ms                                                    | 61.0 ms: 1.01x faster                                                  |
| unpickle_pure_python       | 218 us                                                     | 218 us: 1.00x faster                                                   |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.00x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 81.7 ms: 1.00x slower                                                  |
| scimark_sor                | 127 ms                                                     | 128 ms: 1.01x slower                                                   |
| pycparser                  | 1.16 sec                                                   | 1.17 sec: 1.01x slower                                                 |
| hexiom                     | 6.30 ms                                                    | 6.37 ms: 1.01x slower                                                  |
| raytrace                   | 267 ms                                                     | 270 ms: 1.01x slower                                                   |
| float                      | 78.9 ms                                                    | 79.9 ms: 1.01x slower                                                  |
| spectral_norm              | 116 ms                                                     | 118 ms: 1.01x slower                                                   |
| bench_thread_pool          | 834 us                                                     | 846 us: 1.01x slower                                                   |
| pickle_list                | 5.11 us                                                    | 5.21 us: 1.02x slower                                                  |
| deltablue                  | 3.25 ms                                                    | 3.32 ms: 1.02x slower                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                  |
| pickle_pure_python         | 305 us                                                     | 313 us: 1.02x slower                                                   |
| fannkuch                   | 402 ms                                                     | 414 ms: 1.03x slower                                                   |
| async_tree_io_tg           | 936 ms                                                     | 975 ms: 1.04x slower                                                   |
| unpickle_list              | 5.34 us                                                    | 5.57 us: 1.04x slower                                                  |
| mako                       | 11.2 ms                                                    | 11.7 ms: 1.04x slower                                                  |
| nbody                      | 88.3 ms                                                    | 93.0 ms: 1.05x slower                                                  |
| json_dumps                 | 10.7 ms                                                    | 11.3 ms: 1.05x slower                                                  |
| python_startup             | 10.8 ms                                                    | 11.8 ms: 1.10x slower                                                  |
| gc_traversal               | 3.98 ms                                                    | 4.73 ms: 1.19x slower                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 2.70 ms: 1.49x slower                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 78.0 ms: 3.27x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.02x faster                                                           |

Benchmark hidden because not significant (5): tomli_loads, pickle, regex_v8, pylint, coroutines
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241018-3.14.0a1+-f8ba9fb/bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.12x