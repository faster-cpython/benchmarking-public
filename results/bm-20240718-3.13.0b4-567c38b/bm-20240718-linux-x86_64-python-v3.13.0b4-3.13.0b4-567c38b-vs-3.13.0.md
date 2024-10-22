# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b4
- machine: linux-x86_64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.01x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| chameleon      | 6.85 ms                                                | 6.96 ms: 1.02x slower                                      |
| docutils       | 2.58 sec                                               | 2.75 sec: 1.06x slower                                     |
| html5lib       | 64.5 ms                                                | 67.1 ms: 1.04x slower                                      |
| tornado_http   | 91.5 ms                                                | 91.7 ms: 1.00x slower                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 429 ms: 1.08x faster                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                     |
| asyncio_tcp                | 488 ms                                                 | 492 ms: 1.01x slower                                       |
| async_tree_none_tg         | 320 ms                                                 | 325 ms: 1.02x slower                                       |
| async_tree_none            | 354 ms                                                 | 366 ms: 1.03x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 595 ms: 1.04x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 570 ms: 1.05x slower                                       |
| async_tree_io              | 843 ms                                                 | 902 ms: 1.07x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 901 ms: 1.09x slower                                       |
| Geometric mean             | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (4): async_generators, asyncio_websockets, coroutines, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 78.5 ms                                                | 76.8 ms: 1.02x faster                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.77 ms: 1.03x faster                                      |
| regex_compile  | 131 ms                                                 | 132 ms: 1.00x slower                                       |
| regex_dna      | 220 ms                                                 | 232 ms: 1.06x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 87.3 ms: 1.00x slower                                      |
| xml_etree_process    | 60.4 ms                                                | 60.9 ms: 1.01x slower                                      |
| tomli_loads          | 2.11 sec                                               | 2.13 sec: 1.01x slower                                     |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| pickle_pure_python   | 300 us                                                 | 303 us: 1.01x slower                                       |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                       |
| xml_etree_parse      | 156 ms                                                 | 158 ms: 1.01x slower                                       |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                       |
| json_loads           | 27.0 us                                                | 27.9 us: 1.04x slower                                      |
| Geometric mean       | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                      |
| python_startup_no_site | 6.99 ms                                                | 7.10 ms: 1.02x slower                                      |
| Geometric mean         | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 34.4 ms                                                | 34.1 ms: 1.01x faster                                      |
| mako            | 11.1 ms                                                | 11.0 ms: 1.01x faster                                      |
| genshi_xml      | 50.3 ms                                                | 50.7 ms: 1.01x slower                                      |
| genshi_text     | 22.9 ms                                                | 23.1 ms: 1.01x slower                                      |
| Geometric mean  | (ref)                                                  | 1.00x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mypy2                      | 1.07 sec                                               | 717 ms: 1.49x faster                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 429 ms: 1.08x faster                                       |
| json                       | 5.20 ms                                                | 5.01 ms: 1.04x faster                                      |
| regex_effbot               | 3.88 ms                                                | 3.77 ms: 1.03x faster                                      |
| pprint_safe_repr           | 744 ms                                                 | 724 ms: 1.03x faster                                       |
| mdp                        | 2.74 sec                                               | 2.67 sec: 1.03x faster                                     |
| pprint_pformat             | 1.51 sec                                               | 1.47 sec: 1.03x faster                                     |
| nqueens                    | 80.6 ms                                                | 78.9 ms: 1.02x faster                                      |
| float                      | 78.5 ms                                                | 76.8 ms: 1.02x faster                                      |
| gc_traversal               | 3.81 ms                                                | 3.74 ms: 1.02x faster                                      |
| telco                      | 8.45 ms                                                | 8.34 ms: 1.01x faster                                      |
| django_template            | 34.4 ms                                                | 34.1 ms: 1.01x faster                                      |
| mako                       | 11.1 ms                                                | 11.0 ms: 1.01x faster                                      |
| go                         | 142 ms                                                 | 141 ms: 1.00x faster                                       |
| richards_super             | 54.4 ms                                                | 54.2 ms: 1.00x faster                                      |
| sqlglot_optimize           | 53.9 ms                                                | 53.7 ms: 1.00x faster                                      |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                      |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                       |
| tornado_http               | 91.5 ms                                                | 91.7 ms: 1.00x slower                                      |
| sympy_integrate            | 19.9 ms                                                | 19.9 ms: 1.00x slower                                      |
| xml_etree_generate         | 87.0 ms                                                | 87.3 ms: 1.00x slower                                      |
| regex_compile              | 131 ms                                                 | 132 ms: 1.00x slower                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                      |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.01x slower                                       |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.01x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                     |
| asyncio_tcp                | 488 ms                                                 | 492 ms: 1.01x slower                                       |
| raytrace                   | 262 ms                                                 | 264 ms: 1.01x slower                                       |
| genshi_xml                 | 50.3 ms                                                | 50.7 ms: 1.01x slower                                      |
| xml_etree_process          | 60.4 ms                                                | 60.9 ms: 1.01x slower                                      |
| scimark_lu                 | 115 ms                                                 | 116 ms: 1.01x slower                                       |
| tomli_loads                | 2.11 sec                                               | 2.13 sec: 1.01x slower                                     |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| pickle_pure_python         | 300 us                                                 | 303 us: 1.01x slower                                       |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                       |
| dulwich_log                | 63.0 ms                                                | 63.7 ms: 1.01x slower                                      |
| genshi_text                | 22.9 ms                                                | 23.1 ms: 1.01x slower                                      |
| deepcopy_memo              | 38.0 us                                                | 38.5 us: 1.01x slower                                      |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.01x slower                                       |
| xml_etree_parse            | 156 ms                                                 | 158 ms: 1.01x slower                                       |
| deepcopy                   | 352 us                                                 | 357 us: 1.01x slower                                       |
| deepcopy_reduce            | 3.17 us                                                | 3.21 us: 1.02x slower                                      |
| python_startup_no_site     | 6.99 ms                                                | 7.10 ms: 1.02x slower                                      |
| chameleon                  | 6.85 ms                                                | 6.96 ms: 1.02x slower                                      |
| async_tree_none_tg         | 320 ms                                                 | 325 ms: 1.02x slower                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                      |
| chaos                      | 58.4 ms                                                | 59.5 ms: 1.02x slower                                      |
| crypto_pyaes               | 73.0 ms                                                | 74.4 ms: 1.02x slower                                      |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                       |
| xml_etree_iterparse        | 102 ms                                                 | 105 ms: 1.03x slower                                       |
| deltablue                  | 3.15 ms                                                | 3.25 ms: 1.03x slower                                      |
| async_tree_none            | 354 ms                                                 | 366 ms: 1.03x slower                                       |
| json_loads                 | 27.0 us                                                | 27.9 us: 1.04x slower                                      |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 595 ms: 1.04x slower                                       |
| html5lib                   | 64.5 ms                                                | 67.1 ms: 1.04x slower                                      |
| scimark_monte_carlo        | 66.3 ms                                                | 69.1 ms: 1.04x slower                                      |
| pyflate                    | 460 ms                                                 | 481 ms: 1.05x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 570 ms: 1.05x slower                                       |
| fannkuch                   | 381 ms                                                 | 402 ms: 1.06x slower                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.96 sec: 1.06x slower                                     |
| regex_dna                  | 220 ms                                                 | 232 ms: 1.06x slower                                       |
| docutils                   | 2.58 sec                                               | 2.75 sec: 1.06x slower                                     |
| dask                       | 338 ms                                                 | 361 ms: 1.07x slower                                       |
| async_tree_io              | 843 ms                                                 | 902 ms: 1.07x slower                                       |
| scimark_sor                | 122 ms                                                 | 131 ms: 1.07x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 901 ms: 1.09x slower                                       |
| coverage                   | 83.7 ms                                                | 91.7 ms: 1.09x slower                                      |
| create_gc_cycles           | 1.61 ms                                                | 1.78 ms: 1.11x slower                                      |
| Geometric mean             | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (25): pylint, pycparser, logging_simple, sympy_expand, pathlib, typing_runtime_protocols, logging_format, async_generators, scimark_sparse_mat_mult, richards, regex_v8, nbody, hexiom, bench_thread_pool, spectral_norm, 2to3, sqlglot_normalize, asyncio_websockets, bench_mp_pool, sympy_str, generators, thrift, scimark_fft, coroutines, async_tree_memoization
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x