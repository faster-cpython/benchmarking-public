# Results vs. 3.13.0

- fork: nohlson
- ref: enable_fortify_sourc
- machine: linux-x86_64
- commit hash: 7a595e7
- commit date: 2024-07-14
- overall geometric mean: 1.01x faster
- HPT reliability: 61.46%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 263 ms: 1.01x faster                                                   |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                 |
| html5lib       | 64.5 ms                                                | 64.9 ms: 1.01x slower                                                  |
| tornado_http   | 91.5 ms                                                | 89.8 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 377 ms: 1.23x faster                                                   |
| async_tree_none_tg        | 320 ms                                                 | 294 ms: 1.09x faster                                                   |
| async_tree_none           | 354 ms                                                 | 326 ms: 1.09x faster                                                   |
| async_tree_memoization    | 442 ms                                                 | 408 ms: 1.09x faster                                                   |
| async_generators          | 433 ms                                                 | 428 ms: 1.01x faster                                                   |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                   |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                 |
| asyncio_tcp               | 488 ms                                                 | 492 ms: 1.01x slower                                                   |
| coroutines                | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                  |
| async_tree_io_tg          | 825 ms                                                 | 848 ms: 1.03x slower                                                   |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 78.1 ms: 1.01x faster                                                  |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                   |
| nbody          | 85.7 ms                                                | 91.4 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 23.9 ms: 1.06x faster                                                  |
| regex_effbot   | 3.88 ms                                                | 3.68 ms: 1.06x faster                                                  |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 59.6 ms: 1.01x faster                                                  |
| xml_etree_generate   | 87.0 ms                                                | 85.9 ms: 1.01x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 211 us: 1.01x faster                                                   |
| pickle_pure_python   | 300 us                                                 | 303 us: 1.01x slower                                                   |
| xml_etree_parse      | 156 ms                                                 | 158 ms: 1.01x slower                                                   |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| json_loads           | 27.0 us                                                | 27.4 us: 1.02x slower                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                  |
| python_startup_no_site | 6.99 ms                                                | 7.09 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 34.3 ms: 1.00x faster                                                  |
| genshi_text     | 22.9 ms                                                | 23.1 ms: 1.01x slower                                                  |
| mako            | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 262 us: 1.35x faster                                                   |
| deepcopy_memo             | 38.0 us                                                | 30.0 us: 1.27x faster                                                  |
| async_tree_memoization_tg | 465 ms                                                 | 377 ms: 1.23x faster                                                   |
| deepcopy_reduce           | 3.17 us                                                | 2.65 us: 1.19x faster                                                  |
| pathlib                   | 17.1 ms                                                | 15.6 ms: 1.09x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 294 ms: 1.09x faster                                                   |
| async_tree_none           | 354 ms                                                 | 326 ms: 1.09x faster                                                   |
| async_tree_memoization    | 442 ms                                                 | 408 ms: 1.09x faster                                                   |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.72 ms: 1.07x faster                                                  |
| mdp                       | 2.74 sec                                               | 2.57 sec: 1.07x faster                                                 |
| pycparser                 | 1.19 sec                                               | 1.13 sec: 1.06x faster                                                 |
| regex_v8                  | 25.3 ms                                                | 23.9 ms: 1.06x faster                                                  |
| regex_effbot              | 3.88 ms                                                | 3.68 ms: 1.06x faster                                                  |
| gc_traversal              | 3.81 ms                                                | 3.69 ms: 1.03x faster                                                  |
| bench_thread_pool         | 815 us                                                 | 792 us: 1.03x faster                                                   |
| logging_simple            | 5.66 us                                                | 5.51 us: 1.03x faster                                                  |
| logging_format            | 6.25 us                                                | 6.09 us: 1.03x faster                                                  |
| nqueens                   | 80.6 ms                                                | 78.5 ms: 1.03x faster                                                  |
| richards_super            | 54.4 ms                                                | 53.1 ms: 1.02x faster                                                  |
| spectral_norm             | 115 ms                                                 | 112 ms: 1.02x faster                                                   |
| richards                  | 48.1 ms                                                | 47.2 ms: 1.02x faster                                                  |
| scimark_lu                | 115 ms                                                 | 113 ms: 1.02x faster                                                   |
| json                      | 5.20 ms                                                | 5.10 ms: 1.02x faster                                                  |
| tornado_http              | 91.5 ms                                                | 89.8 ms: 1.02x faster                                                  |
| regex_dna                 | 220 ms                                                 | 217 ms: 1.01x faster                                                   |
| telco                     | 8.45 ms                                                | 8.34 ms: 1.01x faster                                                  |
| xml_etree_process         | 60.4 ms                                                | 59.6 ms: 1.01x faster                                                  |
| xml_etree_generate        | 87.0 ms                                                | 85.9 ms: 1.01x faster                                                  |
| async_generators          | 433 ms                                                 | 428 ms: 1.01x faster                                                   |
| unpickle_pure_python      | 213 us                                                 | 211 us: 1.01x faster                                                   |
| go                        | 142 ms                                                 | 140 ms: 1.01x faster                                                   |
| sqlglot_optimize          | 53.9 ms                                                | 53.5 ms: 1.01x faster                                                  |
| 2to3                      | 265 ms                                                 | 263 ms: 1.01x faster                                                   |
| float                     | 78.5 ms                                                | 78.1 ms: 1.01x faster                                                  |
| sympy_integrate           | 19.9 ms                                                | 19.8 ms: 1.00x faster                                                  |
| django_template           | 34.4 ms                                                | 34.3 ms: 1.00x faster                                                  |
| sqlglot_normalize         | 107 ms                                                 | 107 ms: 1.00x faster                                                   |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                  |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                   |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                 |
| html5lib                  | 64.5 ms                                                | 64.9 ms: 1.01x slower                                                  |
| asyncio_tcp               | 488 ms                                                 | 492 ms: 1.01x slower                                                   |
| pprint_pformat            | 1.51 sec                                               | 1.52 sec: 1.01x slower                                                 |
| pickle_pure_python        | 300 us                                                 | 303 us: 1.01x slower                                                   |
| genshi_text               | 22.9 ms                                                | 23.1 ms: 1.01x slower                                                  |
| pidigits                  | 186 ms                                                 | 188 ms: 1.01x slower                                                   |
| xml_etree_parse           | 156 ms                                                 | 158 ms: 1.01x slower                                                   |
| dulwich_log               | 63.0 ms                                                | 63.7 ms: 1.01x slower                                                  |
| sqlglot_transpile         | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                  |
| json_dumps                | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| python_startup_no_site    | 6.99 ms                                                | 7.09 ms: 1.02x slower                                                  |
| json_loads                | 27.0 us                                                | 27.4 us: 1.02x slower                                                  |
| generators                | 28.8 ms                                                | 29.3 ms: 1.02x slower                                                  |
| pyflate                   | 460 ms                                                 | 467 ms: 1.02x slower                                                   |
| typing_runtime_protocols  | 159 us                                                 | 162 us: 1.02x slower                                                   |
| hexiom                    | 6.13 ms                                                | 6.24 ms: 1.02x slower                                                  |
| coroutines                | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                  |
| scimark_sor               | 122 ms                                                 | 126 ms: 1.03x slower                                                   |
| sqlglot_parse             | 1.27 ms                                                | 1.30 ms: 1.03x slower                                                  |
| xml_etree_iterparse       | 102 ms                                                 | 105 ms: 1.03x slower                                                   |
| chaos                     | 58.4 ms                                                | 59.9 ms: 1.03x slower                                                  |
| raytrace                  | 262 ms                                                 | 269 ms: 1.03x slower                                                   |
| async_tree_io_tg          | 825 ms                                                 | 848 ms: 1.03x slower                                                   |
| mako                      | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                  |
| scimark_monte_carlo       | 66.3 ms                                                | 68.8 ms: 1.04x slower                                                  |
| docutils                  | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                 |
| deltablue                 | 3.15 ms                                                | 3.29 ms: 1.05x slower                                                  |
| bpe_tokeniser             | 4.69 sec                                               | 4.91 sec: 1.05x slower                                                 |
| fannkuch                  | 381 ms                                                 | 401 ms: 1.05x slower                                                   |
| logging_silent            | 102 ns                                                 | 108 ns: 1.05x slower                                                   |
| dask                      | 338 ms                                                 | 359 ms: 1.06x slower                                                   |
| nbody                     | 85.7 ms                                                | 91.4 ms: 1.07x slower                                                  |
| create_gc_cycles          | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                  |
| coverage                  | 83.7 ms                                                | 93.1 ms: 1.11x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (17): pylint, async_tree_cpu_io_mixed, sympy_str, async_tree_cpu_io_mixed_tg, sympy_expand, genshi_xml, comprehensions, sympy_sum, crypto_pyaes, regex_compile, thrift, bench_mp_pool, meteor_contest, pprint_safe_repr, scimark_fft, tomli_loads, async_tree_io
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 61.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x