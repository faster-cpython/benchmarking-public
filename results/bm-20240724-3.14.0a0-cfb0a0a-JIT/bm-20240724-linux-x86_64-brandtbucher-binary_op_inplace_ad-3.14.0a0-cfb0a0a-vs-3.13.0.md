# Results vs. 3.13.0

- fork: brandtbucher
- ref: binary_op_inplace_ad
- machine: linux-x86_64
- commit hash: cfb0a0a
- commit date: 2024-07-24
- overall geometric mean: 1.01x faster
- HPT reliability: 50.61%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 273 ms: 1.03x slower                                                        |
| docutils       | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                      |
| tornado_http   | 91.5 ms                                                | 95.4 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                        |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                        |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 418 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 531 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 565 ms: 1.02x faster                                                        |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                       |
| asyncio_tcp                | 488 ms                                                 | 504 ms: 1.03x slower                                                        |
| async_generators           | 433 ms                                                 | 453 ms: 1.05x slower                                                        |
| async_tree_io_tg           | 825 ms                                                 | 871 ms: 1.05x slower                                                        |
| async_tree_io              | 843 ms                                                 | 901 ms: 1.07x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.1 ms: 1.12x faster                                                       |
| nbody          | 85.7 ms                                                | 79.8 ms: 1.07x faster                                                       |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                       |
| regex_v8       | 25.3 ms                                                | 25.4 ms: 1.01x slower                                                       |
| regex_dna      | 220 ms                                                 | 222 ms: 1.01x slower                                                        |
| regex_compile  | 131 ms                                                 | 134 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                      |
| xml_etree_generate   | 87.0 ms                                                | 81.0 ms: 1.07x faster                                                       |
| xml_etree_process    | 60.4 ms                                                | 56.7 ms: 1.07x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                        |
| xml_etree_iterparse  | 102 ms                                                 | 98.9 ms: 1.03x faster                                                       |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                        |
| json_loads           | 27.0 us                                                | 28.1 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (2): pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.21 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.80 ms: 1.13x faster                                                       |
| django_template | 34.4 ms                                                | 35.8 ms: 1.04x slower                                                       |
| genshi_text     | 22.9 ms                                                | 24.6 ms: 1.08x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 58.0 ms: 1.15x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 28.4 us: 1.34x faster                                                       |
| deepcopy                   | 352 us                                                 | 271 us: 1.30x faster                                                        |
| scimark_fft                | 369 ms                                                 | 309 ms: 1.19x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.22 ms: 1.19x faster                                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                        |
| richards                   | 48.1 ms                                                | 40.8 ms: 1.18x faster                                                       |
| richards_super             | 54.4 ms                                                | 46.7 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 3.17 us                                                | 2.75 us: 1.15x faster                                                       |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.13x faster                                                        |
| mako                       | 11.1 ms                                                | 9.80 ms: 1.13x faster                                                       |
| float                      | 78.5 ms                                                | 70.1 ms: 1.12x faster                                                       |
| scimark_monte_carlo        | 66.3 ms                                                | 60.1 ms: 1.10x faster                                                       |
| tomli_loads                | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                      |
| mdp                        | 2.74 sec                                               | 2.52 sec: 1.09x faster                                                      |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                        |
| crypto_pyaes               | 73.0 ms                                                | 67.4 ms: 1.08x faster                                                       |
| telco                      | 8.45 ms                                                | 7.87 ms: 1.07x faster                                                       |
| nbody                      | 85.7 ms                                                | 79.8 ms: 1.07x faster                                                       |
| xml_etree_generate         | 87.0 ms                                                | 81.0 ms: 1.07x faster                                                       |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                        |
| xml_etree_process          | 60.4 ms                                                | 56.7 ms: 1.07x faster                                                       |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                                        |
| pyflate                    | 460 ms                                                 | 432 ms: 1.06x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 418 ms: 1.06x faster                                                        |
| pathlib                    | 17.1 ms                                                | 16.2 ms: 1.05x faster                                                       |
| pprint_safe_repr           | 744 ms                                                 | 712 ms: 1.04x faster                                                        |
| fannkuch                   | 381 ms                                                 | 365 ms: 1.04x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.53 sec: 1.04x faster                                                      |
| meteor_contest             | 108 ms                                                 | 104 ms: 1.03x faster                                                        |
| gc_traversal               | 3.81 ms                                                | 3.68 ms: 1.03x faster                                                       |
| pprint_pformat             | 1.51 sec                                               | 1.46 sec: 1.03x faster                                                      |
| xml_etree_iterparse        | 102 ms                                                 | 98.9 ms: 1.03x faster                                                       |
| regex_effbot               | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                       |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 531 ms: 1.02x faster                                                        |
| logging_simple             | 5.66 us                                                | 5.56 us: 1.02x faster                                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 565 ms: 1.02x faster                                                        |
| json                       | 5.20 ms                                                | 5.15 ms: 1.01x faster                                                       |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                                        |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                        |
| regex_v8                   | 25.3 ms                                                | 25.4 ms: 1.01x slower                                                       |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                       |
| regex_dna                  | 220 ms                                                 | 222 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                       |
| bench_thread_pool          | 815 us                                                 | 831 us: 1.02x slower                                                        |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                        |
| regex_compile              | 131 ms                                                 | 134 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.61 ms: 1.02x slower                                                       |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                       |
| 2to3                       | 265 ms                                                 | 273 ms: 1.03x slower                                                        |
| python_startup_no_site     | 6.99 ms                                                | 7.21 ms: 1.03x slower                                                       |
| asyncio_tcp                | 488 ms                                                 | 504 ms: 1.03x slower                                                        |
| raytrace                   | 262 ms                                                 | 271 ms: 1.04x slower                                                        |
| go                         | 142 ms                                                 | 147 ms: 1.04x slower                                                        |
| sqlglot_normalize          | 107 ms                                                 | 111 ms: 1.04x slower                                                        |
| sqlglot_optimize           | 53.9 ms                                                | 56.0 ms: 1.04x slower                                                       |
| django_template            | 34.4 ms                                                | 35.8 ms: 1.04x slower                                                       |
| json_loads                 | 27.0 us                                                | 28.1 us: 1.04x slower                                                       |
| tornado_http               | 91.5 ms                                                | 95.4 ms: 1.04x slower                                                       |
| logging_silent             | 102 ns                                                 | 107 ns: 1.04x slower                                                        |
| async_generators           | 433 ms                                                 | 453 ms: 1.05x slower                                                        |
| async_tree_io_tg           | 825 ms                                                 | 871 ms: 1.05x slower                                                        |
| typing_runtime_protocols   | 159 us                                                 | 169 us: 1.06x slower                                                        |
| async_tree_io              | 843 ms                                                 | 901 ms: 1.07x slower                                                        |
| hexiom                     | 6.13 ms                                                | 6.55 ms: 1.07x slower                                                       |
| scimark_sor                | 122 ms                                                 | 132 ms: 1.07x slower                                                        |
| genshi_text                | 22.9 ms                                                | 24.6 ms: 1.08x slower                                                       |
| nqueens                    | 80.6 ms                                                | 87.1 ms: 1.08x slower                                                       |
| dask                       | 338 ms                                                 | 365 ms: 1.08x slower                                                        |
| create_gc_cycles           | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                       |
| sympy_str                  | 274 ms                                                 | 299 ms: 1.09x slower                                                        |
| sympy_expand               | 462 ms                                                 | 506 ms: 1.10x slower                                                        |
| coverage                   | 83.7 ms                                                | 92.1 ms: 1.10x slower                                                       |
| scimark_lu                 | 115 ms                                                 | 128 ms: 1.11x slower                                                        |
| sympy_integrate            | 19.9 ms                                                | 22.3 ms: 1.12x slower                                                       |
| pylint                     | 313 ms                                                 | 353 ms: 1.13x slower                                                        |
| dulwich_log                | 63.0 ms                                                | 71.2 ms: 1.13x slower                                                       |
| docutils                   | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                      |
| sympy_sum                  | 150 ms                                                 | 171 ms: 1.14x slower                                                        |
| deltablue                  | 3.15 ms                                                | 3.60 ms: 1.14x slower                                                       |
| genshi_xml                 | 50.3 ms                                                | 58.0 ms: 1.15x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (9): chaos, logging_format, pickle_pure_python, comprehensions, bench_mp_pool, html5lib, generators, json_dumps, thrift
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 50.61% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x