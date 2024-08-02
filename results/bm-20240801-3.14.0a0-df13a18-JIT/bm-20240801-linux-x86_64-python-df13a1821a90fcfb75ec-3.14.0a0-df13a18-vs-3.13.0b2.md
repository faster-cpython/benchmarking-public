# Results vs. 3.13.0b2

- fork: python
- ref: df13a1821a90fcfb75ec
- machine: linux-x86_64
- commit hash: df13a18
- commit date: 2024-08-01
- overall geometric mean: 1.04x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 274 ms: 1.00x slower                                                  |
| docutils       | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                                |
| html5lib       | 67.2 ms                                                    | 65.2 ms: 1.03x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 92.3 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 396 ms: 1.12x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 303 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 538 ms: 1.09x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 426 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 871 ms: 1.07x faster                                                  |
| async_tree_io              | 939 ms                                                     | 910 ms: 1.03x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 79.8 ms: 1.11x faster                                                 |
| float          | 78.9 ms                                                    | 71.6 ms: 1.10x faster                                                 |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                      | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 133 ms: 1.03x faster                                                  |
| regex_v8       | 25.1 ms                                                    | 25.2 ms: 1.01x slower                                                 |
| regex_dna      | 221 ms                                                     | 223 ms: 1.01x slower                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                                  |
| xml_etree_generate   | 87.4 ms                                                    | 80.0 ms: 1.09x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 56.0 ms: 1.09x faster                                                 |
| tomli_loads          | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                |
| xml_etree_iterparse  | 107 ms                                                     | 99.8 ms: 1.08x faster                                                 |
| json_loads           | 28.9 us                                                    | 27.9 us: 1.04x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 297 us: 1.03x faster                                                  |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.02x faster                                                  |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.14 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.82 ms: 1.14x faster                                                 |
| django_template | 34.8 ms                                                    | 36.0 ms: 1.04x slower                                                 |
| genshi_text     | 23.7 ms                                                    | 24.7 ms: 1.04x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 54.5 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.00x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 29.0 us: 1.37x faster                                                 |
| deepcopy                   | 367 us                                                     | 273 us: 1.35x faster                                                  |
| scimark_fft                | 392 ms                                                     | 311 ms: 1.26x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.24 ms: 1.24x faster                                                 |
| richards                   | 50.9 ms                                                    | 41.1 ms: 1.24x faster                                                 |
| richards_super             | 57.4 ms                                                    | 46.8 ms: 1.23x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.82 us: 1.19x faster                                                 |
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 67.4 ms: 1.15x faster                                                 |
| mako                       | 11.2 ms                                                    | 9.82 ms: 1.14x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.9 ms: 1.14x faster                                                 |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.13x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 396 ms: 1.12x faster                                                  |
| pyflate                    | 484 ms                                                     | 433 ms: 1.12x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.12x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.51 sec: 1.11x faster                                                |
| async_tree_none_tg         | 336 ms                                                     | 303 ms: 1.11x faster                                                  |
| nbody                      | 88.3 ms                                                    | 79.8 ms: 1.11x faster                                                 |
| float                      | 78.9 ms                                                    | 71.6 ms: 1.10x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                  |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                  |
| xml_etree_generate         | 87.4 ms                                                    | 80.0 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 538 ms: 1.09x faster                                                  |
| xml_etree_process          | 61.2 ms                                                    | 56.0 ms: 1.09x faster                                                 |
| tomli_loads                | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                |
| async_tree_memoization     | 463 ms                                                     | 426 ms: 1.09x faster                                                  |
| fannkuch                   | 402 ms                                                     | 369 ms: 1.09x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 99.8 ms: 1.08x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 871 ms: 1.07x faster                                                  |
| logging_format             | 6.47 us                                                    | 6.06 us: 1.07x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 16.3 ms: 1.06x faster                                                 |
| gc_traversal               | 3.98 ms                                                    | 3.74 ms: 1.06x faster                                                 |
| chaos                      | 61.3 ms                                                    | 57.8 ms: 1.06x faster                                                 |
| mdp                        | 2.79 sec                                                   | 2.63 sec: 1.06x faster                                                |
| telco                      | 8.41 ms                                                    | 7.95 ms: 1.06x faster                                                 |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.05x faster                                                  |
| json_loads                 | 28.9 us                                                    | 27.9 us: 1.04x faster                                                 |
| asyncio_tcp                | 508 ms                                                     | 490 ms: 1.04x faster                                                  |
| thrift                     | 823 us                                                     | 794 us: 1.04x faster                                                  |
| json                       | 5.31 ms                                                    | 5.13 ms: 1.04x faster                                                 |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                 |
| async_tree_io              | 939 ms                                                     | 910 ms: 1.03x faster                                                  |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| logging_simple             | 5.74 us                                                    | 5.57 us: 1.03x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 65.2 ms: 1.03x faster                                                 |
| regex_compile              | 137 ms                                                     | 133 ms: 1.03x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                                |
| pprint_safe_repr           | 758 ms                                                     | 738 ms: 1.03x faster                                                  |
| pickle_pure_python         | 305 us                                                     | 297 us: 1.03x faster                                                  |
| tornado_http               | 94.6 ms                                                    | 92.3 ms: 1.02x faster                                                 |
| coroutines                 | 23.2 ms                                                    | 22.6 ms: 1.02x faster                                                 |
| comprehensions             | 16.6 us                                                    | 16.2 us: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                |
| coverage                   | 93.1 ms                                                    | 91.3 ms: 1.02x faster                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.30 ms: 1.02x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.02x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 821 us: 1.02x faster                                                  |
| dask                       | 369 ms                                                     | 365 ms: 1.01x faster                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                                 |
| 2to3                       | 274 ms                                                     | 274 ms: 1.00x slower                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.14 ms: 1.00x slower                                                 |
| regex_v8                   | 25.1 ms                                                    | 25.2 ms: 1.01x slower                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 55.8 ms: 1.01x slower                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| regex_dna                  | 221 ms                                                     | 223 ms: 1.01x slower                                                  |
| logging_silent             | 105 ns                                                     | 106 ns: 1.01x slower                                                  |
| go                         | 145 ms                                                     | 146 ms: 1.01x slower                                                  |
| pycparser                  | 1.16 sec                                                   | 1.17 sec: 1.01x slower                                                |
| raytrace                   | 267 ms                                                     | 271 ms: 1.02x slower                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                 |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.02x slower                                                  |
| typing_runtime_protocols   | 165 us                                                     | 168 us: 1.02x slower                                                  |
| docutils                   | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                                |
| django_template            | 34.8 ms                                                    | 36.0 ms: 1.04x slower                                                 |
| genshi_text                | 23.7 ms                                                    | 24.7 ms: 1.04x slower                                                 |
| async_generators           | 442 ms                                                     | 466 ms: 1.05x slower                                                  |
| genshi_xml                 | 51.6 ms                                                    | 54.5 ms: 1.06x slower                                                 |
| sympy_str                  | 282 ms                                                     | 300 ms: 1.06x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 86.4 ms: 1.06x slower                                                 |
| hexiom                     | 6.30 ms                                                    | 6.73 ms: 1.07x slower                                                 |
| sympy_expand               | 473 ms                                                     | 510 ms: 1.08x slower                                                  |
| sympy_sum                  | 156 ms                                                     | 170 ms: 1.09x slower                                                  |
| sympy_integrate            | 20.5 ms                                                    | 22.6 ms: 1.10x slower                                                 |
| deltablue                  | 3.25 ms                                                    | 3.60 ms: 1.11x slower                                                 |
| generators                 | 29.6 ms                                                    | 33.1 ms: 1.12x slower                                                 |
| pylint                     | 317 ms                                                     | 355 ms: 1.12x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                          |
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x