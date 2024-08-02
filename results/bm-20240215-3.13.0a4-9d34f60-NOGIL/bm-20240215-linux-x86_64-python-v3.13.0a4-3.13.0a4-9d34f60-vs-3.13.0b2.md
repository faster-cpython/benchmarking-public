# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.12x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 296 ms: 1.08x slower                                       |
| chameleon      | 7.22 ms                                                    | 8.24 ms: 1.14x slower                                      |
| docutils       | 2.83 sec                                                   | 3.07 sec: 1.08x slower                                     |
| html5lib       | 67.2 ms                                                    | 67.9 ms: 1.01x slower                                      |
| tornado_http   | 94.6 ms                                                    | 98.6 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                      | 1.07x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_io              | 939 ms                                                     | 796 ms: 1.18x faster                                       |
| async_tree_io_tg           | 936 ms                                                     | 828 ms: 1.13x faster                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 458 ms: 1.03x slower                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 612 ms: 1.04x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 646 ms: 1.06x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 377 ms: 1.12x slower                                       |
| Geometric mean             | (ref)                                                      | 1.00x faster                                               |

Benchmark hidden because not significant (2): async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 78.9 ms                                                    | 74.2 ms: 1.06x faster                                      |
| pidigits       | 191 ms                                                     | 194 ms: 1.01x slower                                       |
| nbody          | 88.3 ms                                                    | 104 ms: 1.18x slower                                       |
| Geometric mean | (ref)                                                      | 1.04x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.60 ms: 1.02x faster                                      |
| regex_compile  | 137 ms                                                     | 141 ms: 1.03x slower                                       |
| regex_dna      | 221 ms                                                     | 232 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                      | 1.01x slower                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 151 ms: 1.07x faster                                       |
| pickle_list          | 5.11 us                                                    | 4.88 us: 1.05x faster                                      |
| unpickle_list        | 5.34 us                                                    | 5.21 us: 1.03x faster                                      |
| xml_etree_generate   | 87.4 ms                                                    | 90.5 ms: 1.04x slower                                      |
| pickle               | 11.5 us                                                    | 12.0 us: 1.05x slower                                      |
| tomli_loads          | 2.12 sec                                                   | 2.23 sec: 1.05x slower                                     |
| json_dumps           | 10.7 ms                                                    | 11.6 ms: 1.08x slower                                      |
| unpickle_pure_python | 218 us                                                     | 237 us: 1.09x slower                                       |
| pickle_pure_python   | 305 us                                                     | 333 us: 1.09x slower                                       |
| json_loads           | 28.9 us                                                    | 32.2 us: 1.11x slower                                      |
| xml_etree_process    | 61.2 ms                                                    | 71.1 ms: 1.16x slower                                      |
| pickle_dict          | 34.8 us                                                    | 41.2 us: 1.19x slower                                      |
| unpickle             | 15.1 us                                                    | 18.0 us: 1.19x slower                                      |
| xml_etree_iterparse  | 107 ms                                                     | 166 ms: 1.54x slower                                       |
| Geometric mean       | (ref)                                                      | 1.10x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 12.0 ms: 1.12x slower                                      |
| python_startup_no_site | 7.11 ms                                                    | 10.0 ms: 1.41x slower                                      |
| Geometric mean         | (ref)                                                      | 1.26x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_xml      | 51.6 ms                                                    | 54.7 ms: 1.06x slower                                      |
| genshi_text     | 23.7 ms                                                    | 26.1 ms: 1.10x slower                                      |
| django_template | 34.8 ms                                                    | 39.1 ms: 1.12x slower                                      |
| mako            | 11.2 ms                                                    | 16.3 ms: 1.45x slower                                      |
| Geometric mean  | (ref)                                                      | 1.17x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 1.82 ms                                                    | 1.03 ms: 1.77x faster                                      |
| gc_traversal               | 3.98 ms                                                    | 2.57 ms: 1.55x faster                                      |
| typing_runtime_protocols   | 165 us                                                     | 122 us: 1.35x faster                                       |
| async_tree_io              | 939 ms                                                     | 796 ms: 1.18x faster                                       |
| async_tree_io_tg           | 936 ms                                                     | 828 ms: 1.13x faster                                       |
| pylint                     | 317 ms                                                     | 296 ms: 1.07x faster                                       |
| xml_etree_parse            | 162 ms                                                     | 151 ms: 1.07x faster                                       |
| mypy2                      | 742 ms                                                     | 696 ms: 1.07x faster                                       |
| float                      | 78.9 ms                                                    | 74.2 ms: 1.06x faster                                      |
| pickle_list                | 5.11 us                                                    | 4.88 us: 1.05x faster                                      |
| scimark_fft                | 392 ms                                                     | 380 ms: 1.03x faster                                       |
| richards                   | 50.9 ms                                                    | 49.2 ms: 1.03x faster                                      |
| unpickle_list              | 5.34 us                                                    | 5.21 us: 1.03x faster                                      |
| crypto_pyaes               | 77.5 ms                                                    | 75.5 ms: 1.03x faster                                      |
| pyflate                    | 484 ms                                                     | 474 ms: 1.02x faster                                       |
| regex_effbot               | 3.67 ms                                                    | 3.60 ms: 1.02x faster                                      |
| richards_super             | 57.4 ms                                                    | 56.3 ms: 1.02x faster                                      |
| bench_mp_pool              | 23.9 ms                                                    | 23.4 ms: 1.02x faster                                      |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                       |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                      |
| scimark_lu                 | 122 ms                                                     | 121 ms: 1.01x faster                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.25 ms: 1.00x faster                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.85 sec: 1.01x slower                                     |
| html5lib                   | 67.2 ms                                                    | 67.9 ms: 1.01x slower                                      |
| spectral_norm              | 116 ms                                                     | 118 ms: 1.01x slower                                       |
| pidigits                   | 191 ms                                                     | 194 ms: 1.01x slower                                       |
| scimark_sor                | 127 ms                                                     | 129 ms: 1.02x slower                                       |
| dulwich_log                | 67.2 ms                                                    | 69.0 ms: 1.03x slower                                      |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                     |
| regex_compile              | 137 ms                                                     | 141 ms: 1.03x slower                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 458 ms: 1.03x slower                                       |
| deepcopy_reduce            | 3.35 us                                                    | 3.46 us: 1.03x slower                                      |
| xml_etree_generate         | 87.4 ms                                                    | 90.5 ms: 1.04x slower                                      |
| nqueens                    | 81.4 ms                                                    | 84.7 ms: 1.04x slower                                      |
| tornado_http               | 94.6 ms                                                    | 98.6 ms: 1.04x slower                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 612 ms: 1.04x slower                                       |
| async_generators           | 442 ms                                                     | 463 ms: 1.05x slower                                       |
| pickle                     | 11.5 us                                                    | 12.0 us: 1.05x slower                                      |
| regex_dna                  | 221 ms                                                     | 232 ms: 1.05x slower                                       |
| sqlglot_normalize          | 110 ms                                                     | 116 ms: 1.05x slower                                       |
| hexiom                     | 6.30 ms                                                    | 6.62 ms: 1.05x slower                                      |
| pprint_safe_repr           | 758 ms                                                     | 797 ms: 1.05x slower                                       |
| meteor_contest             | 110 ms                                                     | 115 ms: 1.05x slower                                       |
| generators                 | 29.6 ms                                                    | 31.2 ms: 1.05x slower                                      |
| tomli_loads                | 2.12 sec                                                   | 2.23 sec: 1.05x slower                                     |
| pprint_pformat             | 1.56 sec                                                   | 1.64 sec: 1.06x slower                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 646 ms: 1.06x slower                                       |
| sqlite_synth               | 2.99 us                                                    | 3.17 us: 1.06x slower                                      |
| genshi_xml                 | 51.6 ms                                                    | 54.7 ms: 1.06x slower                                      |
| deepcopy                   | 367 us                                                     | 390 us: 1.06x slower                                       |
| go                         | 145 ms                                                     | 154 ms: 1.06x slower                                       |
| fannkuch                   | 402 ms                                                     | 428 ms: 1.07x slower                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 59.3 ms: 1.07x slower                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 74.0 ms: 1.07x slower                                      |
| gunicorn                   | 1.28 ms                                                    | 1.37 ms: 1.08x slower                                      |
| aiohttp                    | 1.18 ms                                                    | 1.27 ms: 1.08x slower                                      |
| chaos                      | 61.3 ms                                                    | 66.2 ms: 1.08x slower                                      |
| json_dumps                 | 10.7 ms                                                    | 11.6 ms: 1.08x slower                                      |
| telco                      | 8.41 ms                                                    | 9.09 ms: 1.08x slower                                      |
| 2to3                       | 274 ms                                                     | 296 ms: 1.08x slower                                       |
| docutils                   | 2.83 sec                                                   | 3.07 sec: 1.08x slower                                     |
| unpickle_pure_python       | 218 us                                                     | 237 us: 1.09x slower                                       |
| logging_silent             | 105 ns                                                     | 114 ns: 1.09x slower                                       |
| pickle_pure_python         | 305 us                                                     | 333 us: 1.09x slower                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.78 ms: 1.09x slower                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.44 ms: 1.09x slower                                      |
| json                       | 5.31 ms                                                    | 5.81 ms: 1.09x slower                                      |
| pathlib                    | 17.3 ms                                                    | 19.0 ms: 1.10x slower                                      |
| genshi_text                | 23.7 ms                                                    | 26.1 ms: 1.10x slower                                      |
| logging_format             | 6.47 us                                                    | 7.18 us: 1.11x slower                                      |
| json_loads                 | 28.9 us                                                    | 32.2 us: 1.11x slower                                      |
| python_startup             | 10.8 ms                                                    | 12.0 ms: 1.12x slower                                      |
| comprehensions             | 16.6 us                                                    | 18.5 us: 1.12x slower                                      |
| raytrace                   | 267 ms                                                     | 298 ms: 1.12x slower                                       |
| logging_simple             | 5.74 us                                                    | 6.43 us: 1.12x slower                                      |
| async_tree_none_tg         | 336 ms                                                     | 377 ms: 1.12x slower                                       |
| django_template            | 34.8 ms                                                    | 39.1 ms: 1.12x slower                                      |
| chameleon                  | 7.22 ms                                                    | 8.24 ms: 1.14x slower                                      |
| deepcopy_memo              | 39.7 us                                                    | 45.6 us: 1.15x slower                                      |
| sympy_integrate            | 20.5 ms                                                    | 23.8 ms: 1.16x slower                                      |
| xml_etree_process          | 61.2 ms                                                    | 71.1 ms: 1.16x slower                                      |
| nbody                      | 88.3 ms                                                    | 104 ms: 1.18x slower                                       |
| pickle_dict                | 34.8 us                                                    | 41.2 us: 1.19x slower                                      |
| unpickle                   | 15.1 us                                                    | 18.0 us: 1.19x slower                                      |
| sympy_str                  | 282 ms                                                     | 354 ms: 1.25x slower                                       |
| deltablue                  | 3.25 ms                                                    | 4.16 ms: 1.28x slower                                      |
| mdp                        | 2.79 sec                                                   | 3.64 sec: 1.31x slower                                     |
| sympy_expand               | 473 ms                                                     | 623 ms: 1.32x slower                                       |
| sympy_sum                  | 156 ms                                                     | 211 ms: 1.36x slower                                       |
| python_startup_no_site     | 7.11 ms                                                    | 10.0 ms: 1.41x slower                                      |
| mako                       | 11.2 ms                                                    | 16.3 ms: 1.45x slower                                      |
| xml_etree_iterparse        | 107 ms                                                     | 166 ms: 1.54x slower                                       |
| flaskblogging              | 9.01 ms                                                    | 18.7 ms: 2.08x slower                                      |
| bench_thread_pool          | 834 us                                                     | 2.42 ms: 2.91x slower                                      |
| coverage                   | 93.1 ms                                                    | 712 ms: 7.65x slower                                       |
| thrift                     | 823 us                                                     | 9.43 ms: 11.46x slower                                     |
| Geometric mean             | (ref)                                                      | 1.12x slower                                               |

Benchmark hidden because not significant (4): async_tree_none, regex_v8, asyncio_tcp, async_tree_memoization
Ignored benchmarks (3) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, dask, djangocms

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.07x