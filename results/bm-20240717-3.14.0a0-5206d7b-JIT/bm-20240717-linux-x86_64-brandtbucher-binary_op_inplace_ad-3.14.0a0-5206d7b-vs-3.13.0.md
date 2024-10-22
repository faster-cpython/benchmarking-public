# Results vs. 3.13.0

- fork: brandtbucher
- ref: binary_op_inplace_ad
- machine: linux-x86_64
- commit hash: 5206d7b
- commit date: 2024-07-17
- overall geometric mean: 1.01x faster
- HPT reliability: 53.58%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 273 ms: 1.03x slower                                                        |
| docutils       | 2.58 sec                                               | 2.86 sec: 1.11x slower                                                      |
| html5lib       | 64.5 ms                                                | 65.0 ms: 1.01x slower                                                       |
| tornado_http   | 91.5 ms                                                | 94.2 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 376 ms: 1.24x faster                                                        |
| async_tree_none            | 354 ms                                                 | 322 ms: 1.10x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 408 ms: 1.08x faster                                                        |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 561 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 538 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                      |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                       |
| async_tree_io_tg           | 825 ms                                                 | 844 ms: 1.02x slower                                                        |
| asyncio_tcp                | 488 ms                                                 | 503 ms: 1.03x slower                                                        |
| async_generators           | 433 ms                                                 | 456 ms: 1.05x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (2): async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.1 ms: 1.12x faster                                                       |
| nbody          | 85.7 ms                                                | 80.0 ms: 1.07x faster                                                       |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.75 ms: 1.04x faster                                                       |
| regex_v8       | 25.3 ms                                                | 24.4 ms: 1.03x faster                                                       |
| regex_compile  | 131 ms                                                 | 136 ms: 1.04x slower                                                        |
| regex_dna      | 220 ms                                                 | 229 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                      |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                        |
| xml_etree_generate   | 87.0 ms                                                | 81.8 ms: 1.06x faster                                                       |
| xml_etree_process    | 60.4 ms                                                | 58.2 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 102 ms                                                 | 100 ms: 1.02x faster                                                        |
| json_loads           | 27.0 us                                                | 27.5 us: 1.02x slower                                                       |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (2): json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.81 ms: 1.13x faster                                                       |
| django_template | 34.4 ms                                                | 36.1 ms: 1.05x slower                                                       |
| genshi_text     | 22.9 ms                                                | 25.1 ms: 1.10x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 57.7 ms: 1.15x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 28.8 us: 1.32x faster                                                       |
| deepcopy                   | 352 us                                                 | 271 us: 1.30x faster                                                        |
| async_tree_memoization_tg  | 465 ms                                                 | 376 ms: 1.24x faster                                                        |
| scimark_fft                | 369 ms                                                 | 312 ms: 1.18x faster                                                        |
| deepcopy_reduce            | 3.17 us                                                | 2.68 us: 1.18x faster                                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.31 ms: 1.16x faster                                                       |
| richards                   | 48.1 ms                                                | 42.2 ms: 1.14x faster                                                       |
| mako                       | 11.1 ms                                                | 9.81 ms: 1.13x faster                                                       |
| float                      | 78.5 ms                                                | 70.1 ms: 1.12x faster                                                       |
| richards_super             | 54.4 ms                                                | 48.7 ms: 1.12x faster                                                       |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.11x faster                                                        |
| async_tree_none            | 354 ms                                                 | 322 ms: 1.10x faster                                                        |
| scimark_monte_carlo        | 66.3 ms                                                | 60.6 ms: 1.09x faster                                                       |
| tomli_loads                | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 408 ms: 1.08x faster                                                        |
| mdp                        | 2.74 sec                                               | 2.55 sec: 1.08x faster                                                      |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.07x faster                                                        |
| nbody                      | 85.7 ms                                                | 80.0 ms: 1.07x faster                                                       |
| crypto_pyaes               | 73.0 ms                                                | 68.1 ms: 1.07x faster                                                       |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                        |
| xml_etree_generate         | 87.0 ms                                                | 81.8 ms: 1.06x faster                                                       |
| fannkuch                   | 381 ms                                                 | 360 ms: 1.06x faster                                                        |
| pyflate                    | 460 ms                                                 | 435 ms: 1.06x faster                                                        |
| pathlib                    | 17.1 ms                                                | 16.2 ms: 1.05x faster                                                       |
| pycparser                  | 1.19 sec                                               | 1.14 sec: 1.05x faster                                                      |
| telco                      | 8.45 ms                                                | 8.06 ms: 1.05x faster                                                       |
| pprint_safe_repr           | 744 ms                                                 | 710 ms: 1.05x faster                                                        |
| pprint_pformat             | 1.51 sec                                               | 1.45 sec: 1.04x faster                                                      |
| xml_etree_process          | 60.4 ms                                                | 58.2 ms: 1.04x faster                                                       |
| regex_effbot               | 3.88 ms                                                | 3.75 ms: 1.04x faster                                                       |
| gc_traversal               | 3.81 ms                                                | 3.67 ms: 1.04x faster                                                       |
| logging_format             | 6.25 us                                                | 6.04 us: 1.03x faster                                                       |
| regex_v8                   | 25.3 ms                                                | 24.4 ms: 1.03x faster                                                       |
| logging_simple             | 5.66 us                                                | 5.48 us: 1.03x faster                                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 561 ms: 1.02x faster                                                        |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 102 ms                                                 | 100 ms: 1.02x faster                                                        |
| json                       | 5.20 ms                                                | 5.14 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 538 ms: 1.01x faster                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                      |
| html5lib                   | 64.5 ms                                                | 65.0 ms: 1.01x slower                                                       |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.77 sec: 1.02x slower                                                      |
| json_loads                 | 27.0 us                                                | 27.5 us: 1.02x slower                                                       |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                       |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.61 ms: 1.02x slower                                                       |
| async_tree_io_tg           | 825 ms                                                 | 844 ms: 1.02x slower                                                        |
| bench_thread_pool          | 815 us                                                 | 835 us: 1.02x slower                                                        |
| python_startup_no_site     | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                       |
| tornado_http               | 91.5 ms                                                | 94.2 ms: 1.03x slower                                                       |
| generators                 | 28.8 ms                                                | 29.7 ms: 1.03x slower                                                       |
| 2to3                       | 265 ms                                                 | 273 ms: 1.03x slower                                                        |
| asyncio_tcp                | 488 ms                                                 | 503 ms: 1.03x slower                                                        |
| logging_silent             | 102 ns                                                 | 106 ns: 1.03x slower                                                        |
| sqlglot_optimize           | 53.9 ms                                                | 55.8 ms: 1.04x slower                                                       |
| regex_compile              | 131 ms                                                 | 136 ms: 1.04x slower                                                        |
| go                         | 142 ms                                                 | 147 ms: 1.04x slower                                                        |
| regex_dna                  | 220 ms                                                 | 229 ms: 1.04x slower                                                        |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                                        |
| django_template            | 34.4 ms                                                | 36.1 ms: 1.05x slower                                                       |
| async_generators           | 433 ms                                                 | 456 ms: 1.05x slower                                                        |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                                        |
| scimark_sor                | 122 ms                                                 | 129 ms: 1.06x slower                                                        |
| nqueens                    | 80.6 ms                                                | 85.9 ms: 1.07x slower                                                       |
| dask                       | 338 ms                                                 | 362 ms: 1.07x slower                                                        |
| scimark_lu                 | 115 ms                                                 | 123 ms: 1.07x slower                                                        |
| sympy_expand               | 462 ms                                                 | 498 ms: 1.08x slower                                                        |
| sympy_str                  | 274 ms                                                 | 295 ms: 1.08x slower                                                        |
| pylint                     | 313 ms                                                 | 338 ms: 1.08x slower                                                        |
| dulwich_log                | 63.0 ms                                                | 68.1 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 159 us                                                 | 173 us: 1.09x slower                                                        |
| hexiom                     | 6.13 ms                                                | 6.65 ms: 1.09x slower                                                       |
| create_gc_cycles           | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                       |
| genshi_text                | 22.9 ms                                                | 25.1 ms: 1.10x slower                                                       |
| docutils                   | 2.58 sec                                               | 2.86 sec: 1.11x slower                                                      |
| coverage                   | 83.7 ms                                                | 93.4 ms: 1.12x slower                                                       |
| sympy_sum                  | 150 ms                                                 | 167 ms: 1.12x slower                                                        |
| sympy_integrate            | 19.9 ms                                                | 22.3 ms: 1.12x slower                                                       |
| genshi_xml                 | 50.3 ms                                                | 57.7 ms: 1.15x slower                                                       |
| deltablue                  | 3.15 ms                                                | 3.66 ms: 1.16x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (7): json_dumps, async_tree_io, pickle_pure_python, asyncio_websockets, bench_mp_pool, chaos, thrift
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 53.58% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x