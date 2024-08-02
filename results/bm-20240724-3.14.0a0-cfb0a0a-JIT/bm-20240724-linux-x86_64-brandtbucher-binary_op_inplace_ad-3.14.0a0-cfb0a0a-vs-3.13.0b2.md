# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: binary_op_inplace_ad
- machine: linux-x86_64
- commit hash: cfb0a0a
- commit date: 2024-07-24
- overall geometric mean: 1.04x faster
- HPT reliability: 99.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 273 ms: 1.00x faster                                                        |
| docutils       | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                      |
| html5lib       | 67.2 ms                                                    | 64.6 ms: 1.04x faster                                                       |
| tornado_http   | 94.6 ms                                                    | 95.4 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                      | 1.00x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.12x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 418 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 531 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 871 ms: 1.08x faster                                                        |
| async_tree_io              | 939 ms                                                     | 901 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.1 ms: 1.12x faster                                                       |
| nbody          | 88.3 ms                                                    | 79.8 ms: 1.11x faster                                                       |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                        |
| regex_dna      | 221 ms                                                     | 222 ms: 1.00x slower                                                        |
| regex_v8       | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                       |
| regex_effbot   | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|---------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads         | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                                      |
| xml_etree_parse     | 162 ms                                                     | 147 ms: 1.10x faster                                                        |
| xml_etree_iterparse | 107 ms                                                     | 98.9 ms: 1.09x faster                                                       |
| xml_etree_generate  | 87.4 ms                                                    | 81.0 ms: 1.08x faster                                                       |
| xml_etree_process   | 61.2 ms                                                    | 56.7 ms: 1.08x faster                                                       |
| json_loads          | 28.9 us                                                    | 28.1 us: 1.03x faster                                                       |
| json_dumps          | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                       |
| pickle_pure_python  | 305 us                                                     | 299 us: 1.02x faster                                                        |
| Geometric mean      | (ref)                                                      | 1.06x faster                                                                |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.21 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                      | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.80 ms: 1.15x faster                                                       |
| django_template | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                       |
| genshi_text     | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 58.0 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.4 us: 1.40x faster                                                       |
| deepcopy                   | 367 us                                                     | 271 us: 1.36x faster                                                        |
| scimark_fft                | 392 ms                                                     | 309 ms: 1.27x faster                                                        |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.22 ms: 1.25x faster                                                       |
| richards                   | 50.9 ms                                                    | 40.8 ms: 1.25x faster                                                       |
| richards_super             | 57.4 ms                                                    | 46.7 ms: 1.23x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                    | 2.75 us: 1.22x faster                                                       |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                        |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.1 ms: 1.15x faster                                                       |
| crypto_pyaes               | 77.5 ms                                                    | 67.4 ms: 1.15x faster                                                       |
| mako                       | 11.2 ms                                                    | 9.80 ms: 1.15x faster                                                       |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.15x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                        |
| float                      | 78.9 ms                                                    | 70.1 ms: 1.12x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.12x faster                                                        |
| pyflate                    | 484 ms                                                     | 432 ms: 1.12x faster                                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.53 sec: 1.11x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 418 ms: 1.11x faster                                                        |
| mdp                        | 2.79 sec                                                   | 2.52 sec: 1.11x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 531 ms: 1.11x faster                                                        |
| nbody                      | 88.3 ms                                                    | 79.8 ms: 1.11x faster                                                       |
| tomli_loads                | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                        |
| fannkuch                   | 402 ms                                                     | 365 ms: 1.10x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                     | 98.9 ms: 1.09x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                        |
| gc_traversal               | 3.98 ms                                                    | 3.68 ms: 1.08x faster                                                       |
| xml_etree_generate         | 87.4 ms                                                    | 81.0 ms: 1.08x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 56.7 ms: 1.08x faster                                                       |
| async_tree_io_tg           | 936 ms                                                     | 871 ms: 1.08x faster                                                        |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                                       |
| telco                      | 8.41 ms                                                    | 7.87 ms: 1.07x faster                                                       |
| pprint_safe_repr           | 758 ms                                                     | 712 ms: 1.06x faster                                                        |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.06x faster                                                      |
| meteor_contest             | 110 ms                                                     | 104 ms: 1.06x faster                                                        |
| chaos                      | 61.3 ms                                                    | 58.2 ms: 1.05x faster                                                       |
| async_tree_io              | 939 ms                                                     | 901 ms: 1.04x faster                                                        |
| html5lib                   | 67.2 ms                                                    | 64.6 ms: 1.04x faster                                                       |
| logging_format             | 6.47 us                                                    | 6.24 us: 1.04x faster                                                       |
| logging_simple             | 5.74 us                                                    | 5.56 us: 1.03x faster                                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                       |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                        |
| json                       | 5.31 ms                                                    | 5.15 ms: 1.03x faster                                                       |
| json_loads                 | 28.9 us                                                    | 28.1 us: 1.03x faster                                                       |
| thrift                     | 823 us                                                     | 800 us: 1.03x faster                                                        |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.03x faster                                                       |
| generators                 | 29.6 ms                                                    | 28.9 ms: 1.03x faster                                                       |
| regex_compile              | 137 ms                                                     | 134 ms: 1.02x faster                                                        |
| pickle_pure_python         | 305 us                                                     | 299 us: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                      |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                        |
| sqlglot_transpile          | 1.63 ms                                                    | 1.61 ms: 1.01x faster                                                       |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.01x faster                                                       |
| coverage                   | 93.1 ms                                                    | 92.1 ms: 1.01x faster                                                       |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                       |
| asyncio_tcp                | 508 ms                                                     | 504 ms: 1.01x faster                                                        |
| bench_thread_pool          | 834 us                                                     | 831 us: 1.00x faster                                                        |
| 2to3                       | 274 ms                                                     | 273 ms: 1.00x faster                                                        |
| regex_dna                  | 221 ms                                                     | 222 ms: 1.00x slower                                                        |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| tornado_http               | 94.6 ms                                                    | 95.4 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 56.0 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 110 ms                                                     | 111 ms: 1.01x slower                                                        |
| regex_v8                   | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                       |
| python_startup_no_site     | 7.11 ms                                                    | 7.21 ms: 1.01x slower                                                       |
| go                         | 145 ms                                                     | 147 ms: 1.01x slower                                                        |
| raytrace                   | 267 ms                                                     | 271 ms: 1.02x slower                                                        |
| logging_silent             | 105 ns                                                     | 107 ns: 1.02x slower                                                        |
| async_generators           | 442 ms                                                     | 453 ms: 1.03x slower                                                        |
| regex_effbot               | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                                       |
| django_template            | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                       |
| typing_runtime_protocols   | 165 us                                                     | 169 us: 1.03x slower                                                        |
| scimark_sor                | 127 ms                                                     | 132 ms: 1.03x slower                                                        |
| docutils                   | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                      |
| genshi_text                | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                                       |
| hexiom                     | 6.30 ms                                                    | 6.55 ms: 1.04x slower                                                       |
| scimark_lu                 | 122 ms                                                     | 128 ms: 1.05x slower                                                        |
| dulwich_log                | 67.2 ms                                                    | 71.2 ms: 1.06x slower                                                       |
| sympy_str                  | 282 ms                                                     | 299 ms: 1.06x slower                                                        |
| nqueens                    | 81.4 ms                                                    | 87.1 ms: 1.07x slower                                                       |
| sympy_expand               | 473 ms                                                     | 506 ms: 1.07x slower                                                        |
| sympy_integrate            | 20.5 ms                                                    | 22.3 ms: 1.09x slower                                                       |
| sympy_sum                  | 156 ms                                                     | 171 ms: 1.10x slower                                                        |
| deltablue                  | 3.25 ms                                                    | 3.60 ms: 1.11x slower                                                       |
| pylint                     | 317 ms                                                     | 353 ms: 1.11x slower                                                        |
| genshi_xml                 | 51.6 ms                                                    | 58.0 ms: 1.12x slower                                                       |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                                |

Benchmark hidden because not significant (4): dask, unpickle_pure_python, coroutines, pycparser
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.82% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x