# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: immortal_ref_count_s
- machine: linux-x86_64
- commit hash: e179c31
- commit date: 2024-09-20
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 255 ms: 1.07x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.65 sec: 1.07x faster                                                          |
| html5lib       | 67.2 ms                                                    | 62.2 ms: 1.08x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 89.8 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                      | 1.07x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 310 ms: 1.22x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 391 ms: 1.18x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 385 ms: 1.15x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 297 ms: 1.13x faster                                                            |
| async_tree_io              | 939 ms                                                     | 856 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.08x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 868 ms: 1.08x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 554 ms: 1.06x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.13x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 76.6 ms: 1.03x faster                                                           |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                            |
| nbody          | 88.3 ms                                                    | 89.9 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 127 ms: 1.07x faster                                                            |
| regex_v8       | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                           |
| regex_effbot   | 3.67 ms                                                    | 3.68 ms: 1.00x slower                                                           |
| regex_dna      | 221 ms                                                     | 225 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 26.8 us: 1.08x faster                                                           |
| json_dumps           | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                                           |
| xml_etree_parse      | 162 ms                                                     | 154 ms: 1.05x faster                                                            |
| xml_etree_process    | 61.2 ms                                                    | 58.7 ms: 1.04x faster                                                           |
| xml_etree_generate   | 87.4 ms                                                    | 84.8 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.03x faster                                                            |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                            |
| unpickle_list        | 5.34 us                                                    | 5.27 us: 1.01x faster                                                           |
| tomli_loads          | 2.12 sec                                                   | 2.10 sec: 1.01x faster                                                          |
| pickle_pure_python   | 305 us                                                     | 304 us: 1.00x faster                                                            |
| pickle_list          | 5.11 us                                                    | 5.18 us: 1.01x slower                                                           |
| pickle_dict          | 34.8 us                                                    | 35.4 us: 1.02x slower                                                           |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                                           |
| unpickle             | 15.1 us                                                    | 16.0 us: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.00 ms: 1.02x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 21.9 ms: 1.08x faster                                                           |
| genshi_xml      | 51.6 ms                                                    | 49.2 ms: 1.05x faster                                                           |
| django_template | 34.8 ms                                                    | 34.5 ms: 1.01x faster                                                           |
| mako            | 11.2 ms                                                    | 11.4 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 256 us: 1.43x faster                                                            |
| deepcopy_memo              | 39.7 us                                                    | 30.4 us: 1.31x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.67 us: 1.26x faster                                                           |
| async_tree_none            | 378 ms                                                     | 310 ms: 1.22x faster                                                            |
| go                         | 145 ms                                                     | 120 ms: 1.20x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 391 ms: 1.18x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 385 ms: 1.15x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 297 ms: 1.13x faster                                                            |
| gc_traversal               | 3.98 ms                                                    | 3.55 ms: 1.12x faster                                                           |
| async_tree_io              | 939 ms                                                     | 856 ms: 1.10x faster                                                            |
| richards_super             | 57.4 ms                                                    | 52.3 ms: 1.10x faster                                                           |
| richards                   | 50.9 ms                                                    | 46.5 ms: 1.09x faster                                                           |
| json                       | 5.31 ms                                                    | 4.86 ms: 1.09x faster                                                           |
| crypto_pyaes               | 77.5 ms                                                    | 71.0 ms: 1.09x faster                                                           |
| asyncio_tcp                | 508 ms                                                     | 468 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.08x faster                                                            |
| scimark_lu                 | 122 ms                                                     | 112 ms: 1.08x faster                                                            |
| html5lib                   | 67.2 ms                                                    | 62.2 ms: 1.08x faster                                                           |
| genshi_text                | 23.7 ms                                                    | 21.9 ms: 1.08x faster                                                           |
| thrift                     | 823 us                                                     | 763 us: 1.08x faster                                                            |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                           |
| async_tree_io_tg           | 936 ms                                                     | 868 ms: 1.08x faster                                                            |
| json_loads                 | 28.9 us                                                    | 26.8 us: 1.08x faster                                                           |
| 2to3                       | 274 ms                                                     | 255 ms: 1.07x faster                                                            |
| regex_compile              | 137 ms                                                     | 127 ms: 1.07x faster                                                            |
| coverage                   | 93.1 ms                                                    | 86.8 ms: 1.07x faster                                                           |
| scimark_fft                | 392 ms                                                     | 367 ms: 1.07x faster                                                            |
| pprint_safe_repr           | 758 ms                                                     | 710 ms: 1.07x faster                                                            |
| docutils                   | 2.83 sec                                                   | 2.65 sec: 1.07x faster                                                          |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.07x faster                                                          |
| sympy_sum                  | 156 ms                                                     | 146 ms: 1.06x faster                                                            |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.96 ms: 1.06x faster                                                           |
| generators                 | 29.6 ms                                                    | 27.9 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 554 ms: 1.06x faster                                                            |
| json_dumps                 | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                                           |
| sympy_str                  | 282 ms                                                     | 268 ms: 1.06x faster                                                            |
| bench_thread_pool          | 834 us                                                     | 791 us: 1.05x faster                                                            |
| tornado_http               | 94.6 ms                                                    | 89.8 ms: 1.05x faster                                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 4.77 sec: 1.05x faster                                                          |
| xml_etree_parse            | 162 ms                                                     | 154 ms: 1.05x faster                                                            |
| sqlglot_optimize           | 55.5 ms                                                    | 52.9 ms: 1.05x faster                                                           |
| sympy_integrate            | 20.5 ms                                                    | 19.5 ms: 1.05x faster                                                           |
| typing_runtime_protocols   | 165 us                                                     | 157 us: 1.05x faster                                                            |
| sqlite_synth               | 2.99 us                                                    | 2.85 us: 1.05x faster                                                           |
| genshi_xml                 | 51.6 ms                                                    | 49.2 ms: 1.05x faster                                                           |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                                           |
| logging_format             | 6.47 us                                                    | 6.19 us: 1.04x faster                                                           |
| dulwich_log                | 67.2 ms                                                    | 64.3 ms: 1.04x faster                                                           |
| sqlglot_normalize          | 110 ms                                                     | 106 ms: 1.04x faster                                                            |
| xml_etree_process          | 61.2 ms                                                    | 58.7 ms: 1.04x faster                                                           |
| chaos                      | 61.3 ms                                                    | 59.0 ms: 1.04x faster                                                           |
| sympy_expand               | 473 ms                                                     | 456 ms: 1.04x faster                                                            |
| mdp                        | 2.79 sec                                                   | 2.69 sec: 1.04x faster                                                          |
| pyflate                    | 484 ms                                                     | 468 ms: 1.03x faster                                                            |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.03x faster                                                           |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                           |
| nqueens                    | 81.4 ms                                                    | 78.9 ms: 1.03x faster                                                           |
| xml_etree_generate         | 87.4 ms                                                    | 84.8 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                          |
| float                      | 78.9 ms                                                    | 76.6 ms: 1.03x faster                                                           |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                            |
| scimark_sor                | 127 ms                                                     | 124 ms: 1.03x faster                                                            |
| logging_simple             | 5.74 us                                                    | 5.59 us: 1.03x faster                                                           |
| spectral_norm              | 116 ms                                                     | 113 ms: 1.03x faster                                                            |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.03x faster                                                            |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| async_generators           | 442 ms                                                     | 432 ms: 1.02x faster                                                            |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.7 ms: 1.02x faster                                                           |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                            |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                                            |
| regex_v8                   | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.00 ms: 1.02x faster                                                           |
| hexiom                     | 6.30 ms                                                    | 6.20 ms: 1.01x faster                                                           |
| unpickle_list              | 5.34 us                                                    | 5.27 us: 1.01x faster                                                           |
| tomli_loads                | 2.12 sec                                                   | 2.10 sec: 1.01x faster                                                          |
| logging_silent             | 105 ns                                                     | 104 ns: 1.01x faster                                                            |
| django_template            | 34.8 ms                                                    | 34.5 ms: 1.01x faster                                                           |
| raytrace                   | 267 ms                                                     | 265 ms: 1.01x faster                                                            |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                           |
| pickle_pure_python         | 305 us                                                     | 304 us: 1.00x faster                                                            |
| regex_effbot               | 3.67 ms                                                    | 3.68 ms: 1.00x slower                                                           |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                           |
| fannkuch                   | 402 ms                                                     | 404 ms: 1.01x slower                                                            |
| deltablue                  | 3.25 ms                                                    | 3.28 ms: 1.01x slower                                                           |
| mako                       | 11.2 ms                                                    | 11.4 ms: 1.01x slower                                                           |
| coroutines                 | 23.2 ms                                                    | 23.4 ms: 1.01x slower                                                           |
| telco                      | 8.41 ms                                                    | 8.51 ms: 1.01x slower                                                           |
| pickle_list                | 5.11 us                                                    | 5.18 us: 1.01x slower                                                           |
| regex_dna                  | 221 ms                                                     | 225 ms: 1.02x slower                                                            |
| pickle_dict                | 34.8 us                                                    | 35.4 us: 1.02x slower                                                           |
| nbody                      | 88.3 ms                                                    | 89.9 ms: 1.02x slower                                                           |
| pickle                     | 11.5 us                                                    | 11.7 us: 1.02x slower                                                           |
| unpickle                   | 15.1 us                                                    | 16.0 us: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                    |

Benchmark hidden because not significant (2): pycparser, pylint
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240920-3.14.0a0-e179c31/bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.00x