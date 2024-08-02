# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: dynamic_exit
- machine: linux-x86_64
- commit hash: a8158ae
- commit date: 2024-05-05
- overall geometric mean: 1.01x slower
- HPT reliability: 88.84%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 284 ms: 1.03x slower                                                 |
| chameleon      | 7.22 ms                                                    | 7.30 ms: 1.01x slower                                                |
| html5lib       | 67.2 ms                                                    | 70.5 ms: 1.05x slower                                                |
| tornado_http   | 94.6 ms                                                    | 98.0 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                      | 1.03x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 605 ms: 1.03x slower                                                 |
| async_tree_none_tg         | 336 ms                                                     | 351 ms: 1.05x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.02x slower                                                         |

Benchmark hidden because not significant (6): async_tree_none, async_tree_io, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 79.0 ms: 1.12x faster                                                |
| float          | 78.9 ms                                                    | 72.3 ms: 1.09x faster                                                |
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.07x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                                |
| regex_effbot   | 3.67 ms                                                    | 3.74 ms: 1.02x slower                                                |
| regex_dna      | 221 ms                                                     | 226 ms: 1.02x slower                                                 |
| regex_compile  | 137 ms                                                     | 141 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.97 sec: 1.08x faster                                               |
| xml_etree_parse      | 162 ms                                                     | 153 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.06x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 58.9 ms: 1.04x faster                                                |
| xml_etree_generate   | 87.4 ms                                                    | 84.2 ms: 1.04x faster                                                |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                |
| json_loads           | 28.9 us                                                    | 27.9 us: 1.03x faster                                                |
| pickle_list          | 5.11 us                                                    | 4.99 us: 1.02x faster                                                |
| pickle_pure_python   | 305 us                                                     | 301 us: 1.02x faster                                                 |
| unpickle_list        | 5.34 us                                                    | 5.39 us: 1.01x slower                                                |
| pickle_dict          | 34.8 us                                                    | 35.5 us: 1.02x slower                                                |
| unpickle_pure_python | 218 us                                                     | 224 us: 1.03x slower                                                 |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                                |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                         |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                                |
| python_startup_no_site | 7.11 ms                                                    | 7.66 ms: 1.08x slower                                                |
| Geometric mean         | (ref)                                                      | 1.06x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.67 ms: 1.16x faster                                                |
| django_template | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                |
| genshi_text     | 23.7 ms                                                    | 24.5 ms: 1.04x slower                                                |
| genshi_xml      | 51.6 ms                                                    | 58.2 ms: 1.13x slower                                                |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| scimark_fft                | 392 ms                                                     | 313 ms: 1.26x faster                                                 |
| richards                   | 50.9 ms                                                    | 43.2 ms: 1.18x faster                                                |
| spectral_norm              | 116 ms                                                     | 99.0 ms: 1.17x faster                                                |
| richards_super             | 57.4 ms                                                    | 49.3 ms: 1.16x faster                                                |
| mako                       | 11.2 ms                                                    | 9.67 ms: 1.16x faster                                                |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.63 ms: 1.14x faster                                                |
| crypto_pyaes               | 77.5 ms                                                    | 69.1 ms: 1.12x faster                                                |
| fannkuch                   | 402 ms                                                     | 359 ms: 1.12x faster                                                 |
| nbody                      | 88.3 ms                                                    | 79.0 ms: 1.12x faster                                                |
| float                      | 78.9 ms                                                    | 72.3 ms: 1.09x faster                                                |
| tomli_loads                | 2.12 sec                                                   | 1.97 sec: 1.08x faster                                               |
| mdp                        | 2.79 sec                                                   | 2.59 sec: 1.08x faster                                               |
| scimark_monte_carlo        | 69.2 ms                                                    | 64.2 ms: 1.08x faster                                                |
| pyflate                    | 484 ms                                                     | 452 ms: 1.07x faster                                                 |
| coverage                   | 93.1 ms                                                    | 87.1 ms: 1.07x faster                                                |
| xml_etree_parse            | 162 ms                                                     | 153 ms: 1.06x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 101 ms: 1.06x faster                                                 |
| chaos                      | 61.3 ms                                                    | 58.2 ms: 1.05x faster                                                |
| deepcopy_memo              | 39.7 us                                                    | 37.8 us: 1.05x faster                                                |
| sqlite_synth               | 2.99 us                                                    | 2.87 us: 1.04x faster                                                |
| xml_etree_process          | 61.2 ms                                                    | 58.9 ms: 1.04x faster                                                |
| xml_etree_generate         | 87.4 ms                                                    | 84.2 ms: 1.04x faster                                                |
| pprint_safe_repr           | 758 ms                                                     | 731 ms: 1.04x faster                                                 |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                |
| json_loads                 | 28.9 us                                                    | 27.9 us: 1.03x faster                                                |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                               |
| pickle_list                | 5.11 us                                                    | 4.99 us: 1.02x faster                                                |
| json                       | 5.31 ms                                                    | 5.20 ms: 1.02x faster                                                |
| thrift                     | 823 us                                                     | 810 us: 1.02x faster                                                 |
| pickle_pure_python         | 305 us                                                     | 301 us: 1.02x faster                                                 |
| regex_v8                   | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                                |
| deepcopy_reduce            | 3.35 us                                                    | 3.30 us: 1.01x faster                                                |
| pidigits                   | 191 ms                                                     | 189 ms: 1.01x faster                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                |
| logging_format             | 6.47 us                                                    | 6.43 us: 1.01x faster                                                |
| meteor_contest             | 110 ms                                                     | 109 ms: 1.01x faster                                                 |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                                |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                |
| unpickle_list              | 5.34 us                                                    | 5.39 us: 1.01x slower                                                |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                               |
| chameleon                  | 7.22 ms                                                    | 7.30 ms: 1.01x slower                                                |
| regex_effbot               | 3.67 ms                                                    | 3.74 ms: 1.02x slower                                                |
| coroutines                 | 23.2 ms                                                    | 23.7 ms: 1.02x slower                                                |
| regex_dna                  | 221 ms                                                     | 226 ms: 1.02x slower                                                 |
| pickle_dict                | 34.8 us                                                    | 35.5 us: 1.02x slower                                                |
| go                         | 145 ms                                                     | 148 ms: 1.02x slower                                                 |
| dask                       | 369 ms                                                     | 378 ms: 1.02x slower                                                 |
| asyncio_tcp                | 508 ms                                                     | 521 ms: 1.02x slower                                                 |
| flaskblogging              | 9.01 ms                                                    | 9.25 ms: 1.03x slower                                                |
| sqlglot_optimize           | 55.5 ms                                                    | 57.0 ms: 1.03x slower                                                |
| scimark_lu                 | 122 ms                                                     | 125 ms: 1.03x slower                                                 |
| unpickle_pure_python       | 218 us                                                     | 224 us: 1.03x slower                                                 |
| pickle                     | 11.5 us                                                    | 11.8 us: 1.03x slower                                                |
| django_template            | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 605 ms: 1.03x slower                                                 |
| regex_compile              | 137 ms                                                     | 141 ms: 1.03x slower                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.87 ms: 1.03x slower                                                |
| pathlib                    | 17.3 ms                                                    | 17.9 ms: 1.03x slower                                                |
| djangocms                  | 31.5 us                                                    | 32.6 us: 1.03x slower                                                |
| 2to3                       | 274 ms                                                     | 284 ms: 1.03x slower                                                 |
| genshi_text                | 23.7 ms                                                    | 24.5 ms: 1.04x slower                                                |
| tornado_http               | 94.6 ms                                                    | 98.0 ms: 1.04x slower                                                |
| gc_traversal               | 3.98 ms                                                    | 4.12 ms: 1.04x slower                                                |
| python_startup             | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                                |
| logging_silent             | 105 ns                                                     | 109 ns: 1.04x slower                                                 |
| async_tree_none_tg         | 336 ms                                                     | 351 ms: 1.05x slower                                                 |
| bench_thread_pool          | 834 us                                                     | 871 us: 1.05x slower                                                 |
| scimark_sor                | 127 ms                                                     | 133 ms: 1.05x slower                                                 |
| hexiom                     | 6.30 ms                                                    | 6.60 ms: 1.05x slower                                                |
| html5lib                   | 67.2 ms                                                    | 70.5 ms: 1.05x slower                                                |
| dulwich_log                | 67.2 ms                                                    | 70.4 ms: 1.05x slower                                                |
| async_generators           | 442 ms                                                     | 465 ms: 1.05x slower                                                 |
| sqlglot_normalize          | 110 ms                                                     | 116 ms: 1.06x slower                                                 |
| gunicorn                   | 1.28 ms                                                    | 1.35 ms: 1.06x slower                                                |
| raytrace                   | 267 ms                                                     | 282 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 165 us                                                     | 175 us: 1.07x slower                                                 |
| aiohttp                    | 1.18 ms                                                    | 1.26 ms: 1.07x slower                                                |
| sympy_str                  | 282 ms                                                     | 302 ms: 1.07x slower                                                 |
| sympy_expand               | 473 ms                                                     | 508 ms: 1.08x slower                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.66 ms: 1.08x slower                                                |
| nqueens                    | 81.4 ms                                                    | 88.4 ms: 1.09x slower                                                |
| sympy_sum                  | 156 ms                                                     | 172 ms: 1.10x slower                                                 |
| mypy2                      | 742 ms                                                     | 822 ms: 1.11x slower                                                 |
| sympy_integrate            | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                                |
| genshi_xml                 | 51.6 ms                                                    | 58.2 ms: 1.13x slower                                                |
| pylint                     | 317 ms                                                     | 364 ms: 1.15x slower                                                 |
| deltablue                  | 3.25 ms                                                    | 3.86 ms: 1.19x slower                                                |
| generators                 | 29.6 ms                                                    | 51.4 ms: 1.74x slower                                                |
| Geometric mean             | (ref)                                                      | 1.01x slower                                                         |

Benchmark hidden because not significant (13): async_tree_none, async_tree_io, telco, asyncio_websockets, sqlglot_transpile, deepcopy, logging_simple, pycparser, unpickle, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io_tg
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, docutils

# HPT report

- Reliability score: 88.84% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x