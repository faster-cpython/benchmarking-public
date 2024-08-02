# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: dynamic_exit
- machine: linux-x86_64
- commit hash: a8158ae
- commit date: 2024-05-05
- overall geometric mean: 1.22x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 357 ms: 1.30x slower                                                 |
| chameleon      | 7.22 ms                                                    | 9.02 ms: 1.25x slower                                                |
| html5lib       | 67.2 ms                                                    | 83.5 ms: 1.24x slower                                                |
| tornado_http   | 94.6 ms                                                    | 108 ms: 1.14x slower                                                 |
| Geometric mean | (ref)                                                      | 1.23x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 481 ms: 1.08x slower                                                 |
| async_tree_none            | 378 ms                                                     | 411 ms: 1.09x slower                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 639 ms: 1.09x slower                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 666 ms: 1.09x slower                                                 |
| async_tree_io_tg           | 936 ms                                                     | 1.03 sec: 1.10x slower                                               |
| async_tree_io              | 939 ms                                                     | 1.05 sec: 1.12x slower                                               |
| async_tree_none_tg         | 336 ms                                                     | 379 ms: 1.13x slower                                                 |
| async_tree_memoization     | 463 ms                                                     | 532 ms: 1.15x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.10x slower                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 193 ms: 1.01x slower                                                 |
| float          | 78.9 ms                                                    | 92.6 ms: 1.17x slower                                                |
| nbody          | 88.3 ms                                                    | 123 ms: 1.39x slower                                                 |
| Geometric mean | (ref)                                                      | 1.18x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 223 ms: 1.01x slower                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                |
| regex_v8       | 25.1 ms                                                    | 27.1 ms: 1.08x slower                                                |
| regex_compile  | 137 ms                                                     | 220 ms: 1.61x slower                                                 |
| Geometric mean | (ref)                                                      | 1.16x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 154 ms: 1.05x faster                                                 |
| json_loads           | 28.9 us                                                    | 27.7 us: 1.04x faster                                                |
| unpickle_list        | 5.34 us                                                    | 5.17 us: 1.03x faster                                                |
| pickle_list          | 5.11 us                                                    | 5.03 us: 1.01x faster                                                |
| xml_etree_iterparse  | 107 ms                                                     | 111 ms: 1.03x slower                                                 |
| pickle_dict          | 34.8 us                                                    | 36.0 us: 1.03x slower                                                |
| unpickle             | 15.1 us                                                    | 15.7 us: 1.04x slower                                                |
| pickle               | 11.5 us                                                    | 12.1 us: 1.06x slower                                                |
| json_dumps           | 10.7 ms                                                    | 11.5 ms: 1.07x slower                                                |
| xml_etree_process    | 61.2 ms                                                    | 71.4 ms: 1.17x slower                                                |
| xml_etree_generate   | 87.4 ms                                                    | 104 ms: 1.18x slower                                                 |
| tomli_loads          | 2.12 sec                                                   | 2.81 sec: 1.32x slower                                               |
| unpickle_pure_python | 218 us                                                     | 331 us: 1.52x slower                                                 |
| pickle_pure_python   | 305 us                                                     | 525 us: 1.72x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.13x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.8 ms: 1.00x slower                                                |
| python_startup_no_site | 7.11 ms                                                    | 7.25 ms: 1.02x slower                                                |
| Geometric mean         | (ref)                                                      | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 14.2 ms: 1.26x slower                                                |
| django_template | 34.8 ms                                                    | 49.2 ms: 1.41x slower                                                |
| genshi_xml      | 51.6 ms                                                    | 82.8 ms: 1.60x slower                                                |
| genshi_text     | 23.7 ms                                                    | 39.8 ms: 1.68x slower                                                |
| Geometric mean  | (ref)                                                      | 1.48x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse            | 162 ms                                                     | 154 ms: 1.05x faster                                                 |
| json_loads                 | 28.9 us                                                    | 27.7 us: 1.04x faster                                                |
| unpickle_list              | 5.34 us                                                    | 5.17 us: 1.03x faster                                                |
| gc_traversal               | 3.98 ms                                                    | 3.88 ms: 1.02x faster                                                |
| pickle_list                | 5.11 us                                                    | 5.03 us: 1.01x faster                                                |
| coverage                   | 93.1 ms                                                    | 92.4 ms: 1.01x faster                                                |
| python_startup             | 10.8 ms                                                    | 10.8 ms: 1.00x slower                                                |
| regex_dna                  | 221 ms                                                     | 223 ms: 1.01x slower                                                 |
| pidigits                   | 191 ms                                                     | 193 ms: 1.01x slower                                                 |
| thrift                     | 823 us                                                     | 832 us: 1.01x slower                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.87 sec: 1.02x slower                                               |
| python_startup_no_site     | 7.11 ms                                                    | 7.25 ms: 1.02x slower                                                |
| regex_effbot               | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                |
| create_gc_cycles           | 1.82 ms                                                    | 1.87 ms: 1.03x slower                                                |
| xml_etree_iterparse        | 107 ms                                                     | 111 ms: 1.03x slower                                                 |
| asyncio_tcp                | 508 ms                                                     | 526 ms: 1.03x slower                                                 |
| pickle_dict                | 34.8 us                                                    | 36.0 us: 1.03x slower                                                |
| sqlite_synth               | 2.99 us                                                    | 3.10 us: 1.04x slower                                                |
| unpickle                   | 15.1 us                                                    | 15.7 us: 1.04x slower                                                |
| json                       | 5.31 ms                                                    | 5.53 ms: 1.04x slower                                                |
| mdp                        | 2.79 sec                                                   | 2.91 sec: 1.04x slower                                               |
| pickle                     | 11.5 us                                                    | 12.1 us: 1.06x slower                                                |
| djangocms                  | 31.5 us                                                    | 33.5 us: 1.06x slower                                                |
| flaskblogging              | 9.01 ms                                                    | 9.59 ms: 1.06x slower                                                |
| coroutines                 | 23.2 ms                                                    | 24.8 ms: 1.07x slower                                                |
| dask                       | 369 ms                                                     | 395 ms: 1.07x slower                                                 |
| json_dumps                 | 10.7 ms                                                    | 11.5 ms: 1.07x slower                                                |
| regex_v8                   | 25.1 ms                                                    | 27.1 ms: 1.08x slower                                                |
| async_tree_memoization_tg  | 444 ms                                                     | 481 ms: 1.08x slower                                                 |
| async_tree_none            | 378 ms                                                     | 411 ms: 1.09x slower                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 639 ms: 1.09x slower                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 666 ms: 1.09x slower                                                 |
| async_tree_io_tg           | 936 ms                                                     | 1.03 sec: 1.10x slower                                               |
| pathlib                    | 17.3 ms                                                    | 19.0 ms: 1.10x slower                                                |
| gunicorn                   | 1.28 ms                                                    | 1.41 ms: 1.10x slower                                                |
| aiohttp                    | 1.18 ms                                                    | 1.30 ms: 1.10x slower                                                |
| async_tree_io              | 939 ms                                                     | 1.05 sec: 1.12x slower                                               |
| async_tree_none_tg         | 336 ms                                                     | 379 ms: 1.13x slower                                                 |
| scimark_fft                | 392 ms                                                     | 445 ms: 1.13x slower                                                 |
| async_generators           | 442 ms                                                     | 504 ms: 1.14x slower                                                 |
| tornado_http               | 94.6 ms                                                    | 108 ms: 1.14x slower                                                 |
| async_tree_memoization     | 463 ms                                                     | 532 ms: 1.15x slower                                                 |
| dulwich_log                | 67.2 ms                                                    | 77.9 ms: 1.16x slower                                                |
| xml_etree_process          | 61.2 ms                                                    | 71.4 ms: 1.17x slower                                                |
| float                      | 78.9 ms                                                    | 92.6 ms: 1.17x slower                                                |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 6.20 ms: 1.18x slower                                                |
| meteor_contest             | 110 ms                                                     | 129 ms: 1.18x slower                                                 |
| spectral_norm              | 116 ms                                                     | 137 ms: 1.18x slower                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 104 ms: 1.18x slower                                                 |
| bench_thread_pool          | 834 us                                                     | 991 us: 1.19x slower                                                 |
| mypy2                      | 742 ms                                                     | 886 ms: 1.19x slower                                                 |
| fannkuch                   | 402 ms                                                     | 483 ms: 1.20x slower                                                 |
| logging_format             | 6.47 us                                                    | 7.83 us: 1.21x slower                                                |
| logging_simple             | 5.74 us                                                    | 6.97 us: 1.21x slower                                                |
| html5lib                   | 67.2 ms                                                    | 83.5 ms: 1.24x slower                                                |
| scimark_sor                | 127 ms                                                     | 158 ms: 1.24x slower                                                 |
| sympy_sum                  | 156 ms                                                     | 194 ms: 1.24x slower                                                 |
| chameleon                  | 7.22 ms                                                    | 9.02 ms: 1.25x slower                                                |
| pylint                     | 317 ms                                                     | 396 ms: 1.25x slower                                                 |
| mako                       | 11.2 ms                                                    | 14.2 ms: 1.26x slower                                                |
| sympy_integrate            | 20.5 ms                                                    | 25.9 ms: 1.27x slower                                                |
| telco                      | 8.41 ms                                                    | 10.7 ms: 1.27x slower                                                |
| pyflate                    | 484 ms                                                     | 619 ms: 1.28x slower                                                 |
| crypto_pyaes               | 77.5 ms                                                    | 99.9 ms: 1.29x slower                                                |
| sympy_str                  | 282 ms                                                     | 366 ms: 1.30x slower                                                 |
| sympy_expand               | 473 ms                                                     | 614 ms: 1.30x slower                                                 |
| 2to3                       | 274 ms                                                     | 357 ms: 1.30x slower                                                 |
| typing_runtime_protocols   | 165 us                                                     | 217 us: 1.32x slower                                                 |
| tomli_loads                | 2.12 sec                                                   | 2.81 sec: 1.32x slower                                               |
| deepcopy_reduce            | 3.35 us                                                    | 4.45 us: 1.33x slower                                                |
| raytrace                   | 267 ms                                                     | 357 ms: 1.34x slower                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 75.4 ms: 1.36x slower                                                |
| sqlglot_parse              | 1.32 ms                                                    | 1.81 ms: 1.37x slower                                                |
| sqlglot_transpile          | 1.63 ms                                                    | 2.24 ms: 1.37x slower                                                |
| richards_super             | 57.4 ms                                                    | 79.4 ms: 1.38x slower                                                |
| pycparser                  | 1.16 sec                                                   | 1.60 sec: 1.38x slower                                               |
| nbody                      | 88.3 ms                                                    | 123 ms: 1.39x slower                                                 |
| richards                   | 50.9 ms                                                    | 71.0 ms: 1.40x slower                                                |
| sqlglot_normalize          | 110 ms                                                     | 154 ms: 1.40x slower                                                 |
| scimark_lu                 | 122 ms                                                     | 171 ms: 1.41x slower                                                 |
| deepcopy                   | 367 us                                                     | 518 us: 1.41x slower                                                 |
| django_template            | 34.8 ms                                                    | 49.2 ms: 1.41x slower                                                |
| deepcopy_memo              | 39.7 us                                                    | 56.6 us: 1.43x slower                                                |
| chaos                      | 61.3 ms                                                    | 87.6 ms: 1.43x slower                                                |
| deltablue                  | 3.25 ms                                                    | 4.67 ms: 1.44x slower                                                |
| go                         | 145 ms                                                     | 208 ms: 1.44x slower                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 99.5 ms: 1.44x slower                                                |
| logging_silent             | 105 ns                                                     | 152 ns: 1.45x slower                                                 |
| unpickle_pure_python       | 218 us                                                     | 331 us: 1.52x slower                                                 |
| pprint_safe_repr           | 758 ms                                                     | 1.21 sec: 1.60x slower                                               |
| genshi_xml                 | 51.6 ms                                                    | 82.8 ms: 1.60x slower                                                |
| regex_compile              | 137 ms                                                     | 220 ms: 1.61x slower                                                 |
| comprehensions             | 16.6 us                                                    | 27.1 us: 1.63x slower                                                |
| pprint_pformat             | 1.56 sec                                                   | 2.55 sec: 1.64x slower                                               |
| genshi_text                | 23.7 ms                                                    | 39.8 ms: 1.68x slower                                                |
| hexiom                     | 6.30 ms                                                    | 10.7 ms: 1.70x slower                                                |
| pickle_pure_python         | 305 us                                                     | 525 us: 1.72x slower                                                 |
| nqueens                    | 81.4 ms                                                    | 141 ms: 1.73x slower                                                 |
| generators                 | 29.6 ms                                                    | 65.9 ms: 2.22x slower                                                |
| Geometric mean             | (ref)                                                      | 1.22x slower                                                         |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, docutils

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.17x
- 95% likely to have a slowdown of 1.17x
- 99% likely to have a slowdown of 1.15x

# Memory
- memory change: 1.01x