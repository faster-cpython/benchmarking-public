# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: immortal_ref_count_s
- machine: linux-x86_64
- commit hash: 506492e
- commit date: 2024-09-20
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 254 ms: 1.08x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.65 sec: 1.07x faster                                                          |
| html5lib       | 67.2 ms                                                    | 63.4 ms: 1.06x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 91.1 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                      | 1.06x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 312 ms: 1.21x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 390 ms: 1.19x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                                            |
| async_tree_io              | 939 ms                                                     | 850 ms: 1.10x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 306 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 557 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 547 ms: 1.07x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 875 ms: 1.07x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 76.2 ms: 1.04x faster                                                           |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                            |
| nbody          | 88.3 ms                                                    | 87.7 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 127 ms: 1.07x faster                                                            |
| regex_v8       | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                                           |
| regex_effbot   | 3.67 ms                                                    | 3.66 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 26.6 us: 1.09x faster                                                           |
| xml_etree_process    | 61.2 ms                                                    | 58.5 ms: 1.05x faster                                                           |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                           |
| pickle_dict          | 34.8 us                                                    | 33.5 us: 1.04x faster                                                           |
| xml_etree_generate   | 87.4 ms                                                    | 84.4 ms: 1.04x faster                                                           |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.03x faster                                                            |
| tomli_loads          | 2.12 sec                                                   | 2.06 sec: 1.03x faster                                                          |
| unpickle             | 15.1 us                                                    | 14.7 us: 1.03x faster                                                           |
| pickle               | 11.5 us                                                    | 11.2 us: 1.03x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                     | 106 ms: 1.02x faster                                                            |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                            |
| pickle_list          | 5.11 us                                                    | 5.13 us: 1.00x slower                                                           |
| unpickle_list        | 5.34 us                                                    | 5.40 us: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 6.98 ms: 1.02x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.0 ms: 1.08x faster                                                           |
| genshi_xml      | 51.6 ms                                                    | 50.0 ms: 1.03x faster                                                           |
| django_template | 34.8 ms                                                    | 34.4 ms: 1.01x faster                                                           |
| mako            | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                      | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 259 us: 1.42x faster                                                            |
| deepcopy_memo              | 39.7 us                                                    | 30.0 us: 1.32x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.70 us: 1.24x faster                                                           |
| go                         | 145 ms                                                     | 118 ms: 1.22x faster                                                            |
| async_tree_none            | 378 ms                                                     | 312 ms: 1.21x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 390 ms: 1.19x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                                            |
| richards                   | 50.9 ms                                                    | 46.0 ms: 1.11x faster                                                           |
| async_tree_io              | 939 ms                                                     | 850 ms: 1.10x faster                                                            |
| richards_super             | 57.4 ms                                                    | 52.0 ms: 1.10x faster                                                           |
| mdp                        | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                                          |
| async_tree_none_tg         | 336 ms                                                     | 306 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 557 ms: 1.10x faster                                                            |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.85 ms: 1.09x faster                                                           |
| json_loads                 | 28.9 us                                                    | 26.6 us: 1.09x faster                                                           |
| 2to3                       | 274 ms                                                     | 254 ms: 1.08x faster                                                            |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                           |
| genshi_text                | 23.7 ms                                                    | 22.0 ms: 1.08x faster                                                           |
| regex_compile              | 137 ms                                                     | 127 ms: 1.07x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 547 ms: 1.07x faster                                                            |
| pprint_safe_repr           | 758 ms                                                     | 707 ms: 1.07x faster                                                            |
| json                       | 5.31 ms                                                    | 4.95 ms: 1.07x faster                                                           |
| pprint_pformat             | 1.56 sec                                                   | 1.45 sec: 1.07x faster                                                          |
| crypto_pyaes               | 77.5 ms                                                    | 72.4 ms: 1.07x faster                                                           |
| async_tree_io_tg           | 936 ms                                                     | 875 ms: 1.07x faster                                                            |
| coverage                   | 93.1 ms                                                    | 87.1 ms: 1.07x faster                                                           |
| scimark_fft                | 392 ms                                                     | 368 ms: 1.07x faster                                                            |
| docutils                   | 2.83 sec                                                   | 2.65 sec: 1.07x faster                                                          |
| thrift                     | 823 us                                                     | 773 us: 1.06x faster                                                            |
| scimark_lu                 | 122 ms                                                     | 115 ms: 1.06x faster                                                            |
| html5lib                   | 67.2 ms                                                    | 63.4 ms: 1.06x faster                                                           |
| generators                 | 29.6 ms                                                    | 28.0 ms: 1.06x faster                                                           |
| asyncio_tcp                | 508 ms                                                     | 481 ms: 1.06x faster                                                            |
| sympy_sum                  | 156 ms                                                     | 148 ms: 1.06x faster                                                            |
| sympy_integrate            | 20.5 ms                                                    | 19.5 ms: 1.05x faster                                                           |
| bench_thread_pool          | 834 us                                                     | 792 us: 1.05x faster                                                            |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                                           |
| sympy_str                  | 282 ms                                                     | 269 ms: 1.05x faster                                                            |
| gc_traversal               | 3.98 ms                                                    | 3.79 ms: 1.05x faster                                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 4.79 sec: 1.05x faster                                                          |
| sqlite_synth               | 2.99 us                                                    | 2.86 us: 1.05x faster                                                           |
| xml_etree_process          | 61.2 ms                                                    | 58.5 ms: 1.05x faster                                                           |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                           |
| sqlglot_optimize           | 55.5 ms                                                    | 53.2 ms: 1.04x faster                                                           |
| pickle_dict                | 34.8 us                                                    | 33.5 us: 1.04x faster                                                           |
| tornado_http               | 94.6 ms                                                    | 91.1 ms: 1.04x faster                                                           |
| chaos                      | 61.3 ms                                                    | 59.0 ms: 1.04x faster                                                           |
| logging_format             | 6.47 us                                                    | 6.23 us: 1.04x faster                                                           |
| typing_runtime_protocols   | 165 us                                                     | 159 us: 1.04x faster                                                            |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.04x faster                                                           |
| xml_etree_generate         | 87.4 ms                                                    | 84.4 ms: 1.04x faster                                                           |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                            |
| sqlglot_normalize          | 110 ms                                                     | 106 ms: 1.04x faster                                                            |
| float                      | 78.9 ms                                                    | 76.2 ms: 1.04x faster                                                           |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.03x faster                                                            |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                           |
| genshi_xml                 | 51.6 ms                                                    | 50.0 ms: 1.03x faster                                                           |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.1 ms: 1.03x faster                                                           |
| tomli_loads                | 2.12 sec                                                   | 2.06 sec: 1.03x faster                                                          |
| unpickle                   | 15.1 us                                                    | 14.7 us: 1.03x faster                                                           |
| dulwich_log                | 67.2 ms                                                    | 65.2 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                          |
| spectral_norm              | 116 ms                                                     | 113 ms: 1.03x faster                                                            |
| sympy_expand               | 473 ms                                                     | 460 ms: 1.03x faster                                                            |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                            |
| pickle                     | 11.5 us                                                    | 11.2 us: 1.03x faster                                                           |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| scimark_sor                | 127 ms                                                     | 124 ms: 1.02x faster                                                            |
| async_generators           | 442 ms                                                     | 433 ms: 1.02x faster                                                            |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                            |
| deltablue                  | 3.25 ms                                                    | 3.19 ms: 1.02x faster                                                           |
| pyflate                    | 484 ms                                                     | 474 ms: 1.02x faster                                                            |
| logging_simple             | 5.74 us                                                    | 5.64 us: 1.02x faster                                                           |
| python_startup_no_site     | 7.11 ms                                                    | 6.98 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                     | 106 ms: 1.02x faster                                                            |
| raytrace                   | 267 ms                                                     | 262 ms: 1.02x faster                                                            |
| hexiom                     | 6.30 ms                                                    | 6.21 ms: 1.01x faster                                                           |
| nqueens                    | 81.4 ms                                                    | 80.3 ms: 1.01x faster                                                           |
| logging_silent             | 105 ns                                                     | 103 ns: 1.01x faster                                                            |
| regex_v8                   | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                                           |
| django_template            | 34.8 ms                                                    | 34.4 ms: 1.01x faster                                                           |
| telco                      | 8.41 ms                                                    | 8.32 ms: 1.01x faster                                                           |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                            |
| mako                       | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                                           |
| nbody                      | 88.3 ms                                                    | 87.7 ms: 1.01x faster                                                           |
| fannkuch                   | 402 ms                                                     | 400 ms: 1.00x faster                                                            |
| regex_effbot               | 3.67 ms                                                    | 3.66 ms: 1.00x faster                                                           |
| pickle_list                | 5.11 us                                                    | 5.13 us: 1.00x slower                                                           |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                           |
| unpickle_list              | 5.34 us                                                    | 5.40 us: 1.01x slower                                                           |
| pycparser                  | 1.16 sec                                                   | 1.17 sec: 1.01x slower                                                          |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                    |

Benchmark hidden because not significant (5): regex_dna, comprehensions, pickle_pure_python, coroutines, pylint
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240920-3.14.0a0-506492e/bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.00x