# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: binary_op_inplace_ad
- machine: linux-x86_64
- commit hash: 5206d7b
- commit date: 2024-07-17
- overall geometric mean: 1.04x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 273 ms: 1.00x faster                                                        |
| docutils       | 2.83 sec                                                   | 2.86 sec: 1.01x slower                                                      |
| html5lib       | 67.2 ms                                                    | 65.0 ms: 1.03x faster                                                       |
| tornado_http   | 94.6 ms                                                    | 94.2 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 376 ms: 1.18x faster                                                        |
| async_tree_none            | 378 ms                                                     | 322 ms: 1.17x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 408 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                        |
| async_tree_io              | 939 ms                                                     | 840 ms: 1.12x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 844 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 538 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.13x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.1 ms: 1.12x faster                                                       |
| nbody          | 88.3 ms                                                    | 80.0 ms: 1.10x faster                                                       |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                       |
| regex_compile  | 137 ms                                                     | 136 ms: 1.00x faster                                                        |
| regex_effbot   | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                       |
| regex_dna      | 221 ms                                                     | 229 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|---------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse     | 162 ms                                                     | 146 ms: 1.11x faster                                                        |
| tomli_loads         | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                      |
| xml_etree_iterparse | 107 ms                                                     | 100 ms: 1.07x faster                                                        |
| xml_etree_generate  | 87.4 ms                                                    | 81.8 ms: 1.07x faster                                                       |
| json_loads          | 28.9 us                                                    | 27.5 us: 1.05x faster                                                       |
| xml_etree_process   | 61.2 ms                                                    | 58.2 ms: 1.05x faster                                                       |
| json_dumps          | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                       |
| pickle_pure_python  | 305 us                                                     | 300 us: 1.02x faster                                                        |
| Geometric mean      | (ref)                                                      | 1.05x faster                                                                |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.81 ms: 1.15x faster                                                       |
| django_template | 34.8 ms                                                    | 36.1 ms: 1.04x slower                                                       |
| genshi_text     | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 57.7 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.8 us: 1.38x faster                                                       |
| deepcopy                   | 367 us                                                     | 271 us: 1.35x faster                                                        |
| scimark_fft                | 392 ms                                                     | 312 ms: 1.26x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                    | 2.68 us: 1.25x faster                                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.31 ms: 1.22x faster                                                       |
| richards                   | 50.9 ms                                                    | 42.2 ms: 1.21x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 376 ms: 1.18x faster                                                        |
| richards_super             | 57.4 ms                                                    | 48.7 ms: 1.18x faster                                                       |
| async_tree_none            | 378 ms                                                     | 322 ms: 1.17x faster                                                        |
| mako                       | 11.2 ms                                                    | 9.81 ms: 1.15x faster                                                       |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.6 ms: 1.14x faster                                                       |
| crypto_pyaes               | 77.5 ms                                                    | 68.1 ms: 1.14x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 408 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                        |
| float                      | 78.9 ms                                                    | 70.1 ms: 1.12x faster                                                       |
| spectral_norm              | 116 ms                                                     | 104 ms: 1.12x faster                                                        |
| async_tree_io              | 939 ms                                                     | 840 ms: 1.12x faster                                                        |
| fannkuch                   | 402 ms                                                     | 360 ms: 1.12x faster                                                        |
| pyflate                    | 484 ms                                                     | 435 ms: 1.11x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 844 ms: 1.11x faster                                                        |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                        |
| nbody                      | 88.3 ms                                                    | 80.0 ms: 1.10x faster                                                       |
| tomli_loads                | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                      |
| mdp                        | 2.79 sec                                                   | 2.55 sec: 1.09x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 538 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                        |
| gc_traversal               | 3.98 ms                                                    | 3.67 ms: 1.08x faster                                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.45 sec: 1.07x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                     | 100 ms: 1.07x faster                                                        |
| logging_format             | 6.47 us                                                    | 6.04 us: 1.07x faster                                                       |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                                       |
| xml_etree_generate         | 87.4 ms                                                    | 81.8 ms: 1.07x faster                                                       |
| pprint_safe_repr           | 758 ms                                                     | 710 ms: 1.07x faster                                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.77 sec: 1.05x faster                                                      |
| json_loads                 | 28.9 us                                                    | 27.5 us: 1.05x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 58.2 ms: 1.05x faster                                                       |
| logging_simple             | 5.74 us                                                    | 5.48 us: 1.05x faster                                                       |
| chaos                      | 61.3 ms                                                    | 58.6 ms: 1.05x faster                                                       |
| telco                      | 8.41 ms                                                    | 8.06 ms: 1.04x faster                                                       |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                        |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                       |
| html5lib                   | 67.2 ms                                                    | 65.0 ms: 1.03x faster                                                       |
| json                       | 5.31 ms                                                    | 5.14 ms: 1.03x faster                                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                       |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| thrift                     | 823 us                                                     | 799 us: 1.03x faster                                                        |
| regex_v8                   | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.03x faster                                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                       |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                        |
| pycparser                  | 1.16 sec                                                   | 1.14 sec: 1.02x faster                                                      |
| dask                       | 369 ms                                                     | 362 ms: 1.02x faster                                                        |
| pickle_pure_python         | 305 us                                                     | 300 us: 1.02x faster                                                        |
| sqlglot_transpile          | 1.63 ms                                                    | 1.61 ms: 1.02x faster                                                       |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                       |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                       |
| asyncio_tcp                | 508 ms                                                     | 503 ms: 1.01x faster                                                        |
| tornado_http               | 94.6 ms                                                    | 94.2 ms: 1.00x faster                                                       |
| regex_compile              | 137 ms                                                     | 136 ms: 1.00x faster                                                        |
| 2to3                       | 274 ms                                                     | 273 ms: 1.00x faster                                                        |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 55.8 ms: 1.01x slower                                                       |
| logging_silent             | 105 ns                                                     | 106 ns: 1.01x slower                                                        |
| python_startup_no_site     | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                       |
| docutils                   | 2.83 sec                                                   | 2.86 sec: 1.01x slower                                                      |
| dulwich_log                | 67.2 ms                                                    | 68.1 ms: 1.01x slower                                                       |
| scimark_sor                | 127 ms                                                     | 129 ms: 1.01x slower                                                        |
| scimark_lu                 | 122 ms                                                     | 123 ms: 1.02x slower                                                        |
| go                         | 145 ms                                                     | 147 ms: 1.02x slower                                                        |
| regex_effbot               | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                       |
| raytrace                   | 267 ms                                                     | 273 ms: 1.02x slower                                                        |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                                        |
| async_generators           | 442 ms                                                     | 456 ms: 1.03x slower                                                        |
| regex_dna                  | 221 ms                                                     | 229 ms: 1.04x slower                                                        |
| django_template            | 34.8 ms                                                    | 36.1 ms: 1.04x slower                                                       |
| sympy_str                  | 282 ms                                                     | 295 ms: 1.05x slower                                                        |
| typing_runtime_protocols   | 165 us                                                     | 173 us: 1.05x slower                                                        |
| sympy_expand               | 473 ms                                                     | 498 ms: 1.05x slower                                                        |
| nqueens                    | 81.4 ms                                                    | 85.9 ms: 1.06x slower                                                       |
| hexiom                     | 6.30 ms                                                    | 6.65 ms: 1.06x slower                                                       |
| genshi_text                | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                       |
| pylint                     | 317 ms                                                     | 338 ms: 1.07x slower                                                        |
| sympy_sum                  | 156 ms                                                     | 167 ms: 1.07x slower                                                        |
| sympy_integrate            | 20.5 ms                                                    | 22.3 ms: 1.09x slower                                                       |
| genshi_xml                 | 51.6 ms                                                    | 57.7 ms: 1.12x slower                                                       |
| deltablue                  | 3.25 ms                                                    | 3.66 ms: 1.12x slower                                                       |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                                |

Benchmark hidden because not significant (5): unpickle_pure_python, comprehensions, bench_thread_pool, generators, coverage
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x